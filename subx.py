# 
# 

###################################################
#                                                 #
#              prooject by MetiSec                #
#              Veeersion: 1.0                     #
#              Github: MetiSec                    #
#                                                 #
###################################################
# import package's
#
# 
import os
import requests
import json
import pyfiglet
import argparse
import pyfiglet

#  Create domain input
domain = input()

#  create argument 
parser = argparse.ArgumentParser(prog="subx", description="Subdomain enumeration tool")
# parser.add_argument("domain", action="store_true", help="Put domain form user")
parser.add_argument("-c", "--crt", dest="crt", action="store_true", help="Subdomain enumeration with call crt.sh.")
parser.add_argument("-d", "--dynamic", dest="dynamic", action="store_true", help="Subdomain enumeration with dynamic DNS brute force.")
parser.add_argument("-st", "--static", dest="static", action="store_true", help="Subdomain enumeartion with static DNS brute force")
parser.add_argument("-all", "--all-sub", dest="allsub", action="store_true", help="Full automate subdomain enumeration.")
parser.add_argument("-ip", dest="ip", action="store_true", help="find all ip of subdomain's.")
parser.add_argument("-sf", "--subf", dest="subf", action="store_true", help="Use public tools for subdomain enumeration")
parser.add_argument("-s", "--silent", dest="silent", action="store_true", help="Silent mode program")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode program")
parser.add_argument("-wm", "--wordlist-maker", dest="wordlistmaker", action="store_true", help="Small wordlist maker.")
parser.add_argument("-V", "--version", dest="version", action="store_true", help="Program version.")


args = parser.parse_args()
version = args.version
crt = args.crt
dynamic = args.dynamic
static = args.static
allsub = args.allsub
ip = args.ip
silent = args.silent
verbose = args.verbose
wrdlistmaker = args.wordlistmaker
subf = args.subf


# Create Function's 
def banner():
    # create Subx figlet
    bnr = pyfiglet.figlet_format("Subx")
    print(bnr)

def crtc():
    # Subdomain enumeration with call crt.sh provider
    crt_Call = os.system(f"echo {domain} | bash main.sh crt")
    print(crt_Call)

def show_Version():
    banner()
    print("Automation subdomain enumeration tool")
    print("Project by MetiSec              [Version: 1.0]")

def dynamic_DNS_brute():
    dnb = os.system(f"echo {domain} | bash main.sh dynamic")
    print(dnb)

def static_DNS_brute():
    snb = os.system(f"echo {domain} | bash main.sh static")
    print(snb)

def subf_Call():
    subfc = os.system(f"echo {domain} | bash main.sh subf")
    print(subfc)

def allsub_Call():
    allsubc = os.system(f"echo {domain} | bash main.sh allsub")
    print(allsubc)

def findIP():
    find_Ip = os.system(f"echo {domain} | bash main.sh findip")
    print(find_Ip)

def wordlist_Maker():
    command = os.system(f"echo {domain} | bash main.sh wmaker")
    print(command)

if version:
    show_Version()

if crt and silent:
    crtc()
elif crt and silent:
    banner()
    crtc()
elif crt and verbose:
    banner()
    print("Run program for calling CRT.SH provider")
    print("")


if dynamic and silent:
    dynamic_DNS_brute()
elif dynamic:
    banner()
    dynamic_DNS_brute()
elif dynamic and verbose:
    banner()
    print("Start dynamic DNS brute force")
    dynamic_DNS_brute()
    print("")
    print("done")
    
if static and silent:
    static_DNS_brute()
elif static:
    banner()
    static_DNS_brute()
elif static and verbose:
    banner()
    print(f"your domain: {domain}")
    print("Run static DNS brute force")
    static_DNS_brute()
    print("")
    print("DONE")

if allsub and silent():
    allsub_Call()
elif allsub:
    banner()
    allsub_Call()
elif allsub and verbose():
    banner()
    print(f"Domain: {domain}")
    print("Run full automate subdomain enumeration")
    allsub_Call()
    print("")
    print("DONE")


if subf and silent:
    subf_Call()
elif subf:
    banner()
    subf_Call()
elif subf and verbose:
    banner()
    print(f"Domain: {domain}")
    print("Run simple subdmoain enumeration")
    print("")
    subf_Call()
    print("")
    print("DONE")

if ip and silent:
    findIP()
elif ip:
    banner()
    findIP()
elif ip and verbose:
    banner()
    print("")
    print(f"Domain:  {domain}")
    print("")
    findIP()
    print("")
    print("DONE")

if wrdlistmaker and silent:
    wordlist_Maker()
elif wrdlistmaker:
    banner()
    wordlist_Maker()
elif wrdlistmaker and verbose:
    banner()
    print("")
    print(f"Domain:  {domain}")
    print("")
    wordlist_Maker()
    print("")
    print("DONE")