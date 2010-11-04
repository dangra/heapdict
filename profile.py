import pstats
import cProfile
from pickle import load
from heapdict import heapdict

SAMPLES = '/tmp/heapdict-perftest.samples'
docs = load(open(SAMPLES, 'rb'))

def main():
    heap = heapdict()

    for k, v in docs:
        heap[k] = v

    try:
        while True:
            heap.popitem()
    except IndexError:
        pass


if __name__ == "__main__":  
    cProfile.run("main()", "Profile.prof")  
    s = pstats.Stats("Profile.prof")  
    s.strip_dirs().sort_stats("time").print_stats(10) 
