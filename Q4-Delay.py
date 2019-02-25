from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class TwoHostMultiSwitch( Topo ):
    def build( self, n=2 ):
	d = '90ms'
	host1 = self.addHost('host1')
	host2 = self.addHost('host2')
	switch = []
	
	for i in range(n):
	    switch.append( self.addSwitch( 'switch%s'%(i+1)) )
	
	for i in range(n-1):
	    self.addLink( switch[i], switch[i+1] , delay = d)
	self.addLink(host1 , switch[0] , delay = d)
	self.addLink(host2 , switch[-1], delay = d)

topos  = {'mytopo' : TwoHostMultiSwitch}
