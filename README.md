# BigDataProjects
American Heritage School - Class of 2023 - Computer Science Track - Big Data Projects

## Hardware Setup - Physical
- 5 OrangePi PC's
- 5 Power adapters (5V 2amps for each OrangePI)
- 5 Ethernet Cables
- 1 Ethernet Switch
- 1 Ethernet switch power cord
- 1 USB wifi adapter

## Hardware Setup - Non-physical
- Wifi on one node, with the other 4 nodes using the wifi node as a gateway
- Enabling iptables and forwarding all packets 
- Firewall to enable ports 3000, 9701, 3100, 9700, 9090, and 9100
- Prometheus, NodeExporter, and Grafana to visualize performance 
- NFS server that allows file sharing between the nodes

## main.py Project
First test project that was run on the master node. Inefficient sorting algorithm.

## Feb8.py Project
Introduction to the python multiprocessing library. Processes are created and their jobs are to simply print out a statement and an iterator.
Later repurposed to clear extraneous files for a streamlined workflow for future projects.

## Project1.py 
First official project using the python multiprocessing library that used an inefficient sorting algorithm to sort 1 million integers.

## Project2.py
Second official project using the python dispy library to utilize the worker nodes to conduct the sorting

## Project3.py
Third and final official project using the python dispy library to sort 100 million integers. 

## timer.py
A custom timer class to track how long a program is run

## testing.py
A python program designed to simulate one node performing one job from Project3

## test.py
A python program that was created between Projects 2 and 3 to have a worker node sort and merge instead of just conducting the sorting
for increased speed.

## mergetest.py
A custom python program intending to merge two files of sorted integers together. Unfortunately, unfinished.
