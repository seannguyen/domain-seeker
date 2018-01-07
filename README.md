# domain-seeker
A small script to find available domains that suit your need.

# Getting Started

### Setup configs file:
```sh
$ cp configs.py.sample configs.py
```
Update value inside with your real credentials

### Setup `virtualenv`
```sh
$ virtualenv env
$ source env/bin/active
```

### Install Dependencies
```sh
$ pip install -r requirements.txt
```

# How to use?
```sh
python -m domain-seeker io 2
```
With `io` is the TLD you want to search for and 2 is the length of the domain name you want to search