"""
Stringify function.
"""

def stringify(node):
    """
    Convert a list to a string.
    """
    if node is None:
        return "None"
    current_node = node
    string = str(current_node.data) + " -> "
    while current_node.next is  not None:
        current_node = current_node.next
        string += str(current_node.data) + " -> "
    string += "None"
    return string
