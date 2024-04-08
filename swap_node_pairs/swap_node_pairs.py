"""
Swap node pairs.
"""
from preloaded import Node

def swap_pairs(head):
    """
    Swap pairs of nodes in a list.
    """
    if head is None:
        return None
    if head.next is None:
        return head

    lst = [head]
    current = head
    while current.next is not None:
        lst.append(current.next)
        current = current.next

    l = len(lst)//2
    head = lst[1]
    head.next = lst[0]
    current = head.next

    for i in range(1, l):
        current.next = lst[2*i+1]
        current = current.next
        current.next = lst[2*i]
        current = current.next

    if len(lst) % 2 != 0:
        current.next = lst[-1]
        current = current.next
    current.next = None
    return head
