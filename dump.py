#! /bin/python

from urllib import request
import time

base = input('url base: ')
seg_max = int(input('maximum segment: '))

for i in range(0, seg_max+1):
    req = request.urlopen(f'{base}/{i:05}.ts')
    with open(f'{i:05}.ts', 'wb') as f:
        f.write(req.read())
    time.sleep(0.01)
