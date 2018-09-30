import sys, os, time, hashlib, socket
import scapy.all as scapy

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


def swpobj(fname):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n',''))
    return data


def nxidself():
    """
    Identify this machines Hostname and
    then the available local IPs and MAC
    addresses associated with them.
    :return nxinfo {}:
    """
    nxinfo = {}
    os.system('hostname >> name.txt')
    Name = swpobj('name.txt').pop()
    os.system('rm name.txt')
    if os.name != 'nt':
        os.system('ifconfig >> ipinfo.txt')
    else:
        os.system('ipconfig >> ipinfo.txt')
    # Now extract the import parts
    ipinfo = swpobj('ipinfo.txt')
    os.system('rm ipinfo.txt')
    IP = []
    MAC = []
    for line in ipinfo:
        try:
            MACs = line.split('ether ')[1].split(' ')[0]
            MAC.append(MACs)
        except IndexError:
            pass
        try:
            IPs = line.split('inet ')[1].split(' netmask')[0]
            IP.append(IPs)
        except IndexError:
            pass
    nxinfo['ip'] = IP
    nxinfo['mac'] = MAC
    nxinfo['name'] = Name
    return nxinfo


def show_machine(machina):
    ipinfo = machina['ip']
    macadr = machina['mac']
    hname = machina['name']

    print CBOLD+"Name:\t\t"+CEND+CBOLD+CPURP+hname+CEND
    print CBOLD+"IP\t\tMAC_ADDRESS"+CEND
    if len(ipinfo) == len(macadr):
        for i in range(len(ipinfo)):
            print CREDBG+CBOLD+ipinfo.pop()+"\t"+macadr.pop()+CEND


def beacon_sniff():
    os.system('paplay /usr/share/sounds/sound-icons/at')
    # Scan the wireless channels available and grab the raw data
    os.system('iwlist wlan0 scan >> neighborhood.txt')
    nxlandscape = swpobj('neighborhood.txt')
    iface = 0
    BEACONS = {}
    # Beacon Features
    macs = []
    essid = []
    channel = []
    lastpkt = []
    ciphers = []
    # Extract the useful information from wireless scan
    for line in nxlandscape:
        content = line.replace('\n','')
        # MACs
        try:
            # print content.split('Address: ')[1]
            macs.append(content.split('Address: ')[1])
        except IndexError:
            pass
        # ESSID
        try:
            # print content.split('ESSID:')[1]
            essid.append(content.split('ESSID:')[1])
        except IndexError:
            pass
        # Channel/Frequency
        try:
            # print content.split('Frequency:')[1]
            channel.append(content.split('Frequency:')[1])
        except IndexError:
            pass
        # Last Beacon
        try:
            # print content.split('Last beacon: ')[1]
            lastpkt.append(content.split('Last beacon: ')[1])
        except IndexError:
            pass
        # Cipher Suite
        try:
            ciphers.append(content.split('IEEE ')[1])
        except IndexError:
            pass
        # Increment Network Object
        try:
            if content.__contains__('Cell '):
                iface += 1
        except IndexError:
            pass
    BEACONS['mac'] = macs
    BEACONS['essid'] = essid
    BEACONS['channel'] = channel
    BEACONS['crypto'] = ciphers
    print CBOLD+"\t\tFINISHED SCAN "+CEND
    return BEACONS


def local_map(local):
    # Check out the visible network beacons
    beacons = beacon_sniff()
    # Display info about beacons found
    print CITAL+str(len(beacons['mac']))+" Wireless Access Points Identified"+CEND
    if len(beacons['mac']) > 0:
        os.system('paplay /lib/live/mount/rootfs/filesystem.squashfs/usr/share/'
                  'metasploit-framework/data/sounds/default/wonderful.wav')
        print CBOLD + CGREEN + "MAC\t\tESSID\t\tCHANNEL/FREQUENCY" + CEND
        if len(beacons['mac']) == len(beacons['essid']) == len(beacons['channel']):
            for i in range(len(beacons['mac'])):
                print CBOLD + CRED + beacons['mac'].pop() + "\t" + CEND + \
                      CBOLD + CBLUE + beacons['essid'].pop() + "\t" + CEND + \
                      CBOLD + CPURP + beacons['channel'].pop() + "\t" + CEND
    os.system('rm neighborhood.txt')

    # Move on to identifying hosts in Local Network
    live_hosts = []
    # Ping any hosts connected to the same subnet
    os.system('./hellolan.sh >> hosts.txt')
    possible_neighbors = swpobj('hosts.txt')
    os.system('rm hosts.txt')
    print "\t\t"+CBOLD+CITAL+"FINDING LIVE HOSTS ON LAN"+CEND
    for line in possible_neighbors:
        try:
            live_hosts.append(line.split(' domain name pointer ')[1])
        except IndexError:
            pass
    for host in live_hosts:
        print CBOLD+"Found Live Host: " + CWHBLK + host + CEND
    os.system('paplay /lib/live/mount/rootfs/filesystem.squashfs/usr/share/'
              'metasploit-framework/data/sounds/default/excellent.wav')
    try:
        ans = scapy.arping("192.168.1.*")
        print ans
    except:
        pass
    return live_hosts, beacons


def done():
    print  CITAL+CBOLD+CGREEN+"\t\tFINISHED"+CEND
    os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')


def run_active():
    # Define this machines identify in network
    localMachine = nxidself()

    # Display the basic network info found
    show_machine(localMachine)

    # Try mapping local network hosts
    liveHosts, AccessPoints = local_map(localMachine)
    done()


def main():
    if len(sys.argv) > 1:
        argfound = False
        # Run Active Network Monitoring
        if sys.argv[1] == 'active':
            argfound = True
            run_active()
        # Argument is not recognized
        if not argfound:
            usage()

    else:
        usage()


def usage():
    print CBOLD + CITAL + "INCORRECT USAGE!" + CEND
    try:
        os.system('paplay /usr/local/lib/python2.7/dist-packages/pygame/examples/data/punch.wav')
    except:
        pass


if __name__ == '__main__':
    main()