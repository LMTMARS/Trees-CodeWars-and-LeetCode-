"""
This code is for Sort binary tree by levels.
"""
from collections import deque
class Node:
    """
    This class describes Node objects.
    """
    def __init__(self, L, R, value):
        self.value = value
        self.left = L
        self.right = R

def tree_by_levels(node):
    """
    This function sorts
    binary trees by levels.
    """
    res = []
    if node is None:
        return []
    
    to_visit = deque()
    to_visit.append(node)

    while to_visit:
        current = to_visit.popleft()
        res.append(current.value)
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)
    return res