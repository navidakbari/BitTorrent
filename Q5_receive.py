import ping

numberOfClinet = 5


def main():
    while(True):
        
        p = Ping('10.0.0.2' , '10.0.0.1')
        temp = p.do_receive()
        print temp
        
        
if __name__ == "__main__":
    main()