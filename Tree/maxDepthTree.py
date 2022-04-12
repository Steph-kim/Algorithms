from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    return 1 + (max(maxDepth(root.left), maxDepth(root.right)))

# Iterative BFS implementation
def maxDepth2(root):
    if (root is None): return 0
    
    q = deque([root])
    maxDepth = 0
    
    while (q):
        for i in range(len(q)):
            node = q.popleft()
            if (node.left):
                q.append(node.left)
            if (node.right):
                q.append(node.right)
            
        maxDepth += 1
        
    return maxDepth

# Iterative DFS implementation
def maxDepth3(root):
    if (root is None): return 0
    
    stack = [[root, 1]]
    maxDepth = 0
    
    while (stack):
        node, depth = stack.pop()
        if (node):
            maxDepth = max(maxDepth, depth)
            stack.append([node.left, depth+1])
            stack.append([node.right, depth+1])
            
    return maxDepth