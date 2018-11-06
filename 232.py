# This problem was asked by Google.
# Implement a PrefixMapSum class with the following methods:
# •	insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value. 
# •	sum(prefix: str): Return the sum of all values of keys that begin with a given prefix. 
# For example, you should be able to run the following code:
# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3

# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5
####
class Node:
    def add(self, remain, val):
        self.val += val
        if not remain:
            return
        nxt = self.charmap.get(remain[0], Node())
        nxt.add(remain[1:], val)
        self.charmap[remain[0]] = nxt
    
    def get(self, remain):
        if not remain:
            return self.val
        nxt = self.charmap.get(remain[0])
        if not nxt:
            return 0
        else:
            return nxt.get(remain[1:])

    def __init__(self):
        self.charmap = {}
        self.val = 0

class PrefixMapSum:
    def insert(self, key, val):
        self.root.add(key, val)
    def sum(self, key):
        return self.root.get(key)
    def __init__(self):
        self.root = Node()
####
mapsum = PrefixMapSum()

mapsum.insert("columnar", 3)
print(mapsum.sum('col'))

mapsum.insert("column", 2)
print(mapsum.sum('col'))

mapsum.insert("co", 2)
print(mapsum.sum('c'))

