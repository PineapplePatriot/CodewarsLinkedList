"""
Recursive reverse.
"""

class Node(object):
    """
    Base class for a node.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Reverse a list recursively.
    """
    if head is None:
        return
    lst = [head]
    current = head
    while current.next is not None:
        lst.append(current.next)
        current = current.next
    lst_rev = lst[::-1]
    head = lst_rev[0]
    current = head
    for i, v in enumerate(lst_rev[1:]):
        current.next = v
        current = current.next
    current.next = None
    return head
