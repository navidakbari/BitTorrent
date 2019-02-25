from ping import Ping

numberOfClinet = 5


def main():
    while(True):
        
        p = Ping('10.0.0.2' , '10.0.0.1')
        packet_size , ip, ip_header, icmp_header , payLoad = p.do_receive()
        print "PayLoad is %s"%(payLoad)
        
        
if __name__ == "__main__":
    main()
