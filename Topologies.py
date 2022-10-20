from mininet.topo import Topo

class Fat( Topo ):

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1')
        h2 = self.addHost( 'h2')
        h3 = self.addHost( 'h3')
        h4 = self.addHost( 'h4')

        sw1 = self.addSwitch('sw1')
        sw2 = self.addSwitch('sw2')

        # Add links
        self.addLink(h1,sw1)
        self.addLink(sw1,h2)
        self.addLink(sw1,sw2)
        self.addLink(sw2,h3)
        self.addLink(sw2,h4)

topos = { 'mytopo': ( lambda: Fat() ) }


#------------------------------------------------------------------------------------#

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example "

    def build( self ):
        "Create custom topo."

        # Add hosts and sw
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        """bottomLeftHost = self.addHost( 'h3' )
        bottomRightHost = self.addHost( 'h4' )"""
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink*( rightSwitch, rightHost )
        """self.addLink( leftSwitch, bottomLeftHost )
        self.addLink( rightSwitch, bottomRightHost )"""

topos = { 'mytopo ': ( lambda: MyTopo() ) }


# Current testing !!

from mininet.topo import Topo
from mininet.node import Host, OVSKernelSwitch
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example "

    def build( self ):
        "Create custom topo."

        # Add hosts and sw
        firstHost = self.addHost( 'h1' )
        secondHost = self.addHost( 'h2' )
        thirdHost = self.addHost( 'h3' )
        fourthHost = self.addHost( 'h4' )
        firstSwitch = self.addSwitch( 's1' )
        secondSwitch = self.addSwitch( 's2' )
        thirdSwitch = self.addSwitch( 's3' )
        fourthSwitch = self.addSwitch( 's4' )
        fifthSwitch = self.addSwitch( 's5' )
        sixthSwitch = self.addSwitch( 's6' )
        topSwitch = self.addSwitch( 's7' )
        

        # Add links
        self.addLink( firstHost, firstSwitch, 1, 1 )
        self.addLink( firstSwitch, fifthSwitch , 2, 1)
        self.addLink( fifthSwitch, secondSwitch, 2, 1 )
        self.addLink( secondSwitch, secondHost, 2, 1)
        self.addLink( fifthSwitch, topSwitch, 3, 1)
        self.addLink( topSwitch, sixthSwitch, 2, 1)
        self.addLink( sixthSwitch, fourthSwitch, 2, 1)
        self.addLink( sixthSwitch, thirdSwitch, 3, 1)
        self.addLink( thirdSwitch, thirdHost, 2, 1)
        self.addLink( fourthSwitch,fourthHost, 2, 1)

topos = { 'mytopo': ( lambda: MyTopo() ) }

# ---------------------------------------------------------- #

from mininet.topo import Topo
from mininet.node import Host, OVSKernelSwitch
from mininet.link import TCLink

class MyTopo( Topo ):
    "Clos Topo"

    def build( self ):
        "Create Topo from paper."

        # Adding Devices in Topology
        hostOne = self.addHost( 'h1' )
        hostTwo = self.addHost( 'h2' )
        hostThree = self.addHost( 'h3' )
        hostFour = self.addHost( 'h4' )
        hostFive = self.addHost( 'h5' )
        hostSix = self.addHost( 'h6' )
        hostSeven = self.addHost( 'h7' )
        hostEight = self.addHost( 'h8' )
        switchOne = self.addSwitch( 's1' )
        switchTwo = self.addSwitch( 's2' )
        switchThree = self.addSwitch( 's3' )
        switchFour = self.addSwitch( 's4' )
        switchFive = self.addSwitch( 's5' )
        switchSix = self.addSwitch( 's6' )
        switchSeven = self.addSwitch( 's7' )

        # Add links
        self.addLink( hostOne, switchOne, 1, 1 )
        self.addLink( hostTwo, switchOne, 1, 2 )
        self.addLink( hostThree, switchOne, 1, 3 )
        self.addLink( switchOne, switchFive, 4, 1 )
        self.addLink( switchOne, switchSix, 5, 1 )
        self.addLink( switchOne, switchSeven, 6, 1 )
        self.addLink( hostFour, switchTwo, 1, 1 )
        self.addLink( hostFive, switchTwo, 1, 2 )
        self.addLink( switchTwo, switchFive, 3, 2 )
        self.addLink( switchTwo, switchSix, 4, 2 )
        self.addLink( switchTwo, switchSeven, 5, 2 )
        self.addLink( hostSix, switchThree, 1, 1 )
        self.addLink( switchThree, switchFive, 2, 3 )
        self.addLink( switchThree, switchSix, 3, 3 )
        self.addLink( switchThree, switchSeven, 4, 3 )
        self.addLink( hostSeven, switchFour, 1, 1 )
        self.addLink( hostEight, switchFour, 1, 2 )
        self.addLink( switchFour, switchFive, 3, 4 )
        self.addLink( switchFour, switchSix, 4, 4 )
        self.addLink( switchFour, switchSeven, 5, 4)

topos = { 'mytopo': ( lambda: MyTopo() ) }

# ------------------------------------------------------------- #

from mininet.topo import Topo
from mininet.node import Host, OVSKernelSwitch
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example "

    def build( self ):
        "Create custom topo."

        # Add hosts and sw
        hostOne = self.addHost( 'h1' )
        hostTwo = self.addHost( 'h2' )
        hostThree = self.addHost( 'h3' )
        hostFour = self.addHost( 'h4' )
        hostFive = self.addHost( 'h5' )
        hostSix = self.addHost( 'h6' )
        switchOne = self.addSwitch( 's1' )
        switchTwo = self.addSwitch( 's2' )
        switchThree = self.addSwitch( 's3' )
        switchFour = self.addSwitch( 's4' )
        switchFive = self.addSwitch( 's5' )
        switchSix = self.addSwitch( 's6' )
        
        # Add links
        self.addLink( hostOne, switchOne, 1, 1)
        self.addLink( switchOne, switchTwo, 2, 2)
        self.addLink( switchOne, switchThree, 3, 3)
        self.addLink( switchThree, hostThree, 1, 1)
        self.addLink( switchTwo, hostTwo, 1, 1)
        self.addLink( switchTwo, switchThree, 3, 2)
        self.addLink( switchTwo, switchFive, 4, 4)
        self.addLink( switchThree, switchSix, 4, 4)
        self.addLink( switchSix, hostSix, 1, 1)
        self.addLink( switchFive, switchSix, 3, 2)
        self.addLink( switchFive, hostFive, 1, 1)
        self.addLink( switchFive, switchFour, 2, 2)
        self.addLink( switchFour, switchSix, 3, 3)
        self.addLink( switchFour, hostFour, 1, 1)
        

topos = { 'mytopo': ( lambda: MyTopo() ) }