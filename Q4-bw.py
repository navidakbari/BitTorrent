
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class TwoHostMultiSwitch( Topo ):
    def build( self, bandWidth = 1 ):
	n = 2
	host1 = self.addHost('host1')
	host2 = self.addHost('host2')
	switch = []
	
	for i in range(n):
	    switch.append( self.addSwitch( 'switch%s'%(i+1)) )
	
	for i in range(n-1):
	    self.addLink( switch[i], switch[i+1], bw = bandWidth  )
	self.addLink(host1 , switch[0] , bw = bandWidth)
	self.addLink(host2 , switch[-1] , bw = bandWidth)

topos  = {'mytopo' : TwoHostMultiSwitch}





