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
import argparse
import os
import pyfiglet

# Create argument
parser = argparse.ArgumentParser(prog="subx", description="Subdomain enumeration tool")
parser.add_argument("-d", dest="domain", help="Domain to find subdomains")
parser.add_argument("-l", "-list", dest="list", help="file containing a list of domains for subdomain discovery")
parser.add_argument("-dy", "--dynamic", dest="dynamic", action="store_true", help="Subdomain enumeration with dynamic DNS brute force.")
parser.add_argument("-st", "--static", dest="static", action="store_true", help="Subdomain enumeration with static DNS brute force")
parser.add_argument("-ss",dest="simplesub", action="store_true", help="Use the public subdomain enumeration tool")
parser.add_argument("-all", "--all-sub", dest="allsub", action="store_true", help="Full automated subdomain enumeration.")
parser.add_argument("-ip", dest="ipfinder", action="store_true", help="find all IP of subdomains.")
parser.add_argument("-r", dest="resolver", help="resolver file for DNS brute force")
parser.add_argument("-w", dest="wordlist", help="Wordlist file for DNS brute force")
parser.add_argument("-silent", dest="silent", action="store_true", help="shows only subdomains in the output")
parser.add_argument("-V", "-version", action="version", version="Subx version:  2.0")
args = parser.parse_args()

# Create namespace argument
domain = args.domain
list = args.list
dynamic = args.dynamic
static = args.static
simplesub = args.simplesub
allsub = args.allsub
ipfinder = args.ipfinder
resolver = args.resolver
wordlist = args.wordlist
silent = args.silent

# Create function's

def banner():
    # create Subx figlet
    bnr = pyfiglet.figlet_format("Subx")
    print(bnr)


def dynamic_DNS_brute():
    # Dynamic DNS brute force with single domain
    os.system("mkdir tmp")
    os.system(f'echo {domain} | subfinder -silent | rev | cut -d "." -f3 | rev | sort -u > tmp/dynamicDNS.txt')
    os.system(f'echo {domain} | shuffledns -w tmp/dynamicDNS.txt -r {resolver} -silent')
    os.system("rm -rf tmp")

def dynamic_DNS_brute_list():
    # Dynamic DNS brute force with list domain
    os.system("mkdir tmp")
    os.system(f'cat {list} | subfinder -silent | rev | cut -d "." -f3 | rev | sort -u > tmp/dynamicDNS.txt')
    os.system(f'cat {list} | shuffledns -w tmp/dynamicDNS.txt -r {resolver} -silent')
    os.system("rm -rf tmp")

def static_DNS_brue():
    # Static DNS brute force with single domain
    os.system("mkdir tmp")
    os.system(f'echo {domain} | shuffledns -w {wordlist} -r {resolver} -silent')
    os.system("rm -rf tmp")

def static_DNS_brue_list():
    # Static DNS brute with list domain
    os.system("mkdir tmp")
    os.system(f'cat {list} | shuffledns -w {wordlist} -r {resolver} -silent')
    os.system("rm -rf tmp")

def simpleSub():
    # Simple Subdomain enumeration with subfinder and assetfinder with single domain
    os.system("mkdir tmp")
    os.system(f"echo {domain} | subfinder -silent > tmp/simplesub.txt")
    os.system(f"echo {domain} | assetfinder >> tmp/simplesub.txt")
    os.system("cat tmp/simplesub.txt | sort -u")
    os.system("rm -rf tmp")

def simpleSub_list():
    # Simple Subdomain enumeration with subfinder and assetfinder with list domain
    os.system("mkdir tmp")
    os.system(f"cat {list} | subfinder -silent > tmp/simplesub.txt")
    os.system(f"cat {list} | assetfinder >> tmp/simplesub.txt")
    os.system("cat tmp/simplesub.txt | sort -u")
    os.system("rm -rf tmp")

