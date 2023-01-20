# words = input().split()
# result = []
# for word in words:
#     if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#         result.append(word + "-yay")
#     else:
#         result.append(word[1:] + "-" + word[0] + "ay")

# print(" ".join(result))

# import math

# earnings = [int(x) for x in input().split()]
# total = 0
# for i in range(len(earnings)):
#     total += earnings[i] - 20
#     if total >= 1000:
#         print(i+1)
#         break
import math
row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]
row3 = [int(x) for x in input().split()]
s = sum(row1)
muggle = False
if s != sum(row2) or s!= sum(row3):
    muggle = True
else:
    for i in range(len(row1)):
        s2 = row1[i] + row2[i] + row3[i]
        if s != s2:
            muggle = True

    diag1 = row1[0]+row2[1]+row3[2]
    diag2 = row1[2]+row2[1]+row3[0]
    if diag2 == diag1 and diag2 == s:
        pass
    else:
        muggle = True
        
if muggle:
    print("muggle")
else:
    print("magic")

