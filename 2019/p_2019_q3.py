import math
def isvalid(start, block):
    block = start + "".join(block)
    for i in range(len(block)):
        for j in range(i+1,len(block)):
            if block[j] > block[i]:
                for k in range(j+1, len(block)):
                    if block[k] > block[j]:
                        return False
    return True
                
def gen_blocks_maths(n):
    # FOR 4
    #if A is first then has to be reverse alphabetical
    #if B first then reverse alphabetical but a can go anywhere (gaps so n-1)
    #if C first then 
    #8 FED ABCDEFGH
    if n == 1:
        return 1
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lets = []
    for i in range(n):
        lets.append(ALPHA[i])
    # for char in start:
    #     lets.remove(char)
    result = 0
    for i in range(len(lets)):
        fixed = lets[i] + "".join(reversed(lets[i+1:]))
        if i > 0:
            left = gen_blocks_maths(i)
        else:
            left = 1
        #Now is the tricky bit
        #For each of the gaps use a stick 
        total = math.factorial(len(fixed)+1+i)/(math.factorial(len(fixed)+1)*math.factorial(i))
        total *= left
        result += total
        #GIVING UP FOR NOW
    return result
        

print(gen_blocks_maths(6))
def gen_blocks(n, start):
    import itertools
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lets = []
    for i in range(n):
        lets.append(ALPHA[i])
    for char in start:
        lets.remove(char)
    result = 0
    for perm in itertools.permutations(lets):
        if isvalid(start, perm):
            result += 1

    return result

print(gen_blocks(6, ""))

import unittest
class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.cases = [
            (1, "A", 1),
            (2, "AB", 1),
            (2, "BA", 1),
            (4, "C", 5),
            (4, "AB", 0),
            (6, "FED", 5),
            (8, "HGFEDCBA", 1),
            (8, "H", 429),
            (8, "FED", 28),
            (8, "FEH", 42),
            (12, "LKJI", 1430),
            (13, "MH", 13260),
            (14, "N", 742900),
            (16, "KHF", 5508),
            (16, "FEDCBA", 1),
            (18, "FRN", 0),
            (18, "QPON", 2674440),
            (18, "R", 129644790)
        ]
    def testBlockgen(self):
        for n,start, result in self.cases:
            end = gen_blocks(n, start)
            print(end, result)
            assert(end == result)

# if __name__ == '__main__':
#     unittest.main()

#3b -> (all but BIO) BOI, OBI, OIB, IBO,IOB
# 3C->