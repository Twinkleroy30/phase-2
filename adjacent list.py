n,m=map(int,input().split())
adj = [] 
print(adj)
for i in range(n + 1):
    
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj(u).append(v)
    adj(v).append(u)