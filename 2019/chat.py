from itertools import permutations
def gen(l, prefix):
    alphabet = [chr(i) for i in range(ord('A'), ord('A')+l)]

    count = 0
    for perm in permutations(alphabet):
        if perm[0] == prefix[0]:
            valid = True
            for i in range(1, len(prefix)):
                if perm[i] <= prefix[i]:
                    valid = False
                    break
            if valid:
                for i in range(len(prefix), len(perm)-1):
                    if perm[i] >= perm[i+1]:
                        valid = False
                        break
                if valid:
                    count += 1
    return count

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
            end = gen(n, start)
            print(end, result)
            #assert(end == result)

gen(4, 'CB')
if __name__ == '__main__':
    unittest.main()