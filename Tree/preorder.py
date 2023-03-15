class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:  
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res