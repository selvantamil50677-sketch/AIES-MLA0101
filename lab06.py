graph = {'A':[('B',1),('C',4)], 'B':[('G',5)], 'C':[('G',2)], 'G':[]}
h = {'A':3, 'B':2, 'C':1, 'G':0}
q = [(h['A'], 0, 'A', ['A'])]

while q:
    q.sort()
    f, cost, node, path = q.pop(0)
    if node == 'G':
        print("Path:", path)
        print("Cost:", cost)
        break
    for nxt, w in graph[node]:
        c = cost + w
        q.append((c + h[nxt], c, nxt, path + [nxt]))












