from namecheap import Api
from urllib2 import urlopen
import itertools
from string import ascii_lowercase
import json
import argparse
import time

import configs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tld', type=str, help="TLD")
    parser.add_argument('length', type=int, help="length of sub domain")
    args = parser.parse_args()
    seek(args.tld, args.length)


def seek(tld, length):
    domains = get_all_domain_name(tld, length)
    domains_per_query = 50
    for i in xrange(0, len(domains) - 1, domains_per_query):
        domains_query_end_range = min(i+domains_per_query, len(domains))
        print('Checking domain in range %s-%s/%s' % (i, domains_query_end_range, len(domains)))
        partly_result = check_availability(domains[i:domains_query_end_range])
        with open('result.json', 'a') as result_file:
            json.dump(partly_result, result_file, indent=4)

def check_availability(domains, retry_count=0):
    if(retry_count > 5): 
        return {}
    print('Try %s' % (retry_count + 1))
    client_ip = get_current_machine_public_ip()
    api = Api(configs.username, configs.api_key, configs.username, client_ip,
              sandbox=False, debug=False)
    try:
        result = api.domains_check(domains)
    except Exception as error:
        print(error)
        time.sleep(10)
        result = check_availability(domains, retry_count + 1)
    return result

def get_current_machine_public_ip():
    return urlopen('http://ip.42.pl/raw').read()

def get_all_domain_name(tld, length):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9']
    domains = [''.join(i) + '.' + tld for i in itertools.product(alphabets, repeat = length)]
    return domains


if __name__ == '__main__':
    main()










    # A list of TLDs that shorter thant 4 characters
    # "bar"
    # "bid"
    # "bio"
    # "biz"
    # "bz"
    # "ca"
    # "cab"
    # "cam"
    # "car"
    # "cc"
    # "ceo"
    # "ch"
    # "cm"
    # "cn"
    # "co"
    # "com"
    # "de"
    # "dog"
    # "eco"
    # "es"
    # "eu"
    # "fit"
    # "fr"
    # "fun"
    # "fyi"
    # "gdn"
    # "how"
    # "in"
    # "ink"
    # "io"
    # "kim"
    # "krd"
    # "la"
    # "li"
    # "lol"
    # "ltd"
    # "mba"
    # "me"
    # "men"
    # "moe"
    # "mom"
    # "net"
    # "nu"
    # "nyc"
    # "one"
    # "onl"
    # "org"
    # "pe"
    # "pro"
    # "pub"
    # "pw"
    # "red"
    # "rip"
    # "run"
    # "sex"
    # "sg"
    # "ski"
    # "soy"
    # "tax"
    # "top"
    # "tv"
    # "uk"
    # "uno"
    # "us"
    # "vc"
    # "vet"
    # "vin"
    # "vip"
    # "win"
    # "ws"
    # "wtf"
    # "xxx"
    # "xyz"
