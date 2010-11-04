#!/usr/bin/python
import os
import timeit
from random import shuffle
from pickle import dump

SAMPLES = '/tmp/heapdict-perftest.samples'

if not os.path.exists(SAMPLES):
    cats = range(100000)
    score = [float(i)/2.0 for i in range(len(cats))]
    shuffle(score)
    docs = list(zip(cats, score))
    with open(SAMPLES, 'wb') as samples:
        dump(docs, samples)

setup_fmt = '''
from pickle import load
from %(package)s import heapdict

heap = heapdict()
docs = load(open('%(SAMPLES)s', 'rb'))
'''

stmt = '''
for k, v in docs:
    heap[k] = v

try:
    while True:
        heap.popitem()
except IndexError:
    pass
'''

def _timeit(package_name):
    setup = setup_fmt % dict(package=package_name, SAMPLES=SAMPLES)
    t = timeit.Timer(stmt, setup)
    return min(t.repeat(repeat=3, number=1))

t_python = _timeit('heapdict')
print 'python = %f' % t_python
if os.path.exists('cheapdict.so'):
    t_cython = _timeit('cheapdict')
    print 'cython = %f' % t_cython
    print 'cy/py  = %.2f%%' % float(t_cython / t_python * 100)
