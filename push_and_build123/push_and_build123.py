'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    """
    Update a list.
    """
    # Your code goes here.
    new_head_node = Node(data)
    new_head_node.next = head
    return new_head_node

def build_one_two_three():
    """
    Initialize a list
    """
    head_node = Node(1)
    next_node = Node(2)
    next_next_node = Node(3)
    head_node.next = next_node
    next_node.next = next_next_node
    next_next_node.next = None
    return head_node
