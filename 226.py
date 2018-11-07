# This problem was asked by Airbnb.
# You come across a dictionary of sorted words in a language you've never seen before. Write a program 
# that returns the correct order of letters in this language.
# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
####
def char_order(dictionary):
    # precedence graph, number of incoming edges for each node and set of all characters
    prec_graph = {}
    inc_edges = {}
    chars = set(''.join(dictionary))

    for i in range(1, len(dictionary)):
        j = 0
        s1 = dictionary[i-1]
        s2 = dictionary[i]
        while s1[j] == s2[j]:
            j += 1

        c1, c2 = s1[j], s2[j]

        prec_graph[c1] = prec_graph.get(c1, []) + [c2]
        inc_edges[c2] = inc_edges.get(c2, 0) + 1
    
    # find character with no incoming edges
    begin = chars - set(inc_edges.keys())
    ret = []

    # this assumes that topological sorting is possible
    # while there exists a node with no incoming edges
    while begin:
        cur = begin.pop()
        # decrease number of incoming edges from each destination node
        # add the node to the "begin" set when the number of incoming edges reaches 0
        for x in prec_graph.get(cur, []):
            inc_edges[x] -= 1
            if inc_edges[x] == 0:
                begin.add(x)
        # add the traversed node to result list
        ret.append(cur)

    return ret
####
print(char_order(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']))