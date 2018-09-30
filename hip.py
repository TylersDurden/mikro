import os, sys,time
from scapy.all import *

class Bashkit:
    @staticmethod
    def lan_grab():
        print " Finding known Wifi network"
        os.system('ifconfig wlan0 up; /etc/init.d/networking restart')
        os.system('iwlist wlan0 scanning >> lan.txt')
        ssid = input("Look for the SSID that you know, and enter it's name: ")
        os.system('/usr/bin/wpa_passphrase ' + str(ssid) + input('Great. Now enter the password: '))
        os.system('rm lan.txt')

    @staticmethod
    def getfilecontents(path, fname):
        data = []
        if path != '':
            os.system('cat ' + path + '/' + fname)
            for line in open(path + '/' + fname, 'r').readlines():
                data.append(line)
        else:
            for line in open(fname, 'r'):
                data.append(line)
        return data

    @staticmethod
    def get_currentDirectory():
        os.system('pwd >> path.txt')
        d = Bashkit.getfilecontents('','path.txt').pop()
        return d

    @staticmethod
    def get_connected(devname):
        os.system('lsblk>>devs.txt')
        filesystems = Bashkit.getfilecontents('', 'devs.txt')
        for devicename in filesystems:
            if devname in devicename:
                print "[*] "+devname + ' is connected! [*]'
        os.system('rm devs.txt')

    @staticmethod
    def get_hostname():
        return Bashkit.getfilecontents('/etc/','hostname').pop()

    @staticmethod
    def getlocalhost(path):
        os.system('ifconfig wlan0 >> ipinfo.txt')
        iptext = open('ipinfo.txt','r')
        for line in iptext.read():
            try:
                print "IP: " + line.split("inet ")[1].split(" netmask")
                return line.split("inet ")[1].split(" netmask")
            except:
                pass

    @staticmethod
    def has_internet():
        isTrue = False
        
        return isTrue

class MetaFunc:

    @staticmethod
    def sniff_fine():
        print "Sniffing the LAN... Man."
        details = list()
        start = time.time()
        a = sniff(7)
        dt = time.time() - start
        print "---------------------SUMMARY--------------------"
        a.summary()
        print "------------------------------------------------"
        for packet in a:
            packet.display()
            details.append(packet)
        print "---------------------DETAILS---------------------"
        return a, details,dt


class S0CI4L:
    hostDetails = {}
    remotes = []

    def __init__(self, ip, hostname):
        self.hostDetails['ip'] = ip
        self.hostDetails['name'] = hostname

    def addRemote(self, remoteIP):
        self.remotes.append(remoteIP)

    @staticmethod
    def get_connected(devname):
        os.system('lsblk >> devs.txt')
        filesystems = Bashkit.getfilecontents('', 'devs.txt')
        for devicename in filesystems:
            if devname in devicename:
                print devname+' is connected!'
        os.system('rm devs.txt')


def goDeep(path):
    system = os.name
    osdetails = os.environ
    # print os.sysconf_names
    name = Bashkit.get_hostname().replace('\n','')
    ip = Bashkit.getlocalhost(path)
    if str(ip) == 'None':
        ip = '127.0.0.1'
    print "[*] hostname: " + str(name) + " / at " + str(ip) + " [*]"
    print "[*] System: "+system + " [*]"
    print "[*] Found " + str(len(osdetails)) + " OS details [*]"
    return name, system, osdetails, ip


def menu(args):
    print "|//|\\|------ ~<|MENU__OPTS|>~ ------|//|\\|"
    print "| [USB] Checks for connnected USB drives |"
    print "| with factory default names             |"
    print "| [-v] Verbose Print Out of system info  |"
    print "| [dank] indicates you want to perform   |\n" \
          "| some kind of sniffing                  |\n" \
          "| Some Arguments can be combined too ex: |\n" \
          "| -v dank will give you system & LAN info|"
    print "|//|\\|------ ~<|((HIP_PY))|>~ ------|//|\\|"

    if 'USB' in args:
        # Get the names of all connected filesystems and devices
        Bashkit.get_connected('FLASH DRIVE')
    if '-v' in args:  # This allow for a verbose printout
        # Get the local hostname
        current_dir = Bashkit.get_currentDirectory()
        print "[*] Current DIR - " + current_dir.replace('\n','')
        hostname, systype, osinfo, ip = goDeep(current_dir)
    if 'dank' in args:
        # Sniff local traffic
        lan_traffic, packets, dt = MetaFunc.sniff_fine()
        print "[*]"+str(len(packets)) + " packets captured in " + \
              str(dt) + " seconds"
    if 'talk' in args:
        S0CI4L(hostname, ip)


def usage():
    print ""
    print ""


def main():
    if len(sys.argv)>1:
        menu(sys.argv)
    else:
        usage()


if __name__ == '__main__':
    main()
