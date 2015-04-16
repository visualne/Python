from keystoneclient.v2_0 import client as keystone_client
from novaclient import client as nova_client
from neutronclient.v2_0 import client as neutron_client

class OpenStackClient():

    def __init__(self, username=None, password=None, tenant_name=None, auth_url=None):
        self.user = username
        self.password = password
        self.tenant_name = tenant_name
        self.auth_url = auth_url

    ''' Method to connect to keystone and get a client reference '''
    def connect_keystone(self):
        self.keystone = keystone_client.Client(username=self.user, password=self.password, tenant_name=self.tenant_name, auth_url=self.auth_url)
        return self.keystone

    ''' Method to verify the connection to keystone '''
    def _verify_keystone(self):
        if not self.keystone:
            self.connect_keystone()
        else:
            try:
                self.keystone.tenants.list()
            except:
                self.connect_keystone()

    ''' Method to connect to nova and get a client reference. Needed to add version=2 to constructor'''
    def connect_nova(self, service_type="compute"):
        self.nova = nova_client.Client(version=2, username=self.user, api_key=self.password, project_id=self.tenant_name, auth_url=self.auth_url, no_cache=True, service_type = service_type)
        return self.nova

    ''' Method to verify the connection to nova '''
    def _verify_nova(self):
        if not self.nova:
            self.connect_nova()
        else:
            try:
                self.nova.images.list()
            except:
                self.connect_nova()
    
    ''' Method to connect to neutron and get a client reference '''
    def connect_neutron(self):
        self.neutron = neutron_client.Client(username=self.user, password=self.password, tenant_name=self.tenant_name, auth_url=self.auth_url, no_cache=True)
        return self.neutron
    
    ''' Method to verify the connection to neutron '''
    def _verify_neutron(self):
        if not self.neutron:
            self.connect_neutron()
        else:
            try:
                self.neutron.list_networks()
            except:
                self.connect_neutron()


    # ''' Method to connect to glance and get a client reference '''
    # def connect_glance(self):
    #     keystone = self.connect_keystone()
    #     glance_endpoint = keystone.service_catalog.url_for(service_type='image', endpoint_type='publicURL')
    #     print keystone.auth_token
    #     self.glance = glance_client.Client('1', endpoint=glance_endpoint, token=keystone.auth_token)
    #     return self.glance; 

    # ''' Method to verify the connection to glance '''
    # def _connect_glance(self):
    #     if not self.glance:
    #         self.connect_glance()
    #     else:
    #         try:
    #             self.glance.images.list()
    #         except:
    #             self.connect_glance()