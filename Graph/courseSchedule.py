"""
Topological sorting for Directed Acyclic Graph (DAG) 
is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. 
Topological Sorting for a graph is not possible if the graph is not a DAG.

The following solution uses BFS with Kahn's algorithm for Topological Sorting
Kahn's algortih takes advantage of the fact that a DAG G 
has at least one vertex with in-degree 0 and one vertex with out-degree 0. 

Algorith: Steps involved in finding the topological ordering of a DAG: 
    Step-1: Compute in-degree (number of incoming edges) for each of the vertex present in the DAG and initialize the count of visited nodes as 0.
    Step-2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
    Step-3: Remove a vertex from the queue (Dequeue operation) and then. 
        1. Increment count of visited nodes by 1.
        2. Decrease in-degree by 1 for all its neighbouring nodes.
        3. If in-degree of a neighbouring nodes is reduced to zero, then add it to the queue.
    Step 4: Repeat Step 3 until the queue is empty.
    Step 5: If count of visited nodes is not equal to the number of nodes in the graph 
            then the topological sort is not possible for the given graph.

Complexity Analysis
Time complexity: O(V + E)
Space Complexity: O(V + E)

Firstly, we need to finish prerequisites courses before taking a main course so this is a directed graph problem. 
In other words, this problem can be restated to Detect cycle in a directed graph 
or similarly Check if a graph is acyclic. 

"""

from collections import deque

class Solution:
    # build an adjacency list from the edges list
    def buildAdjacencyList(self, numNodes, edgeList):
        adjList = [[] for _ in range(numNodes)]
        
        # [c1, c2]
        # course c1 is a prerequisite of course c2
        # i.e. c2c1 is a directed edge in the graph
        
        for c1, c2 in edgeList:
            adjList[c2].append(c1)
        return adjList
        
        
    def topoBFS(self, numNodes, edgeList):
        adjList = self.buildAdjacencyList(numNodes, edgeList)
        
        # Step-1
        # Store a list of the number of incoming edges of each vertex
        # where v2v1 forms a directed edge
        inDegrees = [0]*numNodes
        for v1, v2 in edgeList:
            inDegrees[v1] += 1

        # Step-2
        # Queue all vertices with no incoming edge
        # At least one such vertex/node must exist in a non-empty DAG
        # Vertices in this queue must eventually have the same ordering as topological sort
        # sort
        queue = deque([])
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)


        # Step 4: Repeat Step 3 until the queue is empty.
        # initialise count of visited nodes
        count = 0
        # empty list that will contain final topo order
        topoOrder = []
        
        while queue:
            # Step 3
            # Pop a vertex from the queue 
            # depending on the order that vertices are removed from queue,
            # a different solution is created
            v = queue.popleft()
            # append it to topoOrder
            topoOrder.append(v)
            # Increment count of visited nodes by 1.
            count += 1
            
            # Decrease in-degree by 1 for all its neighbouring nodes.
            for nei in adjList[v]:
                inDegrees[nei] -= 1
                # If in-degree of a neighbouring nodes is reduced to zero, then add it to the queue.
                if inDegrees[nei] == 0:
                    queue.append(nei)
        
        # Step 5
        # If count of visited nodes is not equal to the number of nodes in the graph 
        # then the topological sort is not possible for the given graph.
        # Else graph has at least one cycle
        return topoOrder if count == numNodes else None
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False 