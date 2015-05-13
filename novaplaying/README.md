
###Overview

This script determines what hypervisors the vms for a specific tenant live on. It also figures out what qvo ports are associated
with the virtual machine(s) in question. Once the qvo ports are determined I am going to write functionality that can push ovs commands to 
the appropriate br-ints on the hypervisors. The ovs command will do things to the traffic flow associated with the specific virtual machine in 
question. ex)mirroing, qos, rspan, etc.

Usage example: python novaclie.py --auth_url http://192.168.1.220:5000/v2.0/ --username admin --password whatever --tenant admin

#Things to do

