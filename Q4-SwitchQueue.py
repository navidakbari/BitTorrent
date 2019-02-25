
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class TwoHostMultiSwitch( Topo ):
    def build( self, n=2 ):
	switchQueue = 15
        host1 = self.addHost('host1')
        host2 = self.addHost('host2')
        switch = []

        for i in range(n):
            switch.append( self.addSwitch( 'switch%s'%(i+1)) )

        for i in range(n-1):
            self.addLink( switch[i], switch[i+1] , max_queue_size = switchQueue , cls = TCLink)
        self.addLink(host1 , switch[0] , max_queue_size = switchQueue , cls = TCLink)
        self.addLink(host2 , switch[-1], max_queue_size = switchQueue , cls = TCLink)

topos  = {'mytopo' : TwoHostMultiSwitch}
