from ping import ping
from ping import Ping

numberOfClinet = 5


def main():
    while(True):
        p = Ping('10.0.0.1' , '10.0.0.2')
        p.do_send()
        



if __name__ == "__main__":
    main()