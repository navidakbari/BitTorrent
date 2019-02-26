from ping import ping
from ping import Ping
from random import randint
import random
import commands
import time 
import socket
numberOfClient = 5

def main():
#     while(True):
# 	    send()
	
	while(True):
		x = input ('what?')
		if(x == 1):
			Server = Ping('10.0.0.1' , '10.0.0.5', payload= 'no~far~0~3~0~0')
			Server.do_send() 
		else : 
			Server = Ping('10.0.0.2' , '10.0.0.5', payload= 'return~10.0.0.6~0~3~0~0')
			Server.do_send() 
			while(True):
				packet_size , src_ip, dest_ip, ip_header, icmp_header , payLoad = Server.do_receive()
				print payLoad
def send():
	sourceIp = findRandomIp()
	destinationIp = findRandomIp()
	while destinationIp == sourceIp:
		 destinationIp = findRandomIp()
	print "from %s to %s" % (sourceIp, destinationIp)
        Server = Ping(sourceIp , destinationIp)
        Server.do_send() 
def findRandomIp():   
	hostname = socket.gethostname()    
	#ip = socket.gethostbyname(hostname)
	#print ip  
	ip = commands.getoutput('/sbin/ifconfig').split('\n')[1][20:28]
	ipFounded = False
	newIpToJoin = ""
	while not ipFounded :
		newIpToJoin = randint(1, numberOfClient)
		newIpToJoin = "10.0.0." + str(newIpToJoin)
		if not newIpToJoin == ip:
			ipFounded = True

	return newIpToJoin
		
if __name__ == "__main__":
    main()
