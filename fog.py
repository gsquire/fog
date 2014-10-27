#!/usr/bin/env python3

# A simple command line tool to check the health of your DigitalOcean droplets.
# author: Garrett Squire, gsquire
import sys
import os

import requests

from termcolor import colored

# Constants that we will use throughout the script.
URL = 'https://api.digitalocean.com/v2/droplets'
OK = 'green'
WARN = 'yellow'
ERR = 'red'

def output_ip(networks):
    """
    Given a list of version 4 network, print out the addresses.
    """
    for network in networks['v4']:
        print('\tipv4 address: {0}'.format(network['ip_address']))

def color_status(status):
    """
    Based on the status of the droplet, color the output.
    """
    if status == 'new' or status == 'archive':
        print('\tstatus: ', end='')
        print(colored(status, WARN))
    elif status == 'off':
        print('\tstatus: ', end='')
        print(colored(status, ERR))
    else:
        print('\tstatus: ', end='')
        print(colored(status, OK))

def parse_output(droplets):
    """
    We will get all of the droplets here and output certain aspects that we
    want to see for the health of each.
    """
    for droplet in droplets['droplets']:
        print('id: {0}'.format(droplet['id']))
        print('\tname: {0}'.format(droplet['name']))
        print('\tregion: {0}'.format(droplet['region']['slug']))
        color_status(droplet['status'])
        output_ip(droplet['networks'])

def main():
    token = os.getenv('DO_TOKEN')
    headers = {'Authorization': 'Bearer {0}'.format(token)}

    req = requests.get(URL, headers=headers)
    if req.status_code == 200:
        parse_output(req.json())
    else:
        print("Could not perform request.")
        sys.exit(1)

if __name__ == '__main__':
    main()
