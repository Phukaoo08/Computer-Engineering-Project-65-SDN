# Computer-Engineering-Project-65-SDN
CE Project 65 Performance Improvement Mechanism in Software-defined Network [Research]

Members :
1.Theerat Budtrakard Stu ID : 62010448
2.Phattaraphat Chaiamornvate Stu ID : 62010684

Advisor :
Assoc. Prof.Sakchai Thipchaksurat Advisor
Academic Year 2022

## Installation
1. Virtual Machine - Oracle VM Virtualbox https://www.virtualbox.org/wiki/Downloads
2. Mininet Emulator (Ubuntu LS v.20.04) https://github.com/mininet/mininet/releases/
3. Ryu Framework [installation w/ commands in VM]
4. Flow manager [installation w/ commands in VM]
5. D-IGT Traffic Generator [installation w/ commands in VM] - http://sdnopenflow.blogspot.com/2015/05/using-of-d-itg-traffic-generator-in.html
6. Python3 [installation w/ commands in VM] 
7. Anaconda for trainning Data https://www.anaconda.com/products/distribution

## Problems that we've met and fixed
###### 1. Installation package from internet
Since VM does not have network directly connected, so we must provide a network for it. By using *sudo dhclient eth1*, and then we checked network with *ifconfig*. Afterwards, we can ping google.com or 8.8.8.8 .

###### 2. Flowmanager display on port http.
The firefox angine cannot display switches or it gives bugs, we should use 'Chrome' or 'Edge' instead.

###### 3. Don't for get to install Ubuntu desktop!
we must have installed the gui for traffic monitor and network components. By using *sudo apt-get install ubuntu-desktop* .

###### 4. Mininet cannot run controller with a port.
cd in ryu directory and run this command to fix it or restart controller *PYTHONPATH=. ./bin/ryu-manager ryu/app/simple_switch.py*.

