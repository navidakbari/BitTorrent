from ping import Ping
from Q5 import send
from Q5 import findRandomIp
import ping

numberOfClinet = 5


def main():
    p = Ping('0.0.0.0' , '0.0.0.0')
    while(True):
        
        
        packet_size , src_ip, dest_ip, ip_header, icmp_header , payLoad = p.do_receive()
        if not packet_size == 0:
                if(ip_header['type'] == ping.ICMP_ECHOREPLY):
                        print "src is %s and dst is %s"%(src_ip, dest_ip)
                        p = Ping(dest_ip, src_ip, payload = "mamad")
                else:
                        sourceIp = findRandomIp()
                        destinationIp = findRandomIp()
	                while destinationIp == sourceIp :
		                destinationIp = findRandomIp()
                        print "random src is %s and dst is %s"%(sourceIp, destinationIp)
                        p = Ping(sourceIp, destinationIp)
                p.do_send()
                        
        print "PayLoad is %s"%(payLoad)
        
        
if __name__ == "__main__":
    main()
