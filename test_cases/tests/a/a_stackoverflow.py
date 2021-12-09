import sys
import pathlib

def one_more(product, solvable, M, K):
    result = solvable.copy()
    m_inc, k_inc = product
    for m in range(0, M + 1):
        for k in range(0, K + 1):
            result[m][k] = solvable[m - m_inc][k - k_inc] or solvable[m][k]
            # if not solvable[m][k]:
            #     result[m][k] = solvable[m - m_inc][k - k_inc]
    return result

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

nb_products, money, kcal = list(map(int, lines[0].split(" ")))
del(lines[0])

p = []

solvable = [[[False  for _ in range(kcal+1)] for _ in range(money+1)] for _ in range(nb_products +1)]
#solvable[0][0] = True

for i in range(nb_products+1):
    for j in range(money+1):
        solvable[i][j][0] = True 

print(solvable)

for l in lines:
    l = list(map(int, l.split(" ")))
    p.append((l[0], l[1]))

# for prod in p:
#    solvable = one_more(prod, solvable, money, kcal)
for i in range(0, nb_products):
    m_inc, k_inc = p[i]
    for m in range(m_inc, money + 1):
        for k in range(k_inc, kcal + 1):
            solvable[i][m][k] = solvable[i-1][m - m_inc][k - k_inc] or solvable[i-1][m][k]

print("Yes" if solvable[nb_products][money][kcal] else "No")