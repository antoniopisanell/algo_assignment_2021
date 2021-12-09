import sys
import pathlib

def isSubsetSum(set, n, sum, set2, sum2, s):
    if (sum == 0 and sum2==0):
        return True
    if n == 0 or sum < 0 or sum2 < 0:
        return False

    if (s[n][sum] != -1):
        return s[n][sum] 
        
    if (set[n-1] > sum) or (set2[n-1] > sum2):
        s[n][sum] = isSubsetSum(set, n-1, sum, set2, sum2, s)
        return s[n][sum]

    exclusion = isSubsetSum(set, n-1, sum, set2, sum2, s)
    inclusion = isSubsetSum(set, n-1, sum-set[n-1], set2, sum2-set2[n-1], s)
    s[n][sum] = exclusion or inclusion
    return s[n][sum] 

def isSubsetSum1(set, n, sum, s, set2, sum2):
    if (sum == 0):
        s[n][sum] = True
    if(sum2 == 0):
        s[n][sum] = True
            # s[0][0] = True
            # return True
    if n == 0 or sum < 0 or sum2 < 0:
        return False
        
    if (s[n][sum] != -1):
        return s[n][sum] 
        
    if (set[n-1] > sum or set2[n-1] > sum2):
        s[n][sum] = isSubsetSum1(set, n-1, sum, s, set2, sum2)
        return s[n][sum]

    exclusion = isSubsetSum1(set, n-1, sum, s, set2, sum2)
    inclusion = isSubsetSum1(set, n-1, sum-set[n-1], s, set2, sum2-set2[n-1])
    s[n][sum] = exclusion or inclusion

    return s[n][sum] 

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
    l = l.split(" ")
    s_m.append(int(l[0]))
    s_k.append(int(l[1]))

s = [[-1 for _ in range(money+1)] for _ in range (nb_products+1)]
s2 = [[-1 for _ in range(kcal+1)] for _ in range (nb_products+1)]
#print("Yes" if isSubsetSum(s_m, nb_products, money, s_k, kcal, s) else "No")
print("Yes" if isSubsetSum1(s_m, nb_products, money, s, s_k, kcal) else "No")