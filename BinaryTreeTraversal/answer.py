"""
This code is for binary tree traversal.
"""
class Node:
    """
    This class describes Node objects.
    """
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def pre_order(node, res=None):
    """
    This function performs
    a pre_order traversal of a
    binary tree.
    """
    if res is None:
        res = []
    if not node:
        return res
    
    res.append(node.data)
    pre_order(node.left, res)
    pre_order(node.right, res)

    return res

def in_order(node, res = None):
    """
    This function performs
    an in_order traversal of
    a binary tree.
    """
    if res is None:
        res = []
    
    if not node:
        return res 
    
    in_order(node.left, res)
    res.append(node.data)
    in_order(node.right, res)
    
    return res

def post_order(node, res=None):
    """
    This function performs
    a post_order traversal of
    a binary tree.
    """
    if res is None:
        res = []
    
    if not node:
        return res 

    post_order(node.left, res)
    post_order(node.right, res)

    res.append(node.data)

    return res