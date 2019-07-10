#!/usr/bin/python
# coding: utf-8

import os
import os.path


def Version():
    Ver = '1.1.3'
    # print("Version = " + Ver)
    return Ver

dir = input()
path, dirs, files = (os.walk(dir)).__next__()

file_count = len(files)
print (file_count)


print(Version())

