import os
import logging
from ConfigParser import SafeConfigParser
from ansibleWrap import ansibleWrap
from OpenStackClient import OpenStackClient


def qbrGet(hypinstqbr):
    '''This function needs to be changed to use the neutron command line utility.
    The command line can give you port ids associated with an instance'''
    '''This port id associated with an instance is used to create the qvo port on the bridge.'''
    #Left OFF HERE. NEED TO  TO SSH INTO VM AND STORE RESULT IN VARIABLE. THIS RESULT
    #WILL THEN BE USED TO CRAFT THE OVS COMMAND NECESSARY TO RUN ON THE HYPERVISOR YOU HAVE SSH'D INTO

    #Lots of dependencies here. 
    #The inventory file needs to be in place
    #Creating it quickly below. A better solution will need to be to come up with later. 
    #ALSO DNS NEEDS TO BE IN PLACE FOR THE HOSTNAMES OF THE HYPERVISORS.
    f = open('/Users/none/ansible_hosts','w')

    for hypervisor in hypinstqbr.keys():
        f.write(hypervisor + '  ansible_ssh_user=root\n')

    #Closing file handler
    f.close()

    
    for host in hypinstqbr.keys():
    #The below for loop crafts the command that will be run on each of the hypervisors. This command
    #is only used to determine the abr ports associated with the instances.

        for instance in hypinstqbr[host]:
            #Change logic below to actually ssh into the vm and execute this command and then store
            #the result into a variable
            bridgeIntCmd = 'cat /var/lib/nova/instances/' + instance + '/libvirt.xml | egrep -o qbr........... | sed \'s/qbr/qvo/\''

            #Actually filling the qbr port associated with the instance in the hypinsqbr dictionary
            a = ansibleWrap()
            #The below output contains the qvo port associated with the instance

            qvoPort = a.runCommand(bridgeIntCmd)['contacted'][host]['stdout']
            print 'Instance: ' + instance + ' has qvo port: ' + qvoPort + ' assigned to it.'

            #Filling in qvo port section of dictionary
            hypinstqbr[host][instance] = qvoPort

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
    print qbrGet(hypinstqbr)



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



    #-store the output of the above command in a variable ex) qbr7b8da7ed-66
    #-Make a new variable called switchPort that will be the be of the format qvo7b8da7ed-66
    #-Create appropriate ovs commands for the appropriate hypervisor








