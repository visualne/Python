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

    #Creating keystone object that will be used to interact with the keystone apis
    keystone = osc.connect_keystone()

    #Creating empty dictionary that will hold the tenant_id to name mapping
    tenantDictionary = {}

    #Instance to hypervisor dictionary in format. {Hypervisor:instance1,instance2,instance3}
    instanceToHypervisor = {}

    #Creating dictionary holding keystone tenant id and keystone tenant name.
    for val in keystone.tenants.list():
        #Filling dicionary
        tenantDictionary[val.id] = val.name

        #Determining the uuid of the Garrett tenant. We will need this later, this tenat will also be
        #used as input from the user later
        if tenantDictionary[val.id] == 'Garrett':
            tenant_id = val.id

    
    #List all servers per hypervisor
    for h in nova.hypervisors.list():

        #Putting the below in a try catch, just in the event there is something strange with the compute services, and
        #values are returned.
        try:
            # #Creating list of what instances are on the hypervisor in question
            instances = nova.hypervisors.search(h.hypervisor_hostname,True)[0].servers

            #List that will hold instances associated with a tenant on a specific hypervisor. This list will be 
            #associated as a value in the instanceToHypervisor dictionary
            tenantInstances = []

            #For loop to look at each instance on the hypervisor and determine if it is in the tenant in question
            for instance in instances:
                #If a tenant_id associated with an instance matches the original tenant_id the user submitted, a dictionary will be filled.
                if nova.servers.get(instance['uuid']).tenant_id == tenant_id:
                    #Filling tenantInstance list
                    tenantInstances.append(nova.servers.get(instance['uuid']).human_id)

                    #Printing uuid of the instance in the specific tenant and the hypervisor that it is on.
                    print nova.servers.get(instance['uuid']).human_id + ' is on hypervisor: ' + h.hypervisor_hostname

            #Filling instanceToHypervisor dictionary. This holds the instance to hypervisor mapping for a specifc tenant
            #For example vm1,vm2,vm3 are in tenant Microsoft. vm1 exists on hypervisor1, vm2 and vm3 exists on hypervisor2
            #so the dictionary will look like this instanceToHypervisor['hypervisor1'] = ['vm1'], instanceToHypervisor['hypervisor1'] = ['vm2','vm3']
            if tenantInstances:
                #Filling hypervisor to instance dictionary
                instanceToHypervisor[h.hypervisor_hostname] = tenantInstances

        except:
            pass

    #this dictionary holds the instances associated with a specific tenant and what hypervisor they are on
    #with the dictionary below we can create the linux commands to run on the hypervisor determine
    #the qv interface attached to br-int on the hypervisor
    print instanceToHypervisor



    #Logic here to push down ovs command to appropriate hypervisors
    #-ssh to the hypervisor in question
    #-cat /var/lib/nova/instances/INSTANCE_ID/libvirt.xml | grep bridge
    #-store the output of the above command in a variable ex) qbr7b8da7ed-66
    #-Make a new variable called switchPort that will be the be of the format qvo7b8da7ed-66
    #-Create appropriate ovs commands for the appropriate hypervisor








