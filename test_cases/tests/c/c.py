import pathlib
url = pathlib.Path(__file__).parent.resolve()
print(url)
file = str(url) + "/" + "05"
lines = []
red_sat = blue_sat = 0

for line in sys.stdin:
    if line == '': # If empty string is read then stop the loop
        break
    lines.append(line.rstrip('\n'))

nb_island, nb_proposals = lines[0].split(" ")

islands = [0] * int(nb_island)
print(str(nb_island) + " / " + str(nb_proposals))

reds = []
blues = []

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w, h, rb):
        self.graph.append([u, v, w, h, rb])
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        i, e = 0, 0
        #self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)
        parent = []
        rank = []
        red_sat = 0
        blue_sat = 0
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1 and i < len(self.graph):
            print(str(i) + " " + str(e))
            if(i == 23):
                print(i)
            u, v, w, h, rb = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                if rb == 0: red_sat += h 
                else: blue_sat += h
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",u, v,end =" ")
            print("-",weight)
        
        print(str(red_sat) + " / " + str(blue_sat))
    
    def get_vertices(self):
        return self.graph
 
 
g = Graph(int(nb_island))

e_w = 1

del lines[0]

for l in lines:
    l_sub = l.split(" ")
    color = l_sub[-1]
    l_sub = l_sub[:-1]
    l_sub = list(map(int, l_sub))
    l_sub.append(color)
    if l_sub[3] == "red":
        reds.append(l_sub)
    else:
        blues.append(l_sub)

print(reds)
print("blue")
print(blues)

reds = sorted(reds, key=lambda item: item[2], reverse=True)
blues = sorted(blues, key=lambda item: item[2], reverse=True)

print("reds size : " + str(len(reds)))
print("blues size : " + str(len(blues)))
print("prop size : " + str(len(reds) + len(blues)))

print(reds)
print("blue")
print(blues)



for r in reds:
    r0 = int(r[0])-1
    r1 = int(r[1])-1
    r2 = int(r[2])
    g.add_edge(r0, r1, e_w, r2, 0)
    e_w += 1


for b in blues:
    b0 = int(b[0])-1
    b1 = int(b[1])-1
    b2 = int(b[2])
    g.add_edge(b0, b1, e_w, b2, 1)
    e_w += 1

print(e_w)
print(len(g.graph))

g.kruskal()