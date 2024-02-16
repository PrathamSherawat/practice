graph={
    'A': ['B','C','D'],
    'B': ['A'],
    'C': ['A','D'],
    'D': ['A','C','E'],
    'E': ['D'],
}

def bfs(node):
    visited=[False]*(len(graph))
    
    queue=[]
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        v=queue.pop(0)
        print(v,end=" ")
        for i  in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

if __name__ == "__main__":
    bfs('A')