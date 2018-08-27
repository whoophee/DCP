# This problem was asked by Airbnb.
# We're given a hashmap with a key courseId and value a list of courseIds, which
# represents that the prerequsite of courseId is courseIds. Return a sorted ordering
# of courses such that we can finish all courses.
# Return null if there is no such ordering.
# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
# should return ['CSC100', 'CSC200', 'CSCS300'].
####
# return reversed topological sort. That's it.
def explore(st, cur, visited, course_map):
    visited[cur] = True
    for nxt in course_map[cur]:
        if not visited[nxt]:
            explore(st, nxt, visited, course_map)
    st.append(cur)

def course_order(course_map):
    nodes = list(course_map.keys())
    visited = {k:False for k in nodes}
    st = []
    for cur in nodes:
        if not visited[cur]:
            explore(st, cur, visited, course_map)
    return st
####
c = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
print(course_order(c))
