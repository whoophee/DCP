# Given a 2-D matrix representing an image, a location of a pixel in the screen
# and a color C, replace the color of the given pixel and all adjacent same colored
# pixels with C.
# For example, given the following matrix, and location pixel of (2, 2), and 'G'
# for green:
# B B W
# W W W
# W W W
# B B B
# Becomes
# B B G
# G G G
# G G G
# B B B
####
def adjacent_coords(coord, m, n):
    ret = []
    x, y = coord
    ret += [(x-1, y)] if x-1 >= 0 else []
    ret += [(x, y-1)] if y-1 >= 0 else []
    ret += [(x+1, y)] if x+1 < m else []
    ret += [(x, y+1)] if y+1 < n else []
    return ret

def recolor(mat, loc, new_colour):
    m = len(mat)
    n = len(mat[0])

    colour = mat[loc[0]][loc[1]]
    st = [loc]
    visited = set()
    # BFS using adjacent coordinates.
    while st:
        cur = st.pop(0)
        # if already visited, ignore
        if cur in visited:
            continue
        # recolour and mark as visited
        mat[cur[0]][cur[1]] = new_colour
        visited.add(cur)

        for x, y in adjacent_coords(cur, m, n):
            if mat[x][y] == colour:
                st.append((x, y))
####
def disp(a):
    print()
    for x in a:
        print(' '.join(x))
a = [['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']]
disp(a)
recolor(a, (2, 2), 'G')
disp(a)
