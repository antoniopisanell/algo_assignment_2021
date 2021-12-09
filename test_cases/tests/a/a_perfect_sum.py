import numpy as np
import pathlib

def one_more(product, solvable):
    result = solvable.copy()
    m_inc, k_inc = product
    for m in range(m_inc, M):
        for k in range(k_inc, K):
            if not solvable[m][k]:
                result[m][k] = solvable[m - m_inc][k - k_inc]
    return result

M = 7 
K = 12
products = [(1, 3), (2, 4), (5, 8), (4, 5)]
M = 42
K = 23
products = [
(10, 3),
(6, 6),
(10, 1),
(6, 5),
(3, 5),
(7, 1),
(10, 7),
(10, 8),
(8, 6),
(1, 1)
]

# For an empty list of products, only the problem with m=k=0 is solvable:
solvable = np.zeros(shape=(M + 1, K + 1), dtype=bool)
solvable[0, 0] = True
solvable = [[False * K] * M]


lines = []
"""
for line in sys.stdin:
    if line == '': # If empty string is read then stop the loop
        break
    lines.append(line.rstrip('\n'))
"""
url = pathlib.Path(__file__).parent.resolve()
file = str(url) + "/" + "03"

with open(file) as f:
    for line in f:
        lines.append(line.rstrip('\n'))

nb_products, money, kcal = list(map(int, lines[0].split(" ")))

del(lines[0])

p = []
s_m = []
s_k = []

for l in lines:
    l = list(map(int, l.split(" ")))
    s_m.append(l[0])
    s_k.append(l[1])
    p.append((l[0], l[1]))


for product in products:
    solvable = one_more(product, solvable)

#for prod in p:
#    solvable = one_more(prod, solvable)

# The full problem of interest:
print(solvable[money, kcal])