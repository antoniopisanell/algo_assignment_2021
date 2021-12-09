import sys

def isSubsetSum(set, n, sum, set2, sum2):
    if (sum == 0 and sum2==0):
        return True
    if (n == 0 or (sum < 0 or sum2 < 0)):
        return False
        
    if (set[n] > sum) or (set2[n] > sum2):              # if one of the two values (money, calories) is bigger than the sum 
        return isSubsetSum(set, n-1, sum, set2, sum2)   # we avoid using this product -> recall with n-1

    inclusion = isSubsetSum(set, n-1, sum-set[n], set2, sum2-set2[n]) # we recurse includig the last product
    exclusion = isSubsetSum(set, n-1, sum, set2, sum2)  # we recurse excluding the last product
    
    return inclusion or exclusion

def isSubsetSum(set, n, sum, set2, sum2, cnt):
    if (sum == 0 and sum2==0):
        return True
    if (n == cnt or (sum < 0 or sum2 < 0)):
        return False
        
    if (set[cnt] > sum) or (set2[cnt] > sum2):
        return isSubsetSum(set, n, sum, set2, sum2, cnt+1)
        
    return isSubsetSum(set, n, sum, set2, sum2, cnt+1) or isSubsetSum(set, n, sum-set[cnt], set2, sum2-set2[cnt], cnt+1)

lines = []
for line in sys.stdin:
    if line == '': # If empty string is read then stop the loop
        break
    lines.append(line.rstrip('\n'))

l = lines[0].split(" ")
nb_products = int(l[0])
money = int(l[1])
kcal = int(l[2])

del(lines[0])

p = []
s_m = []
s_k = []

for l in lines:
    l = l.split(" ")
    s_m.append(int(l[0]))
    s_k.append(int(l[1]))

print("Yes" if isSubsetSum(s_m, nb_products, money, s_k, kcal, 0) else "No")