from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        
        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n
        
        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)
            outdegree[i] = len(graph[i])
        
        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        
        safe = [False] * n
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            
            for prev in reverse_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    queue.append(prev)
        
        result = []
        for i in range(n):
            if safe[i]:
                result.append(i)
        
        return sorted(result)
