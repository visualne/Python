import os
import logging
from ConfigParser import SafeConfigParser
from ansibleWrap import ansibleWrap
from OpenStackClient import OpenStackClient
import argparse
import sys

class instanceInfo():
    #Various information about the instance in question
    def __init__(self):
        self.instance_id = ''
        self.hypervisor = ''
        self.name = ''
        self.ip_address = ''
        self.portID = ''
        self.tenant_id = ''
        self.tenant_name = ''


def userInput(instanceInfoList):
    '''This function is used to determine what instances the user wants to span traffic for: (format: instance1,instance2,instance3)'''
    #You left off here. You to need to create a loop
    for val in instanceInfoList:
        print val.name

    #Grabbing user input, determing what instances they would like to span traffic for.
    var = raw_input("What instances would you like to span traffic for (format: instance1,instance2,instance3): ")

    #Grabbing command line arguements
    arguements = var.split(',')

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

    #Mirroring traffic from a specific vlan. I am also seeing problems seeing inbound traffic from
    #patch port
    #ovs-vsctl -- --id=@gre0 get Port gre0 -- --id=@m create mirror name=m0 select-all=true select-vlan=1 output-port=@gre0 -- set bridge br-int mirrors=@m

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

    #Creating nova object that will be used to interact with nova apis
    nova = osc.connect_nova()

    #Creating keystone object that will be used to interact with the keystone apis
    keystone = osc.connect_keystone()

    #Creating neutron object that will be used to interact with the neutron apis.
    neutron = osc.connect_neutron()

    #Creating empty dictionary that will hold the tenant_id to name mapping
    tenantDictionary = {}    

    #The below list is very important it is going to hold a list of instanceInfo objects that will correspond to each instance
    #for a specific tenant
    instanceInfoList = []


    #Creating dictionary holding keystone tenant id and keystone tenant name.
    for val in keystone.tenants.list():
        #Filling dicionary
        tenantDictionary[val.id] = val.name

        #Determining the uuid of the Garrett tenant. We will need this later, this tenat will also be
        #used as input from the user later
        if tenantDictionary[val.id] == args.tenant:
            tenant_id = val.id

    #At this point tenant dictionary is in the following structure.
    #{u'1ea14d05bde4429699a126d94db50f24': u'Garrett', u'802b76b2a8c948229e7df494f8aba6be': u'demo', 
    #u'495d777cb9434583bfee374c4ec802b6': u'services', u'4b1e5af067414a6390b20661bb6ddc46': u'admin'}

    
    #This outter for loop is grabbing information associated with each hypervisor. 
    #the variable 'h' in this loop is an object representing each hypervisor
    for h in nova.hypervisors.list():

        #Putting the below in a try catch, just in the event there is something strange with the compute services, and
        #values are returned.
        try:
            #Creating list of what instances are on the hypervisor in question
            instances = nova.hypervisors.search(h.hypervisor_hostname,True)[0].servers

            #The above instances list will be in the following format
            #[{u'uuid': u'62b7cd6b-3e19-473f-b1aa-16f747161353', u'name': u'instance-0000004d'}, 
            #{u'uuid': u'9a6f60ff-ca3e-43ab-9224-faae0d2e6f4b', u'name': u'instance-0000004e'}]

            #For loop to look at each instance on the hypervisor and determine if it is in the tenant in question
            for instance in instances:

                #Creating instance info object. This object is simply an easy way for me to keep track
                #of various useful pieces of information about an instance. 
                vm_attributes = instanceInfo()

                #If the tenant_id associated with an instance matches the original tenant_id the user submitted, a dictionary will be filled.
                if nova.servers.get(instance['uuid']).tenant_id == tenant_id:

                    #At this point we can be begin to fill the vm_attributes object.
                    vm_attributes.instance_id = nova.servers.get(instance['uuid']).id
                    vm_attributes.hypervisor = h.hypervisor_hostname
                    vm_attributes.name = nova.servers.get(instance['uuid']).name
                    vm_attributes.tenant_id = nova.servers.get(instance['uuid']).tenant_id
                    vm_attributes.tenant_name = args.tenant

                    #Setting the ip address attribute associated with the vm.
                    vm_attributes.ip_address = nova.servers.get(instance['uuid']).networks.values()[0][0]

                    #The for loop below ultimately grabs the port_id associated with the instance, you can't get this
                    #from nova
                    for val in neutron.list_ports()['ports']:
                        if val['fixed_ips'][0]['ip_address'] == nova.servers.get(instance['uuid']).networks.values()[0][0]:
                            #Creating the whole qvo port string. This is the holy grail. Because
                            #with this we know what port id on br-int is associated with what instance.
                            portID = 'qvo'+val['id'][0:11]

                            #Filling port id attribute
                            vm_attributes.portID = portID
    
            #Appending vm_attributes object to the instanceInfoList
            instanceInfoList.append(vm_attributes)

        except:
            pass

    #Ask user what instances they would like to span traffic for
    userInput(instanceInfoList)
