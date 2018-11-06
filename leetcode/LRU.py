class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRU:
    def _use(self, key, val):
        cur = Node(key, val)

        if not self.ll_begin:
            self.ll_begin = self.ll_end = cur
        else:
            self.ll_end.next = cur
            cur.prev = self.ll_end
            self.ll_end = cur        

        if key in self.map:
            tmp = self.map[key]
            cur_prev = tmp.prev
            cur_next = tmp.next
            if cur_prev:
                cur_prev.next = cur_next
            else:
                self.ll_begin = cur_next
            cur_next.prev = cur_prev

        elif len(self.map) == self.cap:
            tmp = self.ll_begin
            cur_next = tmp.next
            cur_next.prev = None
            self.ll_begin = cur_next
            self.map.pop(tmp.key)

        else:
            pass
        
        self.map[key] = cur

    def put(self, key, val):
        self._use(key, val)

    def get(self, key):
        cur = self.map.get(key)
        if cur:
            self._use(cur.key, cur.val)
            return cur.val
        else:
            return -1

    def __init__(self, cap):
        self.cap = cap
        self.ll_begin = None
        self.ll_end = None
        self.map = {}
####
cache = LRU(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))