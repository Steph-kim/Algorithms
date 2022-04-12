def isSubtree(root, subRoot):
    def isEqual(root1, root2):
        if (not root1 and not root2):
            return True
        
        if (not root1 or not root2):
            return False
        
        if (root1.val != root2.val):
            return False
        
        return isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
    
    if (isEqual(root, subRoot)):
        return True
    
    if (root is None):
        return False
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot) 