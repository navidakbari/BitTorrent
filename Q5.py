import os
import select
import signal
import struct
import sys
import time
import socket,sys
from impacket import ImpactPacket
import ping
from ping import Ping

numberOfClinet = 5


def main():
    while(True):
        ping.ping('10.0.0.1' , '10.0.0.2')
        



if __name__ == "__main__":
    main()