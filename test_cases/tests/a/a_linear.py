import sys 
import pathlib
def subset_sum(arr, total, arr2, total2):
    t = [[[False for _ in range(total2+1)] for _ in range(total+1)] for _ in range(len(arr)+1)]
    for row in t:
        row[0][0] = True
    
    for i in range(1, len(arr)+1):
        for j in range(1, total+1):
            for k in range(1, total2+1):
                if (j - arr[i-1] >= 0 and k - arr2[i-1] >= 0):
                    t[i][j][k] = t[i-1][j][k] or t[i-1][j-arr[i-1]][k-arr2[i-1]]
                else:
                    t[i][j][k] = t[i-1][j][k]
    return t
 
lines = []
for line in sys.stdin:
    if line == '': # If empty string is read then stop the loop
        break
    lines.append(line.rstrip('\n'))
"""
url = pathlib.Path(__file__).parent.resolve()
file = str(url) + "/" + "02"

with open(file) as f:
    for line in f:
        lines.append(line.rstrip('\n'))
"""

nb_products, money, kcal = list(map(int, lines[0].split(" ")))
del(lines[0])

p = []
s_m = []
s_k = []

for l in lines:
    l = list(map(int, l.split(" ")))
    s_m.append(l[0])
    s_k.append(l[1])

print("Yes" if subset_sum(s_m, money, s_k, kcal)[nb_products][money][kcal] else "No")