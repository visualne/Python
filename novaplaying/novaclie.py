import os
import logging
from ConfigParser import SafeConfigParser
from ansibleWrap import ansibleWrap
from OpenStackClient import OpenStackClient
import argparse

def userInput(hypinstqbr):
    '''This function is used to determine what instances the user wants to span traffic for: (format: instance1,instance2,instance3)'''
    for values in hypinstqbr.values():
        for key in values.keys():
            print key

    var = raw_input("What instances would you like to span traffic for (format: instance1,instance2,instance3): ")

    #Grabbing command line arguements
    arguements = var.split(',')

    for k, v in hypinstqbr.items():
        print k, '>', v

    #Determining the hypervisor and qvo port associated with the instance(s) that were selected.
    for k, v in hypinstqbr.items():
        for instance in v.keys():
            if instance in arguements:
                # print v[instance].values()
                print 'Hypervisor:' + k + ' Instance:' + instance + ' Port:' + v[instance].values()[0]

    #Clearing bridge
    #ovs-vsctl clear Bridge br-int mirrors

    #Creating GRE tunnels
    #ovs-vsctl add-port br-int gre0 -- set interface gre0 type=gre options:remote_ip=192.168.2.2 options:key=30    
 
    #Creating ovs commands to SPAN traffic to gre port
    #ovs-vsctl -- set Bridge br-int mirrors=@m  -- --id=@gre0 get Port gre0  -- --id=@qvo5650c159-ed get Port qvo5650c159-ed  -- --id=@m create Mirror name=mymirror \
    #select-dst-port=@qvo5650c159-ed select-src-port=@qvo5650c159-ed output-port=@gre0

    #list mirrors
    #ovs-vsctl list Bridge br0

    #shows openflow port numbers
    #ovs-ofctl show br-tun

    #delete all flows from a specific table

    #adding flow rules to br-tun
    #You will need to grab things like tunnel id and openflow port numbers once they
    #are created on the bridge.
    #ovs-ofctl add-flow br-tun "table=0,priority=1,in_port=4,actions=resubmit(,3)"
    #ovs-ofctl add-flow br-tun "table=3,priority=1,tun_id=30,actions=mod_vlan_vid:1,output:1"
    #For whatever reason the packet isn't being forwarded over the patch port at this point,
    #however the GRE headers are gone after these two flow rules are done.



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
    #     "Instance Name": {IP_ADDRESS:'qbr7b8da7ed-66'},
    #     "Instance Name": {IP_ADDRESS:'qbr7b2da2ef-16'},
    #     "Instance Name": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     },
    # "hypervisor2":{
    #     "Instance Name": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     "Instance Name": {IP_ADDRESS: 'qbr4a2d12ef-76'}
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
                    # tenantInstances[nova.servers.get(instance['uuid']).id] = instanceNetworkandPort
                    tenantInstances[nova.servers.get(instance['uuid']).name] = instanceNetworkandPort

                    #Left off here. You will need to take advantage of below call to grab the first private ip address
                    #associated with the instance and add it to the dictionary to be used later
                    ip_addr = nova.servers.get(instance['uuid']).networks.values()[0][0]

                    #What data structures looks like before going into the below for loop nested dictionary
                    #is declared as instanceNetworkandPort it will be of the format {IP_ADDR:PORT_ID}
                    # tenantInstances =  {"Instance Name": {}, "Instance Name": {}, "Instance Name": {}}

                    #grabbing port
                    for val in neutron.list_ports()['ports']:
                        if val['fixed_ips'][0]['ip_address'] == ip_addr:
                            #Creating the whole qvo port string. This is the holy grail. Because
                            #with this we know what port id on br-int is associated with what instance.
                            portID = 'qvo'+val['id'][0:11]
                            instanceNetworkandPort[val['fixed_ips'][0]['ip_address']] = portID

                    #Adding instanceNetworkandPort dictionary as value to the tenantInstances key of instanceID
                    #after this point the data structure will look like the following
                    #tenantInstances =  {"Instance Name": {'192.168.1.23': '7b8da7ed-66f2-4369-8406-cd3fe2ec737e'}}
                    tenantInstances[nova.servers.get(instance['uuid']).name] = instanceNetworkandPort

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
    #     "Instance Name": {IP_ADDRESS:'qbr7b8da7ed-66'},
    #     "Instance Name": {IP_ADDRESS:'qbr7b2da2ef-16'},
    #     "Instance Name": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     },
    # "hypervisor2":{
    #     "Instance Name": {IP_ADDRESS: 'qbr4b2d32ef-26'},
    #     "Instance Name": {IP_ADDRESS: 'qbr4a2d12ef-76'}
    # }

    #Ask user what instances they would like to span traffic for
    userInput(hypinstqbr)
    # print '\n' + str(hypinstqbr)
