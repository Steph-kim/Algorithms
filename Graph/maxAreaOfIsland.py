class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visit = set()
        m, n = len(grid), len(grid[0])

        def valid(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            return True

        def dfs(r, c):
            if not valid(r, c) or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res