# 2022 paper 1

#Most common letter in str
# from collections import Counter
# text = input()
# c = Counter(text)
# result = []
# max_j = 0
# for i, j in c.most_common():
#     if j >= max_j:
#         max_j = j
#         result.append(i)
#     else:
#         break

# print(" ".join(sorted(result)))

# w, h = input().split()
# w, h = int(w), int(h)
# total = 0
# cols = [""]*w
# coords = set()
# for i in range(h):
#     row = input()
#     results = [x for x in row.split("X") if len(x) >=2]
#     total += len(results)
#     for num in results:
#         coords.add((row.index(num), i))
#     for j in range(len(row)):
#         cols[j] += row[j]
# x = -1
# for col in cols:
#     x += 1
#     results = [i for i in col.split("X") if len(i) >=2]
#     for num in results:
#         if (x, col.index(num)) not in coords:
#             total += 1
#     # total += len(results)

# print(total)

# words = input().split()
# result = []
# for word in words:
#     new = ""
#     new += word[0].upper()
#     old_char = word[0]
#     for i in range(1,len(word)):
#         if word[i] == old_char:
#             #Don't add
#             pass
#         else:
#             old_char = word[i]
#             if old_char not in ['e', 'i', 'o', 'u','a']:
#                 new += old_char
#     result.append(new)
# print("".join(result))

# h = [int(x)-1 for x in input().split()]
# m = max(h)
# cols = [""]*(m+1)
# for x in h:
#     for i in range(len(cols)):
#         if i <= x:
#             cols[i] += "X"
#         else:
#             cols[i] += " "
#         cols[i] += " "

# for col in reversed(cols):
#     print(col.rstrip())

#Pass the parcel - 15 minutes
# n = int(input())
# present = [x for x in input().split("x") if len(x) ]
# from collections import defaultdict
# result = defaultdict(lambda :0)
# for i in range(len(present)):
#     result[i%n] += int(present[i])


# print(max(result.values())) 
#Climbing stairs - had seen it before and took 10 minutes :(
# from functools import lru_cache
# @lru_cache
# def num_pos(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2

#     return num_pos(n-1) + num_pos(n-2)

# print(num_pos(int(input())))

# n = 50
# p,c,t = 0,1,0
# for i in range(n):
#     t = p+c
#     temp_p = p
#     p = c #previous = current
#     c += temp_p
# print(t)

# w, h = [int(x) for x in input().split() ]
# max = 0
# cols = [""]*w
# for i in range(h):
#     row = input()
#     results = [x for x in row.split("X") if len(x) >=2]
#     for num in results:
#         if len(num) > max:
#             max = len(num)
#     for j in range(len(row)):
#         cols[j] += row[j]

# print(cols)
# for col in cols:
#     results = [i for i in col.split("X") if len(i) >=2]
#     for num in results:
#         if len(num) > max:
#             max = len(num)

# print(max)



# w, h = [int(x) for x in input().split() ]
# max_num = 0
# rows = [""]*h
# cols = [""]*w

# for i in range(h):
#     row = input()
#     rows[i] = row
#     for j in range(w):
#         cols[j] += row[j]

# for row in rows:
#     results = [int(i) for i in row.split("X") if len(i) >=2]
#     for num in results:
#         if num > max_num:
#             max_num= num

# for col in cols:
#     results = [int(i) for i in col.split("X") if len(i) >=2]
#     for num in results:
#         if num > max_num:
#             max_num= num

# print(max_num)
#10.30
# nodes = [x for x in input().split(",") if x]
# connections = set()
# for _ in range(int(input())):
#     x,y = input().split(",")
#     connections.add((x,y))
# cur = nodes[0]
# total = [0]
# def traverse(nodes, connections, current, total):
#     if current == nodes[-1]:
#         total[0] += 1
#     for a,b in connections:
#         if a == current:
#             traverse(nodes, connections, b, total)
#     return total
# print(traverse(nodes, connections, cur, total)[0])

#Don't take long
def get_time(pair, times):
    t1 = sum(pair)
    t2 = sum(times) - t1
    return max([t1,t2])


n = int(input())
times = []   
for i in range(n):
    times.append(int(input()))

times = sorted(times)
min_time = 1000000
import itertools
for i in range(1, (len(times)//2)+1):
    for pair in itertools.combinations(times, i):
        t = get_time(pair, times.copy())
        if t < min_time:
            min_time = t

print(min_time)

