import os
import logging
from ConfigParser import SafeConfigParser
from ansibleWrap import ansibleWrap
from OpenStackClient import OpenStackClient


def qbrGet(hypinstqbr,nova,neutron):
    '''This function needs to be changed to use the neutron command line utility.
    The command line can give you port ids associated with an instance'''
    '''This port id associated with an instance is used to create the qvo port on the bridge.'''
        #Creating neutron object that will be used to interact with the neutron apis.


    #Able to grab the network and ip address of vm with this command
    #Only grabbing the network for right now this will need to change later. As of right now
    #It is grabbing the private ip address of the first nic only, later on ability will need to be added
    #so multiple nics can be looked at.
    # I just realized you probably should populate the hypinstqbrdictionary with the private ip address of the vm
    privateIP = nova.servers.list()[1].networks.values()[0][0]


    #Take IP address found above and search through the list of dictonarys for it. Print the dictionary that it is associated with
    
    for val in neutron.list_ports()['ports']:
        for ip in val['fixed_ips']:
            if ip.values()[1] == privateIP:
                print 'match found'

            #print int hypinstqbr dictionary after qvo port was added to a particular instance

            #At this point the hypinstqbr dictionary looks like the following below.
            #What data structure looks like after coming back from the qbrGet function.
            #Data structure returned from some function that goes in and does the magic of getting this stuff
            # hypinstqbr = {
            # "host1":{
            #     "instanceId1": 'qbr7b8da7ed-66',
            #     "instanceId2": 'qbr7b2da2ef-16',
            #     "instanceId3": 'qbr4b2d32ef-26'
            #     },
            # "host2":{
            #     "instanceId4": 'qbr4b2d32ef-26',
            #     "instanceId5": 'qbr4a2d12ef-76'
            # }

            #returning the updated dictionary
            return hypinstqbr

if __name__ == "__main__":

    KEYSTONE_URL = "http://192.168.1.220:5000/v2.0/"
    USERNAME = "admin"
    PASSWORD = "password"
    TENANT = "admin"

    osc = OpenStackClient(username=USERNAME, password=PASSWORD, tenant_name=TENANT, auth_url=KEYSTONE_URL)

    #Creating nova object that will be used to interact with nova apis
    nova = osc.connect_nova()

    #Creating keystone object that will be used to interact with the keystone apis
    keystone = osc.connect_keystone()

    #Creating neutron object that will be used to interact with the neutron apis.
    neutron = osc.connect_neutron()

    #Creating empty dictionary that will hold the tenant_id to name mapping
    tenantDictionary = {}    

    #The below dictionary is very important. When everything is said and done it will be in the following format
    #hypervisor is self explanatory but the dictionary inside econtains the instance associated with the tenant
    #and the corresponding qbr port. This port is important because it will later be used to craft the appropriate
    #ovs command on the bridge.
    # hypinstqbr = {
    # "hypervisor1":{
    #     "instanceId1": 'qbr7b8da7ed-66',
    #     "instanceId2": 'qbr7b2da2ef-16',
    #     "instanceId3": 'qbr4b2d32ef-26'
    #     },
    # "hypervisor2":{
    #     "instanceId4": 'qbr4b2d32ef-26',
    #     "instanceId5": 'qbr4a2d12ef-76'
    # }
    hypinstqbr = {}

    #Creating bridge interfaces list used to store all of the bridge interfaces
    bridgeInterfaces = []

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
            #associated as a value in the hypinstqbr dictionary
            tenantInstances = {}

            #For loop to look at each instance on the hypervisor and determine if it is in the tenant in question
            for instance in instances:
                #If a tenant_id associated with an instance matches the original tenant_id the user submitted, a dictionary will be filled.
                if nova.servers.get(instance['uuid']).tenant_id == tenant_id:
                    #Filling tenantInstance list
                    tenantInstances[nova.servers.get(instance['uuid']).id] = ''

                    #Printing uuid of the instance in the specific tenant and the hypervisor that it is on.
                    print nova.servers.get(instance['uuid']).human_id + ' is on hypervisor: ' + h.hypervisor_hostname

                    #Left off here. You will need to take advantage of below call to grab the first private ip address
                    #associated with the instance and add it to the dictionary to be used later
                    print nova.servers.get(instance['uuid']).networks

            #Filling hypinstqbr dictionary. This holds the instance to hypervisor mapping for a specifc tenant
            #For example vm1,vm2,vm3 are in tenant Microsoft. vm1 exists on hypervisor1, vm2 and vm3 exists on hypervisor2
            #so the dictionary will look like this hypinstqbr['hypervisor1'] = ['vm1'], hypinstqbr['hypervisor1'] = ['vm2','vm3']
            if tenantInstances:
                #Filling hypervisor to instance dictionary
                hypinstqbr[h.hypervisor_hostname] = tenantInstances

        except:
            pass

    #this dictionary holds the instances associated with a specific tenant and what hypervisor they are on
    #with the dictionary below we can create the linux commands to run on the hypervisor determine
    #the qv interface attached to br-int on the hypervisor
    print hypinstqbr


    #What data structure looks like before going into the below for loop
    # hypinstqbr = {
    # "host1":{
    #     "instanceId1": '',
    #     "instanceId2": '',
    #     "instanceId3": '',
    #     },
    # "host2":{
    #     "instanceId4": '',
    #     "instanceId5": ''
    # }

    #go get qbr ports!
    # print qbrGet(hypinstqbr,nova,neutron)



    #What data structure looks like after coming back from the qbrGet function.
    #Data structure returned from some function that goes in and does the magic of getting this stuff
    # hypinstqbr = {
    # "host1":{
    #     "instanceId1": 'qbr7b8da7ed-66',
    #     "instanceId2": 'qbr7b2da2ef-16',
    #     "instanceId3": 'qbr4b2d32ef-26'
    #     },
    # "host2":{
    #     "instanceId4": 'qbr4b2d32ef-26',
    #     "instanceId5": 'qbr4a2d12ef-76'
    # }








