"""
Alternating split.
"""

class Node(object):
    """
    Base class for a node.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    Context class.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    An alternating split for a linked list.
    """
    if head is None:
        raise ExceptionError
    if head.next is None:
        raise ExceptionError

    head1 = head
    current1 = head1
    head2 = head.next
    current2 = head2
    while current2.next is not None:
        current1.next = current2.next
        current1 = current1.next
        if current1.next is not None:
            current2.next = current1.next
            current2 = current2.next
        else:
            break
    current1.next = None
    current2.next = None
    return Context(head1, head2)
