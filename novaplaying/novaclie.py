import os
import logging
from ConfigParser import SafeConfigParser
from ansibleWrap import ansibleWrap
from OpenStackClient import OpenStackClient
import argparse


if __name__ == "__main__":

    #Reading in command line arguements
    #Creating parser object that will be used for command line arguments
    parser = argparse.ArgumentParser()

    #Adding keystone endpoint arguement to parser object. 
    parser.add_argument('--auth_url', required=True, 
    nargs='?', help='This is the url to your keystone endpoint.')

    #Adding username arguement to parser object. 
    parser.add_argument('--username', required=True, 
    nargs='?', help='This is the username arguement. This username will need to have access to the tenant in question.')

    #Adding password arguement to parser object. 
    parser.add_argument('--password', required=True, 
    nargs='?', help='This is the password arguement. This is the password for the associated username.')

    #Adding tenant arguement to parser object. 
    parser.add_argument('--tenant', required=True, 
    nargs='?', help='This is the tenant arguement. The username in question will need access to this tenant')

    #Creating args object that will hold each of the arguments sent into
    #the parser object.
    args = parser.parse_args()

    #now you need to add the above arguements to the instantiation of the below osc object.

    osc = OpenStackClient(username=args.username, password=args.password, tenant_name=args.tenant, auth_url=args.auth_url)

    # osc = OpenStackClient(username=USERNAME, password=PASSWORD, tenant_name=TENANT, auth_url=KEYSTONE_URL)

    #Creating nova object that will be used to interact with nova apis
    nova = osc.connect_nova()

    #Creating keystone object that will be used to interact with the keystone apis
    keystone = osc.connect_keystone()

    #Creating neutron object that will be used to interact with the neutron apis.
    neutron = osc.connect_neutron()

    #Creating empty dictionary that will hold the tenant_id to name mapping
    tenantDictionary = {}    

    #The below dictionary is very important. When everything is said and done it will be in the following format
    #hypervisor is self explanatory but the dictionary inside contains the instance associated with the tenant
    #and the corresponding qbr port. This port is important because it will later be used to craft the appropriate
    #ovs command on the bridge.
    # hypinstqbr = {
    # "hypervisor1":{
    #     "instanceId1": {IP_ADDRESS:'qbr7b8da7ed-66'},
    #     "instanceId2": {IP_ADDRESS:'qbr7b2da2ef-16'},
    #     "instanceId3": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     },
    # "hypervisor2":{
    #     "instanceId4": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     "instanceId5": {IP_ADDRESS: 'qbr4a2d12ef-76'}
    # }
    hypinstqbr = {}

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

            #Dictionary that will hold instances associated with a tenant on a specific hypervisor. This list will be 
            #associated as a value in the hypinstqbr dictionary
            tenantInstances = {}

            #Dictionary that will host instances private ip address and port associated with the private ip address
            instanceNetworkandPort = {}

            #For loop to look at each instance on the hypervisor and determine if it is in the tenant in question
            for instance in instances:
                #If a tenant_id associated with an instance matches the original tenant_id the user submitted, a dictionary will be filled.
                if nova.servers.get(instance['uuid']).tenant_id == tenant_id:
                    #Filling tenantInstance dictionary with empty instnaceNetworkandPort dictionary.
                    tenantInstances[nova.servers.get(instance['uuid']).id] = instanceNetworkandPort

                    #Left off here. You will need to take advantage of below call to grab the first private ip address
                    #associated with the instance and add it to the dictionary to be used later
                    ip_addr = nova.servers.get(instance['uuid']).networks.values()[0][0]

                    #What data structures looks like before going into the below for loop nested dictionary
                    #is declared as instanceNetworkandPort it will be of the format {IP_ADDR:PORT_ID}
                    # tenantInstances =  {"instanceId1": {}, "instanceId2": {}, "instanceId3": {}}

                    #grabbing port
                    for val in neutron.list_ports()['ports']:
                        if val['fixed_ips'][0]['ip_address'] == ip_addr:
                            #Creating the whole qvo port string. This is the holy grail. Because
                            #with this we know what port id on br-int is associated with what instance.
                            portID = 'qvo'+val['id'][0:11]
                            instanceNetworkandPort[val['fixed_ips'][0]['ip_address']] = portID

                    #Adding instanceNetworkandPort dictionary as value to the tenantInstances key of instanceID
                    #after this point the data structure will look like the following
                    #tenantInstances =  {"instanceId1": {'192.168.1.23': '7b8da7ed-66f2-4369-8406-cd3fe2ec737e'}}
                    tenantInstances[nova.servers.get(instance['uuid']).id] = instanceNetworkandPort

                    #Clearing the dictionary because we don't want the old values appended to the new instance at
                    #the start of this for loop.
                    instanceNetworkandPort = {}
                    

            #Filling hypinstqbr dictionary. This holds the instance to hypervisor mapping for a specifc tenant
            #For example vm1,vm2,vm3 are in tenant Microsoft. vm1 exists on hypervisor1, vm2 and vm3 exists on hypervisor2
            #so the dictionary will look like this hypinstqbr['hypervisor1'] = ['vm1'], hypinstqbr['hypervisor1'] = ['vm2','vm3']
            if tenantInstances:
                #Filling hypervisor to instance dictionary
                hypinstqbr[h.hypervisor_hostname] = tenantInstances
        except:
            pass

    #this dictionary holds the instances associated with a the specific tenant and what hypervisor they are on.
    #the dictionary will look like the following:
    # hypinstqbr = {
    # "hypervisor1":{
    #     "instanceId1": {IP_ADDRESS:'qbr7b8da7ed-66'},
    #     "instanceId2": {IP_ADDRESS:'qbr7b2da2ef-16'},
    #     "instanceId3": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     },
    # "hypervisor2":{
    #     "instanceId4": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     "instanceId5": {IP_ADDRESS: 'qbr4a2d12ef-76'}
    # }

    print hypinstqbr



