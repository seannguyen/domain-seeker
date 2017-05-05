from namecheap import Api
from urllib2 import urlopen

import configs


def seek(tld):
    availabilities = check_availability(['us.xyz', 'honestbee.com'])
    for domain, availability in availabilities.iteritems():
        print("%s: %s" % (domain, availability))


def check_availability(domains):
    client_ip = get_current_machine_public_ip()
    api = Api(configs.username, configs.api_key, configs.username, client_ip,
              sandbox=False, debug=False)
    result = api.domains_check(domains)
    return result


def get_current_machine_public_ip():
    return urlopen('http://ip.42.pl/raw').read()


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
