# This problem was asked by Stripe.
# Write a map implementation with a get function that lets you retrieve the value
# of a key at a particular time.
# It should contain the following methods:
# •	set(key, value, time): sets key to value for t = time.
# •	get(key, time): gets the key at t = time.
# The map should work like this. If we set a key at a particular time, it will maintain
# that value forever or until it gets set at a later time. In other words, when we get
# a key at a time, it should return the value that was set for that key set at the most recent time.
# Consider the following examples:
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 1) # get key 1 at time 1 should be 2
####
def range_search(arr, k):
    beg = 0
    end = len(arr)-1

    if not arr or k <= arr[beg]:
        return -1
    if k > arr[end]:
        return end

    while beg + 1 != end:
        mid = (beg + end)//2
        if arr[mid] < k <= arr[end]:
            beg = mid
        else:
            end = mid
    return beg

class TimedMap:
    def get(self, key, t):
        if not self.key_vals.get(key):
            return None
        tmp = range_search(self.key_times[key], t)
        if tmp == -1:
            return None
        nearest_time = self.key_times[key][tmp]
        return self.key_vals[key][nearest_time]

    def set(self, key, val, t):

        if not self.key_vals.get(key):
            self.key_vals[key] = {}
            self.key_times[key] = []

        if not self.key_vals[key].get(t):
            ins = range_search(self.key_times[key], t)
            self.key_times[key].insert(ins+1, t)

        self.key_vals[key][t] = val

    def __init__(self):
        self.key_times = {}
        self.key_vals = {}
####
d = TimedMap()
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
print(d.get(1, 1)) # get key 1 at time 1 should be 1
print(d.get(1, 3)) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
print(d.get(1, 0)) # get key 1 at time 0 should be null
print(d.get(1, 10)) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
print(d.get(1, 1)) # get key 1 at time 1 should be 2
