# subx

![https://raw.githubusercontent.com/ImAyrix/ImAyrix/master/gitartwork.svg](https://raw.githubusercontent.com/ImAyrix/ImAyrix/master/gitartwork.svg)

## description:

subx is a tool for subdomain enumeration. subx utilize for automation in recon. 

```
 ____        _         
/ ___| _   _| |____  __
\___ \| | | | '_ \ \/ /
 ___) | |_| | |_) >  < 
|____/ \__,_|_.__/_/\_\
                       

Automation subdomain enumeration tool
Project by MetiSec              [Version: 1.0]
```

## Usage:

```bash
echo { DOMAIN } | python3 subx.py { FLAG }
```

## Help:

```
usage: subx [-h] [-c] [-d] [-st] [-all] [-ip] [-sf] [-s] [-v] [-wm] [-V]

Subdomain enumeration tool

options:
  -h, --help            show this help message and exit
  -c, --crt             Subdomain enumeration with call crt.sh.
  -d, --dynamic         Subdomain enumeration with dynamic DNS brute force.
  -st, --static         Subdomain enumeartion with static DNS brute force
  -all, --all-sub       Full automate subdomain enumeration.
  -ip                   find all ip of subdomain's.
  -sf, --subf           Use public tools for subdomain enumeration
  -s, --silent          Silent mode program
  -v, --verbose         Verbose mode program
  -wm, --wordlist-maker
                        Small wordlist maker.
  -V, --version         Program version.
```

## Run:

- Step 1:
    - Install python library
        
        ```
        pip install -r requirerment.txt
        ```
        
- Step 2:
- You should install these, tools on your PC or server
    
    ```
    subfinder
    assetfinder
    dnsx
    alterx
    shuffledns
    ```
