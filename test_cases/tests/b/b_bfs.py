import pathlib
import sys

def add_edge(adj, src, dest, a):
    adj[src].append([dest, a])
    adj[dest].append([src, a])

def BFS(adj, src, dest, v, pred, dist):
    visited = [False] * v
    queue = []

    visited[src[0]] = True
    dist[src[0]] = 0
    queue.append(src)

    while queue:
        u = queue.pop(0)
        for i in adj[u[0]]:
            if not visited[i[0]]:
                visited[i[0]] = True
                if u[1] == 1:
                    if i[1] == 1:
                        dist[i[0]] = dist[u[0]] + 2
                    else:
                        dist[i[0]] = dist[u[0]] + 1
                else:
                    dist[i[0]] = dist[u[0]] + 1
                pred[i[0]] = u[0]
                queue.append(i)

            if (i[0] == dest[0]):
                return True
    return False

def printShortestDistance(adj, s, dest, v, minimum_cost):
    pred=[-1] * v
    dist=[2*v] * v

    c = ""
    if (BFS(adj, s, dest, v, pred, dist) == False):
        c = "Impossible"
    
    if(dist[dest[0]] > minimum_cost):
        print(minimum_cost)
    else: 
        if c == "Impossible":
            print(c)
        else:
            print(dist[dest[0]])
        
lines = []

"""
for line in sys.stdin:
    if line == '': # If empty string is read then stop the loop
        break
    lines.append(line.rstrip('\n'))
"""
url = pathlib.Path(__file__).parent.resolve()
file = str(url) + "/" + "01"

with open(file) as f:
    for line in f:
        lines.append(line.rstrip('\n'))

v, nb_train_routes, nb_cities_airports, starting_city, arrival_city = list(map(int, lines[0].split(" ")))

starting_city -= 1
arrival_city -= 1
starting_city = [starting_city, 0]
arrival_city = [arrival_city, 0]

cities_with_airport = []

if len(lines) > 1 and lines[1] != "":
    cities_with_airport = [i-1 for i in list(map(int, lines[1].split(" ")))]

adj = [[] for i in range(v)]
for l in lines[2:]:
    a, b =  [i-1 for i in list(map(int, l.split(" ")))]
    add_edge(adj, a, b, 0)

for c in cities_with_airport:
    for c2 in cities_with_airport:
        b = True
        if c != c2:
            for k in adj[c]:
                if c == k[0]:
                    b = False
            
            for k in adj[c2]:
                if c == k[0]:
                    b = False
            
            if b:
                if c == starting_city[0] or c2 == starting_city[0]:
                    starting_city[1] = 1
                if c == arrival_city[0] or c2 == arrival_city[0]:
                    arrival_city[1] = 1
                add_edge(adj, c, c2, 1)

c = 0
if starting_city[0] == arrival_city[0]:
    print(c)
elif starting_city[1] == 1 and arrival_city[1] == 1:
    minimum_cost = 2    
    printShortestDistance(adj, starting_city, arrival_city, v, minimum_cost)
elif nb_train_routes == 0:
    print("Impossible")
else:
    printShortestDistance(adj, starting_city, arrival_city, v, sys.maxsize)
