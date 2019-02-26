import ping
from ping import Ping
from random import randint
import random
import commands
import time 
import socket
import sys
import threading 
import socket
import select


#               0               1                              2          3       4           5            
#Protocol : returnOrNot? ~ if return -> ip else -> data ~ numberOfData ~ size ~ toDelete ~ fileName 

numberOfClient = 5
protocolTag = '~'

def splitFile(fileName = 'test.txt'):
	f = open(fileName, 'rb')
	result = []
	try:
		byte = f.read(1)
		result.append(str(byte))
		while byte != "":
			byte = f.read(1)
			result.append(str(byte))
	finally:
		f.close()
	result = result[:-1]
	return result

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

def senderFunction(p):
	fileName = raw_input("file name: ")
	#split file
	fileData = splitFile(fileName)

	#send file
	i = 0
	length = 0
	if len(fileData) % 8 == 0 :
		length = len(fileData) / 8
	else:
		length = (len(fileData) / 8) + 1 
	while i < len(fileData):
		data = ''
		for j in range(i , i + 8):
			if j < len(fileData):
				data += fileData[j]
		payload = 'noReturn' + protocolTag + data + protocolTag + '%s'%(i/8) + protocolTag + str(length) + protocolTag  + '0' + protocolTag + fileName
		src, dst = getRandomSourceAndDestination()
		p.set_new_config( src,dst, payload)
		# print "sending %s"%(i/8)
		p.do_send()
		i = i + 8

def downloadFunction(p):
	fileName = raw_input("file name: ")
	ourIp = commands.getoutput('/sbin/ifconfig').split('\n')[1][20:28]
	msg = 'return~'+ ourIp +'~0~3~0~0~' + fileName
	src, dst = getRandomSourceAndDestination()
	p.set_new_config(src, dst, msg)
	p.do_send()

def main():
	p = Ping('0.0.0.0', '0.0.0.0')
	currentSocket = p.get_socket()
	buffer = []
	while(True):
		inputs, output, exception = select.select([currentSocket, sys.stdin] , [currentSocket], [])
		for i in inputs:
			if i == currentSocket :
				receiverFunction(p)
			elif i == sys.stdin :
				x = raw_input()
				buffer.append(x)
		if currentSocket in output :
			for i in range(len(buffer)):
				if buffer[i] == "upload":
					senderFunction(p)
				elif buffer[i] == "download":
					downloadFunction(p)
			buffer = []

		
	



	
        
def receiverFunction(p):
	returnHome = False
	returnIp = 0
	packet_size , src_ip, dest_ip, ip_header, icmp_header , payLoad = p.do_receive()
	if not packet_size == 0:
		payloadData = payLoad.split('~')
		if(payloadData[0] == 'return'): #If msg was return to home
			returnIp = payloadData[1]
			returnHome = True
		if(icmp_header['type'] == ping.ICMP_ECHOREPLY):
			print "PayLoad is %s"%(payLoad)
			if(payloadData[4] == '1'):
				print "***********Deleting"
			elif(returnHome):
				if(not payloadData[0] == 'return') :
					payloadData[4] = '1'
					payLoad = '~'.join(payloadData)
					print "************Sending to Home %s"%(returnIp)
					ourIp = commands.getoutput('/sbin/ifconfig').split('\n')[1][20:28];
					p.set_new_config(ourIp, returnIp, payLoad)
					# time.sleep(1)
					p.do_send()
			else : 
				sourceIp, destinationIp = getRandomSourceAndDestination()
				# print "random src is %s and dst is %s"%(sourceIp, destinationIp)
				p.set_new_config(sourceIp, destinationIp, payLoad)
				# time.sleep(1)
				p.do_send()
        

def getRandomSourceAndDestination():
        sourceIp = findRandomIp()
        destinationIp = findRandomIp()
        while destinationIp == sourceIp :
                destinationIp = findRandomIp()
        return sourceIp, destinationIp
	
if __name__ == "__main__":
    main()
