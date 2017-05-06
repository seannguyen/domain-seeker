from namecheap import Api
from urllib2 import urlopen
import itertools
from string import ascii_lowercase
import json

import configs


def seek(tld):
    domains = get_all_domain_name(tld)
    for i in xrange(0, len(domains) - 1, 100):
        print('Checking domain in range %s-%s/%s' % (i, i+100, len(domains)))
        partly_result = check_availability(domains[i:min(i+100, len(domains))])
        with open('result.json', 'a') as result_file:
            json.dump(partly_result, result_file, indent=4)


def check_availability(domains):
    client_ip = get_current_machine_public_ip()
    api = Api(configs.username, configs.api_key, configs.username, client_ip,
              sandbox=False, debug=False)
    result = api.domains_check(domains)
    return result


def get_current_machine_public_ip():
    return urlopen('http://ip.42.pl/raw').read()

def get_all_domain_name(tld):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9']
    domains = [''.join(i) + '.' + tld for i in itertools.product(alphabets, repeat = 4)]
    return domains


if __name__ == '__main__':
    desired_tld = 'com'
    seek(desired_tld)











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
