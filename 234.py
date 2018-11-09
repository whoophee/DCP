# This problem was asked by Microsoft.
# Recall that the minimum spanning tree is the subset of edges of a tree that connect 
# all its vertices with the smallest possible total edge weight. Given an undirected 
# graph with weighted edges, compute the maximum weight spanning tree.
####

class Graph:
    def add_edge(self, begin, end, l):

        self.edges[(begin, end)] = l
        self.edges[(end, begin)] = l

        tmp = self.graph.get(begin, set())
        tmp.add(end)
        self.graph[begin] = tmp

        tmp = self.graph.get(end, set())
        tmp.add(begin)
        self.graph[end] = tmp

    def __init__(self):
        self.edges = {}
        self.graph = {}


gr = Graph()

gr.add_edge('A', 'B', 7)
gr.add_edge('A', 'D', 5)
gr.add_edge('D', 'B', 9)
gr.add_edge('B', 'C', 8)
gr.add_edge('C', 'E', 5)
gr.add_edge('B', 'E', 7)
gr.add_edge('D', 'E', 15)
gr.add_edge('D', 'F', 6)
gr.add_edge('F', 'E', 8)
gr.add_edge('F', 'G', 11)
gr.add_edge('E', 'G', 9)

####
import heapq

def max_prims(gr):
    ret = []
    visited = set()
    # priority queue for edges
    edgeq = []
    # choose a random beginning node
    beg = list(gr.graph.keys())[0]
    visited.add(beg)
    # add all edges from the beginning node to the edge queue
    # since heapq implements a minheap, the edges are pushed
    # with negative length to simulate a maxheap
    for e in gr.graph[beg]:
        heapq.heappush(edgeq, (-gr.edges[(beg, e)], beg, e))
    # as long as there exist edges in the queue
    while edgeq:
        # get the edge with maximum length
        _, beg, end = heapq.heappop(edgeq)
        # if the end is already present in the graph, choose another edge
        if end in visited:
            continue
        # add the discovered edge to the result set
        ret.append((beg, end))
        visited.add(end)
        # add all edges emanating from the current endpoint to the heap
        for e in gr.graph[end]:
            heapq.heappush(edgeq, (-gr.edges[(end, e)], end, e))
            
    return ret

####
print(max_prims(gr))
    
    
    

    
    