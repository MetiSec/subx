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
```

## Usage:

```bash
python3 subx.py -d [ DOMAIN ] { FLAG }
```

## Help:

```
usage: subx [-h] [-d DOMAIN] [-l LIST] [-dy] [-st] [-ss] [-all] [-ip] [-r RESOLVER] [-w WORDLIST] [-o OUTPUT] [-silent] [-V]

Subdomain enumeration tool

options:
  -h, --help           show this help message and exit
  -d DOMAIN            Domain to find subdomains
  -l LIST, -list LIST  file containing a list of domains for subdomain discovery
  -dy, --dynamic       Subdomain enumeration with dynamic DNS brute force.
  -st, --static        Subdomain enumeration with static DNS brute force
  -ss                  Use the public subdomain enumeration tool
  -all, --all-sub      Full automated subdomain enumeration.
  -ip                  find all IP of subdomains1.
  -r RESOLVER          resolver file for DNS brute force
  -w WORDLIST          Wordlist file for DNS brute force
  -silent              show only subdomains in the output
  -V, -version         show the program's version number and exit
```

## Run:

- Step 1:
    - Install python library
    
    ```
    pip install -r requirements.txt
    ```
    
- Step 2:
    - Before running subx, you should install some tools:
        
        
        | shuffledns | https://github.com/projectdiscovery/shuffledns |
        | --- | --- |
        | subfinder | https://github.com/projectdiscovery/subfinder |
        | assetfinder | https://github.com/tomnomnom/assetfinder |
        | dnsx | https://github.com/projectdiscovery/dnsx |
        | alterx | https://github.com/projectdiscovery/alterx |
- Step 3:
    
    ```bash
    echo "alias subx='pytho3 [ PROJCT PATH ]'" >> ~/.zshrc
    ```
    

## Example:

```bash
subx -d [ DOMAIN ] -all -w { wordlist } -r { resolver } -silent
```
