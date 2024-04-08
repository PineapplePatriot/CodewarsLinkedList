"""
Remove duplicates.
"""

class Node(object):
    """
    Base class for a node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Remove duplicates from a list.
    """
    if head is None:
        return
    current = head
    while current.next is not None:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
