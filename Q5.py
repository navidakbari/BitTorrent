from ping import ping
from ping import Ping
from random import randint
import commands

numberOfClinet = 5

def main():
    while(True):
		sourceIp = findRandomIp()
		destinationIp = findRandomIp()
		print "from %s to %s" % (sourceIp, destinationIp)
		Server = Ping(sourceIp , destination)
		Server.do_send()
        
def findRandomIp():
	ip = commands.getoutput('/sbin/ifconfig').split('\n')[1][27:28]
	ipFounded = False
	while not ipFounded :
		newIpToJoin = randint(1, numberOfClinet)
		newIpToJoin = "10.0.0." + str(numberOfClinet)
		ipFounded = True if newIpToJoin != ip
		
if __name__ == "__main__":
    main()
