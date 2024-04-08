"""
Get the loop.
"""

def loop_size(node):
    """
    Get the size of a loop.
    """
    current1 = node
    current2 = node.next
    while(current1 != current2):
        current2 = current2.next.next
        current1 = current1.next
    current1 = current1.next
    i = 1
    while(current1 != current2):
        i += 1
        current1 = current1.next
    return i
