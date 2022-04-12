def isSameTree(p, q):
    if (p is None and q is None):
        return True
    
    if (p is None or q is None):
        return False
    
    if (p.val != q.val):
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    