"""
Parse list from string.
"""

def linked_list_from_string(s):
    """
    Parse a linked list from string.
    """
    lst = s.split(" -> ")
    if len(lst) == 1:
        return None
    if len(lst) == 2:
        head_node = Node(int(lst[0]))
        head_node.next = None
        return head_node

    head_node = Node(int(lst[0]))
    next_node = Node(int(lst[1]))
    head_node.next = next_node
    for i, v in enumerate(lst[2:]):
        if v == 'None':
            next_node.next = None
            break
        else:
            further_node = Node(int(v))
            next_node.next = further_node
            next_node = further_node

    return head_node
