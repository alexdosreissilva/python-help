# coding=UTF-8

import os
import glob

print(os.listdir('.'))

print("")

for file in glob.glob('*.py'):
    print(file[0:-3])
    for line in open(file):
        if not line.strip().startswith('#'):
            print(line)
