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

## Steps - Running Mininet and Traffic generator
1. Start mininet topology via 
###### sudo mn --custom projectTopo2.py --topo mytopo --controller=remote,ip=192.168.56.101 --switch ovsk,stp=1,protocols=OpenFlow13 --mac --link tc,bw=10
2. In mininet, use *xterm c0* for open a controller terminal. Then change directory to ryu/ryu/app and type the command.(use ovsk switch and stp togerther for prevent loop)
###### ryu-manager simple_switch_stp_13.py
3. After that. use *pingall* command in mininet terminal to checking a broadcast storm packet.
4. As you can see, STP is doing their job. Now, CTRL+C in a controller terminal. and use this command in *ryu/ryu/app* directory.
###### ryu-manager simple_monitor_13.py

## SDN Components 
###### 1. Mininet Emulator v.2.3.0
###### 2. Ryu SDN Framework
###### 3. D-ITG Traffic Generator

## D-ITG Settup [Source - H1,H2,H3] [Destination - H4,H5,H6]
1. ./ITGSend -a "Dest ip" -u 250 1000 -T UDP -t 60000
2. .ITGRecv -l "File.log"

## Performance Evaluation
1. Throughput
2. Delay
3. Compacitance
4. Bi-Directional LSTM vs LSTM

