#!/usr/bin/python

import commands, sys

import os
import logging
from ConfigParser import SafeConfigParser
from keystoneclient.v2_0 import client as keystone_client
from novaclient import client as nova_client
from neutronclient.v2_0 import client as neutron_client
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

def createExternal(neutron):
    '''This function will create the public network. This network will be used for floating ip addresses and 
    the network that the external gateway is pulled from for tenant routers'''
    ##########################    Creating External Network    ##########################

    try:
        #Creating dictionary to pass to the create_network function
        body_sample = {'network': {'name': network_name,
                       'admin_state_up': True, 'router:external': True}}
     
        #Creating network - This will return a dictionary object that will be used later
        netw = neutron.create_network(body=body_sample)

        #The below two elements will be used to create a subnet within a network
        net_dict = netw['network']
        network_id = net_dict['id']

        print('Network %s created' % network_id)
     
        #Creating subnet that will be assocaited with the previously created network
        body_create_subnet = {'subnets': [{'cidr': '192.168.1.0/24',
                              'ip_version': 4, 'network_id': network_id,
                              'enable_dhcp': False, 'allocation_pools':[
                             {'start': '192.168.1.50', 
                             'end': '192.168.1.90'}],
                            'gateway_ip': '192.168.1.1'}]}
     
        #Creating network
        subnet = neutron.create_subnet(body=body_create_subnet)
        print('Created subnet %s' % subnet)


    finally:
        print("Execution completed")

    ######################################################################################

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s')
    LOG.setLevel(logging.INFO)
    KEYSTONE_URL = "http://192.168.1.220:5000/v2.0/"
    USERNAME = "admin"
    PASSWORD = "password"
    TENANT = "admin"

    #Creating osc object that will be used to interact with each of the openstack services
    osc = OpenStackClient(username=USERNAME, password=PASSWORD, tenant_name=TENANT, auth_url=KEYSTONE_URL)
    #Creating nova object that will be used to interact with nova apis
    nova = osc.connect_nova()

    #Creating keystone object that will be used to interact with the keystone apis.
    keystone = osc.connect_keystone()

    #Creating neutron object that will be used to interact with the neutron apis.
    neutron = osc.connect_neutron()

    #Specifying network name
    network_name = 'public'

    for val in neutron.list_networks()['networks']:
        if val['name'] == 'public':
            print 'Print public subnet already created...'
        else:
            #Call to create external network
            createExternal(neutron)











    