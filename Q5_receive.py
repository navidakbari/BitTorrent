from ping import Ping
from Q5 import send
from Q5 import findRandomIp
import ping
import time
import commands

numberOfClinet = 5
#               0               1               2               3          4       5           6            7
#Protocol : returnOrNot? ~ if return -> ip else -> data ~ numberOfData ~ size ~ toDelete ~ fileName ~ returnFileName 
def main():
    p = Ping('0.0.0.0' , '0.0.0.0', payload="test")
    returnHome = False
    returnIp = 0
    while(True):
        packet_size , src_ip, dest_ip, ip_header, icmp_header , payLoad = p.do_receive()
        if not packet_size == 0:
                payloadData = payLoad.split('~')
                if(payloadData[0] == 'return'): #If msg was return to home
                        returnIp = payloadData[1]
                        returnHome = True
                if(icmp_header['type'] == ping.ICMP_ECHOREPLY):
                        print "PayLoad is %s"%(payLoad)
                        if(payloadData[5] == '1'):
                                print "***********Deleting"
                        elif(returnHome and not payloadData[0] == 'return'):
                                payloadData[5] = '1'
                                payLoad = '~'.join(payloadData)
                                print "************Sending to Home %s"%(returnIp)
                                ourIp = commands.getoutput('/sbin/ifconfig').split('\n')[1][20:28];
                                p.set_new_config(ourIp, returnIp, payLoad)
                                # time.sleep(1)
                                p.do_send()
                        else : 
                                sourceIp, destinationIp = getRandomSourceAndIp()
                                print "random src is %s and dst is %s"%(sourceIp, destinationIp)
                                p.set_new_config(sourceIp, destinationIp, payLoad)
                                # time.sleep(1)
                                p.do_send()
        
        
def getRandomSourceAndIp():
        sourceIp = findRandomIp()
        destinationIp = findRandomIp()
        while destinationIp == sourceIp :
                destinationIp = findRandomIp()
        return sourceIp, destinationIp
if __name__ == "__main__":
    main()
