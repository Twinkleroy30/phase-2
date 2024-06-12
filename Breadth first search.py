def initiateBFSTraversal(node, visited, adj, result):
    Q = [node]
    visited[node] = True
    while Q:
        currNode = Q.pop(0)
        result.append(currNode)
 
        for neighbour in adj[currNode]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)
 
def printBFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateBFSTraversal(node,visited, adj, result)
    print("BFS Traversal is: ", result)
 
 
 
# 1. Constructing adjacency matrix 
n, m = map(int, input().split())
# n is no.of nodes 
# m is no.of edges 
adj = [] 
for i in range(n + 1):
    eachRow = [0] * (n + 1)
    adj.append(eachRow)
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1
 
#print(adj)
printBFSTraversal(adj, n)