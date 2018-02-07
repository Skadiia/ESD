#!/usr/bin/env python
#__*__coding:utf-8__*__

"""

Author : Skadiia
Description : ARP poisonning GUI tool
Usage : python ARP_Spoof.py 

"""

import sys
from src import spoof, ui, parser

def help_msg():

def main():
	target, interface, gateway = parser.parsing()

	spoof.Spoof(gateway, target)


if __name__ == '__main__':
	main()