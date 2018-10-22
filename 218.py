# This problem was asked by Yahoo.
# Write an algorithm that computes the reversal of a directed graph. 
# For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
####
graph1 = {}
graph1['A'] = ['B', 'C', 'D']
graph1['B'] = ['C', 'D']
graph1['C'] = ['D']
####
def reversegraph(gr):
    ret = {}
    # iterate through all nodes
    for beg, v in gr.items():
        # add reverse edge to the graph
        for end in v:
            ret[end] = ret.get(end, []) + [beg]
    return ret
####
print(graph1)
print(reversegraph(graph1))