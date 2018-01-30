#-*- coding: utf-8 -*-
import subprocess
import time
from random import randint

#import domain list to check from 'source_list.txt' file
with open('source_list.txt') as f:
    char = f.read().splitlines()
data = ''


for line in char:
    print('testing {0}'.format(line))
    while True:
        bash = str(subprocess.getoutput('whois {0}'.format(line)))
        # make sure that your limit statement looks identical to the one in the if statemant below 
        if ('request limit exceeded' in bash):
            print('\nrequest limit exceeded, sleep few seconds')
            time.sleep(randint(450, 750))
        else:
            #check and modify your statement for unregistered domain
            if ('No information available about domain name' in bash):
                data += line + '\n'
                with open('domain_list.txt', 'w') as f:
                    f.write(data)
                print('\ndomain found\nadded to domain_list.txt')
                break
            else:
                print('Domain registered')
                break
    time.sleep(randint(20, 60))


