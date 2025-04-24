"""
This code is for delete node in a bst task.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_if_leaf(root):
    """
    This function checks whether
    a given Node is a leaf.
    """
    return root.right is None and root.left is None

def find_min(node):
    """
    This function finds minimum value in the tree.
    """
    current = node
    while current.left:
        current = current.left
    return current

class Solution(object):

    def deleteNode(self, root, key):
        """
        This function helps delete a node
        from a bst.
        """
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if check_if_leaf(root):
                return None
                
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            to_change = find_min(root.right)
            root.val = to_change.val
            root.right = self.deleteNode(root.right, to_change.val)
            
        return root
        