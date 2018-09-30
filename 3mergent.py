import sys, os, time, socket, threading
import numpy as np

''' Inline Colors '''
CEND   = '\33[0m'
CBOLD  = '\33[1m'
CITAL  = '\33[3m'
CWHBLK = '\33[7m'
CBLINK = '\33[5m'
CRED   = '\33[31m'
CPURP  = '\33[35m'
CGREEN = '\33[92m'
CBLUE  = '\33[34m'
CBROWN = '\33[46m'
CREDBG = '\33[41m'
CBLKBG = '\33[100m'


def swpdat(fname):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n',''))
    return data


def commando(cmd):
    os.system(cmd + '>> result.txt')
    echo = swpdat('result.txt')
    os.system('rm result.txt')
    return echo


class TCPServer:

    bind_port = 0
    ACK = 0

    def __init__(self, port):
        self.bind_port = port
        self.run()

    def run(self):
        bind_ip = '0.0.0.0'
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((bind_ip,self.bind_port))
        server.listen(5)
        print CBOLD+CGREEN+"SERVER RUNNING ON 127.0.0.1:"+str(self.bind_port)+CEND

        while True:
            client, addr  = server.accept()
            print CBLUE+CBOLD+"Connection Accepted From : %s:%d" %(addr[0],addr[1])
            client_handler = threading.Thread(target=self.handle_client,args=(client,))
            client_handler.start()

    def handle_client(self,client):
        # print what client has sent
        request = client.recv(1024)
        print CRED+CBOLD+"REQUEST: "+request+CEND
        # Send an acknowledgement
        client.send(str(self.ACK))
        client.close()


class Sender:

    bind_port = 0

    def __init__(self,port):
        self.bind_port = port
        remote_host = str(input('Enter the IP you want to connect to: '))
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((remote_host,self.bind_port))
        print ":: CONNECTION ACCEPTED ::"
        running = True
        while running:
            try:
                echo = self.run(sock)
                print CBOLD+CBLUE+CITAL+":: ECHO ::"+CEND
                for line in echo:
                    print "*| "+line.replace('\n','')
            except KeyboardInterrupt:
                running = False
        sock.close()

    def run(self,sock):
        print "Enter Command(s): "
        sock.send(str(input('')))
        ans = sock.recv(1024)
        return ans


def usage():
    print CBOLD+CRED+CITAL+"\tINCORRECT USAGE!"+CEND
    exit(0)

def main():
    if len(sys.argv)<2:
        usage()

    offline = False
    OS = os.name
    compname = commando('hostname').pop
    route_inet = commando('route -n')
    if len(route_inet) < 3:
        offline = True

    else:
        print "Detected Internet Connection "
        if sys.argv[1] == '-reciever':
            try:
                start = time.time()
                TCPServer(9999).run()
            except KeyboardInterrupt:
                dt = str(time.time() - start) + " s"
                print CBOLD + CITAL + CPURP + " SERVER KILLED [" + dt + "]" + CEND
        if sys.argv[1] == '-sender':
            try:
                start = time.time()
                Sender(9999)
            except KeyboardInterrupt:
                dt = time.time() - start
                print "Session Killed ["+str(dt)+'s]'



if __name__ == '__main__':
    main()
