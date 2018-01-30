#-*- coding: utf-8 -*-
import subprocess
import time
char = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
data = ''

for z in char:
    for x in char:
        for c in char:
            tmp = '%s%s%s.pl' % (z, x, c)
            bash = str(subprocess.getoutput('whois {0}'.format(tmp)))
            if ('No information available about domain name' in bash):
                data += tmp + '\n'
                with open('domain_list.txt', 'w') as f:
                    f.write(data)
            else:
                pass
            time.sleep(37)
