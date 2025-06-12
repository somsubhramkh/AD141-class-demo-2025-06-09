#!/usr/bin/env python3

f = open('myfile.txt','a')
f.write('This is a the first line\n')
f.write('Adding another line\n')
print(type(f))
f.close()
