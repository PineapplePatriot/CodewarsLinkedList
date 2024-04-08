"""
Get the nth node.
"""

from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    """
    Get the nth node from a list.
    """
    if (node is None) or index < 0:
        raise IndexError("error")
    if index == 0:
        return node
    current_node = node
    for i in range(index):
        if current_node.next is None:
            raise IndexError("error")
        current_node = current_node.next

    return current_node
