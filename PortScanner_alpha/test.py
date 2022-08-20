import socket
import sys
import subprocess

def getServiceName(port, proto):
    try:
        name = socket.getservbyport(int(port), proto)
    except:
        return None
    return name

UDP_IP = "localhost" #sys.argv[1]
StartPort = 1 # sys.argv[2]
Endport = 100 # sys.argv[3]

for RPORT in range(int(StartPort), int(Endport)):
    MESSAGE = "ping"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    if client == -1:
        print("udp socket creation failed")
        
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    if sock1 == -1:
        print("icmp socket creation failed")
        
    try:
        client.sendto(MESSAGE.encode('utf_8'), (UDP_IP, RPORT))
        sock1.settimeout(1)
        data, addr = sock1.recvfrom(1024)
    except socket.timeout:
        serv = getServiceName(RPORT, 'udp')
        if not serv:
            pass
        else:
            print('Port {}:      Open'.format(RPORT))
    except socket.error as sock_err:
            if (sock_err.errno == socket.errno.ECONNREFUSED):
                print(sock_err('Connection refused'))
            client.close()
            sock1.close()