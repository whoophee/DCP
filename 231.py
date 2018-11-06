# This problem was asked by IBM.
# Given a string with repeated characters, rearrange the string so that no two adjacent 
# characters are the same. If this is not possible, return None.
# For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
####
import heapq

def string_nonrep(rep_str):
    char_count = {}
    for c in rep_str:
        char_count[c] = char_count.get(c, 0) + 1
    
    # max heap emulation
    pq = []
    for k, v in char_count.items():
        heapq.heappush(pq, (-v, k))
    
    ret = ""
    # placeholder element
    prev = (1, -1)

    while True:
        prio, c = heapq.heappop(pq)
        # if placeholder element is reached, break
        if prio == 1:
            break
        ret += c
        # insert prev back into heap
        if prev[0] != 0:
            heapq.heappush(pq, prev)
        prev = (prio+1, c)

    return ret if len(ret) == len(rep_str) else None
    
####
print(string_nonrep("aaabbc"))
print(string_nonrep("aaab"))

        