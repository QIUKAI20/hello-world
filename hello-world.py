#!/usr/bin/python
# -*- coding: utf8 -*-
# Author: YY-互娱事业部-张秋凯
# YY: 909013219  QQ: 550761071
# Date : 2017/06/22
# 说明 ：hello wold

import sys
from hashlib import md5

def CheckStringMd5(args):
    m = md5()
    m.update(args)
    str_md5 = m.hexdigest()
    return str_md5
    
if __name__ == '__main__':
    #doing is this...
    if len(sys.argv) > 1:
        print CheckStringMd5(sys.argv[1])
    else:
        print CheckStringMd5("123456")
