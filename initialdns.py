#!/usr/bin/python3

# InitialDNS - Grab domains from a website and map them.
# HackerSifu


import os
import time
import socket
import subprocess
import argparse


def banner():
    print('''
    ******************************************************************
    * InitialDNS - Grab domains from a website and map them.         *
    *                                                                *
    * HackerSifu                                                     *
    ******************************************************************
    Run the help (-h) flag for usage.
    '''
    )


def initial_d():
    parser = argparse.ArgumentParser(description='FirstSnoop - Grab domains from a website and map them to IPs for recon')
    parser.add_argument('--url',help=' Add the URL you want to pull down for snooping.', required=False)
    args = parser.parse_args()
    banner()

    if args.url is None:
        print("No URL submitted. Please rerun with the --url command and a valid URL. Example: www.example.com")
    else:
        print("Checking " + args.url + '...')
        time.sleep(1)
        os.system('wget ' + args.url)
        time.sleep(6)
        os.system('more index.html | grep "href=" | cut -d "/" -f3 | grep ".com"  | cut -d \'"\' -f1 | sort -u > ' + args.url + '.txt')
        time.sleep(2)
        domain_shell = open(args.url + '.sh', 'w+')
        shell_script = [
            '#!/bin/bash',
            '',
            'for url in $(cat ' + args.url + '.txt);do',
            'host $url | grep "has address"',
            'done' 
        ]
        domain_shell.writelines("%s\n" % line for line in shell_script)
        domain_shell.close()
        os.system('chmod 755 ' + args.url + '.sh')
        os.system('./' + args.url + '.sh')
        os.system('rm ' + args.url + '.sh')
        os.system('rm index.html')
        os.system('rm ' + args.url + '.txt')


if __name__ == '__main__':
    initial_d()