def allSubf():
    # Full automate subdomain discovery with single domain
    os.system("mkdir tmp")
    os.system(f"echo {domain} | subfinder -silent > tmp/simplesub.txt")
    os.system(f"echo {domain} | assetfinder >> tmp/simplesub.txt")
    os.system(f'echo {domain} | subfinder -silent | rev | cut -d "." -f3 | rev | sort -u > tmp/dynamicword.txt')
    os.system(f'echo {domain} | shuffledns -w tmp/dynamicword.txt -r {resolver} -silent > tmp/dynamicDNS.txt')
    os.system(f'echo {domain} | shuffledns -w {wordlist} -r {resolver} -silent > tmp/staticDNS.txt')
    os.system("cat tmp/dynamicword.txt tmp/dynamicDNS.txt tmp/staticDNS.txt | sort -u > final.txt")
    os.system("cat final.txt")
    os.system("rm -rf tmp")

def allSubf_list():
    # Full automate subdomain discovery with list domain
    os.system("mkdir tmp")
    os.system(f"cat {list} | subfinder -silent > tmp/simplesub.txt")
    os.system(f"cat {list} | assetfinder >> tmp/simplesub.txt")
    os.system(f'cat {list} | subfinder -silent | rev | cut -d "." -f3 | rev | sort -u > tmp/dynamicword.txt')
    os.system(f'cat {list} | shuffledns -w tmp/dynamicword.txt -r {resolver} -silent > tmp/dynamicDNS.txt')
    os.system(f'cat {list} | shuffledns -w {wordlist} -r {resolver} -silent > tmp/staticDNS.txt')
    os.system("cat tmp/dynamicword.txt tmp/dynamicDNS.txt tmp/staticDNS.txt | sort -u > final.txt")
    os.system("cat final.txt")
    os.system("rm -rf tmp")

def ipfinderf():
    # Find IP from subfinder output with single domain
    os.system(f"echo {domain} | subfinder -silent | dnsx -a -ro -silent | sort -u")

def ipfinderf_list():
    # Find IP from subfinder output with list domain
    os.system(f"cat {list} | subfinder -silent | dnsx -a -ro -silent sort -u")

if domain and simplesub and silent:
    # Silent mode [ Only show subdomain's]
    simpleSub()
elif domain and simplesub:
    banner()
    simpleSub()

if list and simplesub and silent:
    # Silent mode [ Only show subdomain's]
    simpleSub_list()
elif list and simplesub:
    banner()
    simpleSub()


if domain and dynamic and resolver and silent:
    # Silent mode [ Only show subdomain's]
    dynamic_DNS_brute()
elif domain and dynamic and resolver:
    banner()
    dynamic_DNS_brute()

if list and dynamic and resolver and silent:
    # Silent mode [ Only show subdomain's]
    dynamic_DNS_brute_list()
elif list and dynamic and resolver:
    banner()
    dynamic_DNS_brute_list()

if domain and static and wordlist and resolver and silent:
    # Silent mode [ Only show subdomain's]
    static_DNS_brue()
elif domain and static and wordlist and resolver:
    banner()
    static_DNS_brue()

if list and static and wordlist and resolver and silent:
    # Silent mode [ Only show subdomain's]
    static_DNS_brue_list()
elif list and static and wordlist and resolver:
    banner()
    static_DNS_brue_list()

if domain and allsub and wordlist and resolver and silent:
    # Silent mode [ Only show subdomain's]
    allSubf()
elif domain and allsub and wordlist and resolver:
    banner()
    allSubf()

if list and allsub and wordlist and resolver and silent:
    # Silent mode [ Only show subdomain's]
    allSubf_list()
elif list and allsub and wordlist and resolver:
    banner()
    allSubf_list()

if domain and ipfinder and silent:
    # Silent mode [ Only show subdomain's]
    ipfinderf()
elif domain and ipfinder:
    banner()
    ipfinderf()

if list and ipfinder and silent:
    # Silent mode [ Only show subdomain's]
    ipfinderf_list()
elif list and ipfinder:
    banner()
    ipfinderf_list()

# 
# 
# 
#        ____        _         
#       / ___| _   _| |____  __
#       \___ \| | | | '_ \ \/ /
#        ___) | |_| | |_) >  < 
#       |____/ \__,_|_.__/_/\_\
# 
# 
# 
