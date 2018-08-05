# This problem was asked by Google.
# Given an iterator with methods next() and hasNext(), create a wrapper iterator,
# PeekableInterface, which also implements peek(). peek shows the next element
# that would be returned on next().
# Here is the interface:
# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass
#
#     def peek(self):
#         pass
#
#     def next(self):
#         pass
#
#     def hasNext(self):
#         pass
####
# Make the wrapper do the peeking.
class PeekableInterface(object):
    def __init__(self, iterator):
        self.it = iterator
        self.peek_next = None

    def peek(self):
        if not self.peek_next:
            self.peek_next = it.next()
        return self.peek_next

    def next(self):
        ret = self.peek_next
        if not ret:
            ret = it.next()
        self.peek_next = None
        return ret

    def hasNext(self):
        if self.peek_next:
            return True
        return self.it.hasNext()
