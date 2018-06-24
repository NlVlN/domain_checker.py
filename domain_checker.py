#!/usr/bin/env python3
#whois and dig utilities are required 
from subprocess import getoutput
import time
from datetime import datetime
from random import randint

with open('3char_domain_list.txt') as f:
    char = f.read().splitlines()
data = ''


for line in char:
    print('\n\n\nTesting {0} domain'.format(line))
    bash = str(getoutput('dig soa {0}'.format(line)))

    if ('a-dns.pl. dnsmaster.nask.pl.' not in bash):
        print('\n{0} registered'.format(line))

    else:
        while True:
            d = datetime.now().isoformat()
            bash = str(getoutput('whois {0}'.format(line)))
            if ('request limit exceeded' in bash):
                print('\nRequest limit exceeded, sleep few seconds    {0}'.format(d))
                time.sleep(randint(450, 750))

            elif ('No information available about domain name' in bash):
                data += line + '\n'
                with open('domain_list.txt', 'w') as f:
                    f.write(data)
                print('\n{0} DOMAIN NOT REGISTERED    {1}'.format(line, d))
                break

            else:
                print('\n{0} registered    {1}'.format(line, d))
                break
