""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    """
    Insert a node into the correct location.
    """
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None:
        return Node(data)
    if data <= head.data:
        new_head = Node(data)
        new_head.next = head
        return new_head

    current_node = head

    while current_node.next is not None:
        prev_node = current_node
        current_node = current_node.next 
        if data < current_node.data:
            node = Node(data)
            prev_node.next = node
            node.next = current_node
            return head

    node = Node(data)
    current_node.next = node
    node.next = None
    return head
