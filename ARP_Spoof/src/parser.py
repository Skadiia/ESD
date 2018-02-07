#!/usr/bin/env python
# -.- coding: utf-8 -.-

import argparse
import sys  

    def parsing():
	    ''' Fonction that parse command line arguments '''
	    parser = ArgumentParser(description="ARP cache poisoning tool")
	    parser.add_argument("-i", "--interface",required=True,
	    										type=str,
	    										help="network interface to use")
	    parser.add_argument("-t", "--target",	required=True,
	    										type=str,
	    										help="@IP of target")
	   	parser.add_argument("-t", "--gateway",	required=True,
	    										type=str,
	    										help="@IP of gateway")
	    parser.add_argument('-v', '--version',
	                        					help='Display the program version',
	                        					action='version',
												version='Made by @Skadiia, arp_spoof version is 0.1.')
		args = parser.parse_args()

		return args.interface, args.target