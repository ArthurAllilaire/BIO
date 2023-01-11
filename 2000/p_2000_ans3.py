from collections import *
from itertools import combinations_with_replacement as combs
from itertools import permutations as perms
from itertools import combinations
from copy import *
from math import *
from time import time

FREQ = defaultdict(int)

n = int(input())

diea = tuple(sorted(list(map(int, input().split()))))
dieb = tuple(sorted(list(map(int, input().split()))))

start = time()

m = 0
mm = 20
for a in diea:
    for b in dieb:
        FREQ[a+b] += 1
        m = max(m, a+b)
        mm = min(mm, a+b)

m += 1
#print(mm, m)

# we can guarentee that one die cannot have numbers greater than 8
nums = [1,2,3,4,5,6,7,8]

dice = list(combs(nums, n))

#print(FREQ)

possible = False
for da in dice:
#    da = sorted(da)
#    da = (1,3,3,5)
#    print(da)
    if da == diea or da == dieb:
        continue
    db = []
    valid = True
    freq = copy(FREQ)
    for _ in range(n):
        a = -1
        for i in range(mm, m):
            if freq[i] > 0:
                a = i
                break
        if a == -1:
            valid = False
            break
        db.append(a - da[0])
        if db[-1] <= 0:
            valid = False
            break
        for i in range(n):
            v = db[-1] + da[i]
            if freq[v] > 0:
                freq[v] -= 1
            else:
                valid = False
                break

    if valid:
        for a in da:
            print(a, end=" ")
        print()
        for b in db:
            print(b, end=" ")
        print()
        possible = True
        break

if not possible:
    print("Impossible")

print("Time Taken:", time() - start)