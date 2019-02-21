from mininet.topo import Topo

class MyTopo( Topo ):
    def build( self ):

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )

        # Add links and set their delay
        self.addLink( host1, switch1 , delay = '20ms')
        self.addLink( host2, switch1 , delay = '20ms')
        self.addLink( switch1, switch2 , delay = '50ms')
        self.addLink( host3, switch2 , delay = '15ms')
        self.addLink( host4, switch2, delay = '1s')


topos = {'mytopo' : MyTopo}
        