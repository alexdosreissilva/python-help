# coding=UTF-8

import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read('config.ini')
x = cfg.getint('section2', 'confign') #getboolean, getfloat, get
print(x)
