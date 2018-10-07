import sys, os, time, socket, numpy as np
from scapy.all import  *
CEND   = '\33[0m'
CBOLD  = '\33[1m'
CITAL  = '\33[3m'
CWHBLK = '\33[7m'
CBLINK = '\33[5m'
CRED   = '\33[31m'
CGREEN = '\33[92m'
CBLUE  = '\33[34m'
CBROWN = '\33[46m'
CREDBG = '\33[41m'
CBLKBG = '\33[100m'


def swptxt(fname):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n',''))
    return data


def local_machine():
    """
    Extract the local machines IP and MAC address for
    the ethernet and wireless network interfaces.
    :return:
    """
    os.system('ifconfig wlan0 >> wlan.txt')
    wlan = swptxt('wlan.txt')
    os.system('rm wlan.txt')
    os.system('ifconfig eth0 >> eth.txt')
    eth0 = swptxt('eth.txt')
    os.system('rm eth.txt')
    WLAN = {}
    ETH0 = {}
    haveIP = False
    print CBOLD + CBLKBG + "MACs: \t\t\t" + CEND + CBOLD + CWHBLK + " IP:" + CEND
    for line in wlan:
        try:
            WLAN['ip'] = line.split('inet ')[1].split('netmask')[0]
            wlip = str(WLAN['ip'])
            haveIP = True
        except IndexError:
            pass
        try:
            WLAN['mac'] = line.split('ether ')[1].split(' tx')[0]
            wlmac = str(WLAN['mac'])
            if not haveIP:
                print "WLAN " + CGREEN + wlmac + CEND
            else:
                print "WLAN " + CGREEN + wlmac + CEND+'\t'+\
                      CBLUE+CBOLD+str(WLAN['ip'])+CEND
        except IndexError:
            pass
    for ln in eth0:
        try:
            ETH0['ip'] = ln.split('inet ')[1].split('netmask')[0]
            print CBLUE+str(ETH0['ip'])+CEND
        except IndexError:
            pass
        try:
            ETH0['mac'] = ln.split('ether ')[1].split(' tx')[0]
            print "ETH0 " + CGREEN + str(ETH0['mac']) + CEND
        except IndexError:
            pass
    return WLAN, ETH0, haveIP


def surrounding():
    os.system('iwlist wlan0 scan >> near.txt')
    nearme = swptxt('near.txt')
    os.system('rm near.txt')
    APs = {}
    essids = []
    macs = []
    apN = 0
    for line in nearme:
        try:
            apN = line.split('Address: ')[0]
            mac = line.split('Address: ')[1]
            macs.append(mac)
        except IndexError:
            pass
        try:
            essid = line.split('ESSID:"')[1].replace('"', '')
            essids.append(essid)
            APs[macs.pop()] = essid
        except IndexError:
            pass
    print CITAL + CBOLD + "\t:: Access Points Identified ::" + CEND
    index = 0
    try:
        for ap in APs.keys():
            print CBOLD + APs[ap] + " "+CGREEN + ap + CEND
            index += 1
    except IndexError:
        pass
    print CBOLD+"*----------------------------------------------------------*"+CEND
    return APs


def usage():
    print CBOLD+CRED+"Incorrect Usage!"+CEND
    os.system('paplay bark.ogg')
    exit(0)


def packet_callback(packet):
    #print packet.show()
    DST = packet.dst
    SRC = packet.src
    data = packet.payload
    print CGREEN+CBOLD+"SRC "+CEND+CBOLD+str(SRC)+CEND
    print CRED+CBOLD+"DST "+CEND+CBOLD+str(DST)+CEND
    print CITAL+CBLUE+CBOLD+str(data)+CEND


def rogue_dhcp():
    print CBOLD+CITAL+"\t\t:: Rogue DHCP Server Check ::"+CEND
    conf.checkIPaddr = False
    fam,hw = get_if_raw_hwaddr(conf.iface)
    dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
    ans, unans = srp(dhcp_discover, multi=True)
    print ans.summary()
    print "*--------------------------------------------------------------------------*"
    return ans, unans


def main():
    if len(sys.argv) > 1:
        usage()
    else:
        ''' Get Info abt Local Machine & Nearby wifi signals '''
        wlan, eth,isNxd = local_machine()
        AccessPoints = surrounding()
        os.system('paplay complete.oga')

        # If you have a network connection, find the other machines on the LAN
        # and make sure you're connected to the correct DHCP server
        if isNxd:
            print CBOLD+CITAL+"\t\t\t:: ARPing the Lan ::"+CEND
            ans, unan = arping("192.168.1.*")
            lan_ppl = []
            for arp in range(len(ans)):
                lan_ppl.append(ans[arp][0].pdst)
            for host in lan_ppl:
                os.system('host '+host)
            print "*------------------------------------------------------------*"
            wpa_check, unans = rogue_dhcp()
            for p in wpa_check: print CRED+p[1][Ether].src, p[1][IP].src+CEND

    # Monitor Network Traffic. Assume No Trust.
    print CRED+CBOLD+CBLINK+"\t\t\tStarting Sniffer..."+CEND
    N = 0
    while N<10:
        sniff(prn=packet_callback, count=1)
        N += 1


if __name__ == '__main__':
    main()
