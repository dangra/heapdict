
def _parent(i):
    return ((i - 1) >> 1)

def _left(i):
    return ((i << 1) + 1)

def _right(i):
    return ((i+1) << 1)

def _min_heapify(heap, i):
    l = _left(i)
    r = _right(i)
    n = len(heap)
    if l < n and heap[l][0] < heap[i][0]:
        low = l
    else:
        low = i
    if r < n and heap[r][0] < heap[low][0]:
        low = r

    if low != i:
        _swap(heap, i, low)
        _min_heapify(heap, low)

def _swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]
    heap[i][2] = i
    heap[j][2] = j

def _decrease_key(heap, i):
    while i:
        parent = _parent(i)
        if heap[parent][0] < heap[i][0]:
            break
        _swap(heap, i, parent)
        i = parent

def heap_reheapify(heap, wrapper):
    while wrapper[2]:
        parentpos = _parent(wrapper[2])
        parent = heap[parentpos]
        _swap(heap, wrapper[2], parent[2])

def heap_popitem(heap):
    wrapper = heap[0]
    if len(heap) == 1:
        heap.pop()
    else:
        heap[0] = heap.pop(-1)
        heap[0][2] = 0
        _min_heapify(heap, 0)
    return wrapper

def heap_append_and_decrease(heap, wrapper):
    heap.append(wrapper)
    _decrease_key(heap, len(heap)-1)

__all__ = ['heap_reheapify', 'heap_popitem', 'heap_append_and_decrease']
