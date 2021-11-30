import pathlib
import sys
url = pathlib.Path(__file__).parent.resolve()
file = str(url) + "/" + "01"
lines = []

with open(file) as f:
    for line in f:
        lines.append(line.rstrip('\n'))

nb_cities, nb_train_routes, nb_cities_airports, starting_city, arrival_city = list(map(int, lines[0].split(" ")))
starting_city -= 1
arrival_city -= 1
cities_with_airport = list(map(lambda i: i-1, list(map(int, lines[1].split(" ")))))

G = [None] * nb_cities
for l in lines[2:]:
    a, b = list(map(lambda i: i-1, list(map(int, l.split(" ")))))
    print(str(a) + " / " + str(b))
    if G[a] == None:
        G[a] = []
    if G[b] == None:
        G[b] = []

    G[a].append(b)
    G[b].append(a)

minimum_cost = sys.maxsize

if starting_city in cities_with_airport and arrival_city in cities_with_airport:
    minimum_cost = 2
elif nb_train_routes == 0:
    print("Impossible")

def search_node(actual_node, finishing_node, parent_node, current_cost):
    if current_cost > minimum_cost:
        return minimum_cost
    if actual_node == finishing_node:
        return current_cost

    for n in G[actual_node]:
        if n != parent_node:
            c = search_node(n, finishing_node, actual_node, current_cost+1)
    
    return -1

def search_node_for(actual_node, finishing_node, parent_node, current_cost):
    for n in G[actual_node]:
        for m in G[n]:
            if m != actual_node:
                if current_cost > minimum_cost:
                    return minimum_cost
                if m == finishing_node:
                    return current_cost

            c = search_node(n, finishing_node, actual_node, current_cost+1)
    
    return -1

cost = search_node(starting_city, arrival_city, starting_city, 0)

if cost == -1:
    print("Impossible")

print(cost)