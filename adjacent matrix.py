n,m =map(int, input().split())
adj = [] 
print(adj)
for i in range(n + 1):
    eachRow = [0] * (n + 1)
    adj.append(eachRow)
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1
print(adj)