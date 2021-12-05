#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    words = re.findall(r'\w+', line)
    #line = re.sub('[^\w\d\s\-]+', '', line)
    #words = line.split()
    for word in words:
        print(f'{word}')
