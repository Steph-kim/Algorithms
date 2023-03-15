class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs (ind, i, j):
            if self.Found:
                return
            
            if ind == k:
                self.Found = True
                return
            
            if i < 0 or i >= m or j < 0 or j >= n: 
                return
            
            print(i, " ", j, " ", board[i][j])

            
            cur = board[i][j]
            if cur != word[ind]:
                return
            
            board[i][j] = '#'
            for x, y in [[0,-1],[0,1],[-1,0],[1,0]]:
                dfs(ind + 1, i+x, j+y)

            board[i][j] = cur

            
        self.Found = False
        m = len(board)
        n = len(board[0]) 
        k = len(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.Found:
                    return True
                dfs(0, i, j)
            
        return self.Found