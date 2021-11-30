from collections import defaultdict
import pathlib
import sys

class Graph:
    def __init__(self, minimum_cost, arrival_vertex):
        self.graph = defaultdict(list)
        self.minimum_cost = minimum_cost
        self.arrival_vertex = arrival_vertex
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self, s):
        if len(self.graph) == 0:
            return -1
        else:   
            visited = [False] * (max(self.graph) + 1)
            
        queue = []  
        current_cost = 0
        
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            current_cost += 1

            if current_cost > self.minimum_cost:
                return self.minimum_cost
            if s == self.arrival_vertex:
                return current_cost

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return -1

url = pathlib.Path(__file__).parent.resolve()
file = str(url) + "/" + "01"
lines = []

with open(file) as f:
    for line in f:
        lines.append(line.rstrip('\n'))

nb_cities, nb_train_routes, nb_cities_airports, starting_city, arrival_city = list(map(int, lines[0].split(" ")))
starting_city -= 1
arrival_city -= 1
cities_with_airport = []
if lines[1] != "":
    cities_with_airport = list(map(lambda i: i-1, list(map(int, lines[1].split(" ")))))

g = Graph(sys.maxsize, arrival_city)
for l in lines[2:]:
    a, b = list(map(lambda i: i-1, list(map(int, l.split(" ")))))
    g.addEdge(a, b)

c = 0
if starting_city == arrival_city:
    print(c)
elif starting_city in cities_with_airport and arrival_city in cities_with_airport:
    minimum_cost = 2
    g.minimum_cost = minimum_cost
    c = g.BFS(starting_city)
    if c == -1:
        c = minimum_cost
elif nb_train_routes == 0:
    c = -1
else:
    c = g.BFS(starting_city)

if c != 0:
    if c == -1:
        print("Impossible")
    else:
        print(c)