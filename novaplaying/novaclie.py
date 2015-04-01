import os
import logging
from ConfigParser import SafeConfigParser

from keystoneclient.v2_0 import client as keystone_client
from novaclient import client as nova_client
# from quantumclient.v2_0 import client as quantum_client
# from glanceclient import client as glance_client

LOG = logging.getLogger(__name__)

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
    
    # ''' Method to connect to quantum and get a client reference '''
    # def connect_quantum(self):
    #     self.quantum = quantum_client.Client(username=self.user, password=self.password, tenant_name=self.tenant_name, auth_url=self.auth_url, no_cache=True)
    #     return self.quantum 

    # ''' Method to verify the connection to quantum '''
    # def _verify_quantum(self):
    #     if not self.quantum:
    #         self.connect_quantum()
    #     else:
    #         try:
    #             self.quantum.list_networks()
    #         except:
    #             self.connect_quantum()


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

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s')
    LOG.setLevel(logging.INFO)

    KEYSTONE_URL = "http://192.168.1.220:5000/v2.0/"
    USERNAME = "admin"
    PASSWORD = "password"
    TENANT = "admin"

    osc = OpenStackClient(username=USERNAME, password=PASSWORD, tenant_name=TENANT, auth_url=KEYSTONE_URL)

    #Creating nova object that will be used to interact with nova apis
    nova = osc.connect_nova()

    # List all servers per hypervisor
    for h in nova.hypervisors.list():

        #Putting the below in a try catch, just in the event there is something strange with the compute services, and
        #values are returned.
        try:
            #Creating list of what instances are on the hypervisor in question
            servers = nova.hypervisors.search(h.hypervisor_hostname,True)[0].servers

            #Printing hypervisor name and what instances are currently on it.
            print h.hypervisor_hostname + ' has the following instances on it: \n ' + str(servers)
        except:
            pass

    #Add functionality to determine what tenants instances are on what hypervisors








