read domain

crt_Call(){
    curl https://crt.sh/\?q\=${domain}\&output\=json | jq -r ".[].common_name" | sort -u
}

dynamic_DNS_brute(){
    create_wordlist=$(echo ${domain} | subfinder -silent | alterx -silent | rev | cut -d "." -f3 | rev | sort -u > dynamicw.txt)
    echo ${create_wordlist}
    echo ${domain} | shuffledns -w dynamicw.txt -r resolver.txt -silent
}

static_DNS_brute(){
    echo ${domain} | shuffledns -w static_wordlist.txt -r resolver.txt -silent
}

subf(){
    subfinder_Call=$(echo ${domain} | subfinder -all -silent)
    assetfinder_Call=$(echo ${domain} | assetfinder)
    echo "$subfinder_Call $assetfinder_Call" | sort -u
}

allsub(){
    subfinder_Call=$(echo ${domain} | subfinder -all -silent)
    assetfinder_Call=$(echo ${domain} | assetfinder)
    create_wordlist=$(echo ${domain} | subfinder -silent | alterx -silent | rev | cut -d "." -f3 | rev | sort -u > dynamicw.txt)
    echo ${create_wordlist}
    dynamic=$(echo {domain} | shuffledns -w dynamicw.txt -r resolver.txt -silent)
    static=$(echo ${domain} | shuffledns -w static_wordlist.txt -r resolver.txt -silent) 
    echo "$subfinder_Call $assetfinder_Call $dynamic $static" | sort -u 
}

findIP(){
    echo ${domain} | subfinder -all -silent | dnsx -a -ro -silent | sort -u
}

wordlist_Maker(){
    wmaker=$(echo ${domain} | subfinder -silent | alterx -silent | rev | cut -d "." -f3 | rev | sort -u)
}

if [[ $1 = "crt" ]]
then
    crt_Call
fi

if [[ $1 = "dynamic" ]]
then
    dynamic_DNS_brute
fi

if [[ $1 = "static" ]]
then 
    static_DNS_brute
fi

if [[ $1 = "subf" ]]
then 
    subf
fi

if [[ $1 = "allsub" ]]
then
    allsub
fi

if [[ $1 = "findip" ]]
then
    findIP
fi

if [[ $1 = "wmaker" ]]
then
    wordlist_Maker
fi