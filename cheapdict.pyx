from _heapdict import heap_append_and_decrease, heap_reheapify, heap_popitem


cdef class heapdict(object):
    cdef public list heap
    cdef dict d

    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    def clear(self):
        self.heap.clear()
        self.d.clear()

    def __setitem__(self, key, value):
        if key in self.d:
            del self[key]
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        heap_append_and_decrease(self.heap, wrapper)

    def __delitem__(self, key):
        wrapper = self.d[key]
        heap_reheapify(self.heap, wrapper)
        self.popitem()

    def __getitem__(self, key):
        return self.d[key][0]

    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        """D.popitem() -> (k, v), remove and return the (key, value) pair with lowest\nvalue; but raise KeyError if D is empty."""
        wrapper = heap_popitem(self.heap)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]

    def __len__(self):
        return len(self.d)

    def peekitem(self):
        """D.peekitem() -> (k, v), return the (key, value) pair with lowest value;\n but raise KeyError if D is empty."""
        return (self.heap[0][1], self.heap[0][0])

    def update(self, *a, **kw):
        for k, v in dict(*a, **kw).iteritems():
            self[k] = v


__all__ = ['heapdict']
