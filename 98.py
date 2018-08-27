# This problem was asked by Coursera.
# Given a 2D board of characters and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# For example, given the following board:
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
####
# This is more of a programming problem than an algorithmic one.
# Caching the results at each point would lead to faster results.
# i.e. cache[index_in_graph][index_in_string] could be stored whenever the result is generated.
class LetterBoard:
    def _exists(self, s, i, cur, visited):
        if i == len(s):
            return True
        x, y = cur
        ret = False
        for x1, y1 in self.adj[x][y]:
            if self.board[x1][y1] == s[i] and not (x1, y1) in visited:
                ret |= self._exists(s, i+1, (x1, y1), visited + [(x1, y1)])
            if ret:
                return True
        return False

    def exists(self, s):
        for p in self.start_point[s[0]]:
            if self._exists(s, 1, p, [p]):
                return True
        return False


    def __init__(self, board):
        m = len(board)
        n = len(board[0])
        self.board = board
        self.adj = [[None]*n for _ in range(m)]
        start_point = {}
        # precalculate adjacent indices
        for x in range(m):
            for y in range(n):

                cur = board[x][y]
                if not start_point.get(cur):
                    start_point[cur] = []
                start_point[cur].append((x, y))

                adj = []
                adj += [(x-1, y)] if x > 0 else []
                adj += [(x, y-1)] if y > 0 else []
                adj += [(x+1, y)] if x+1 < m else []
                adj += [(x, y+1)] if y+1 < n else []
                self.adj[x][y] = adj

        self.start_point = start_point
####
t = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
tmp = LetterBoard(t)
print(tmp.exists("ABCCED"))
print(tmp.exists("ABCB"))
