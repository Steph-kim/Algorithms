from collections import deque

def buildGraph(rows, cols, grid, graph):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                graph[r][c] = 0
            else:
                graph[r][c] = 1            

def is_valid(graph, r, c):
    m, n = len(graph), len(graph[0])
    if r < 0 or c < 0 or r >= m or c >= n:
        return False
    return True          

def reachTheEnd(grid, k):
    rows, cols = len(grid), len(grid[0])
    graph = [[1 for _ in range(cols)] for _ in range(rows)]
    buildGraph(rows, cols, grid, graph)

    graph[0][0] = 1
    queue = deque()
    queue.append((0,0))

    while len(queue):
        r, c = queue.popleft()
        d = graph[r][c]

        if r == rows-1 and c == cols-1:
            print("woopee")
            if d <= k:
                return 'Yes'
            else: 
                return 'No'

        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if is_valid(graph, nr, nc) and graph[nr][nc] == '1':
                queue.append((nr, nc))
                graph[nr][nc] = d + 1

    return 'No'

test = ['..##', '#.##', '#...']
for s in test:
    print(s)
print(reachTheEnd(test, 5))



