"""
Move node.
"""

class Node(object):
    """
    Base class for a node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    Context class.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Move a node.
    """
    s = source.next
    d = source
    d.next = dest
    # Your code goes here.
    # Remember to return the context.
    return Context(s, d)
