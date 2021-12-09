import pathlib
import sys

def add_edge(adj, src, dest):
    adj[src].add(dest)
    adj[dest].add(src)

def BFS(adj, src, dest, v, pred, dist, c_a):
    visited = [False] * (v+1)
    queue = []

    visited[src] = True
    dist[src] = 0
    queue.append(src)

    while queue:
        u = queue.pop(0)
        for i in adj[u]: #for all neigbours of u
            if not visited[i]: #if not visited
                visited[i] = True

                dist[i] = dist[u] + 1
                pred[i] = u
                queue.append(i)

            if (i == dest):
                return True
    return False

def printShortestDistance(adj, s, dest, v, minimum_cost, c_a):
    pred=[-1] * (v +1)
    dist=[2*v] * (v+1)

    c = ""
    if (BFS(adj, s, dest, v, pred, dist, c_a) == False):
        c = "Impossible"
    
    if(dist[dest] > minimum_cost):
        c = minimum_cost
    else: 
        if c != "Impossible":
            c = dist[dest]
    
    print(c)
        
lines = []

for line in sys.stdin:
    if line == '': # If empty string is read then stop the loop
        break
    lines.append(line.rstrip('\n'))
"""
url = pathlib.Path(__file__).parent.resolve()
file = str(url) + "/" + "05"

with open(file) as f:
    for line in f:
        lines.append(line.rstrip('\n'))
"""

v, nb_train_routes, nb_cities_airports, starting_city, arrival_city = [int(i) for i in lines[0].split(" ")]
starting_city -= 1
arrival_city -= 1
cities_with_airport = []

if lines[1] != "":
    cities_with_airport = [i-1 for i in [int(i) for i in lines[1].split(" ")]]

adj = [set() for i in range(v+1)]
for l in lines[2:]:
    a, b =  [i-1 for i in [int(i) for i in l.split(" ")]]
    add_edge(adj, a, b)

for c in cities_with_airport:
    add_edge(adj, v, c)

c = 0
if starting_city == arrival_city:
    print(c)
elif starting_city in cities_with_airport and arrival_city in cities_with_airport:
    minimum_cost = 2    
    printShortestDistance(adj, starting_city, arrival_city, v, minimum_cost, cities_with_airport)
elif nb_train_routes == 0:
    print("Impossible")
else:
    printShortestDistance(adj, starting_city, arrival_city, v, sys.maxsize, cities_with_airport)
