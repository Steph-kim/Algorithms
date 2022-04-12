def invertTree(root):
    if (not root): return root
    # print(root.val)
    root.left, root.right = root.right, root.left
        
    if (root.left):
        invertTree(root.left)
    
    if (root.right):
        invertTree(root.right)
    
    return root        
    