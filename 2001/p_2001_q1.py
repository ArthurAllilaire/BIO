def last_standing(n,w):
    n = list(range(1,n+1))
    p1 = 0
    while len(n) > 1:
        p1 += w-1
        p1 = p1 % len(n)
        n.pop(p1)
    return n

# 1 2 3 4 5 6
import unittest
class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            (6, 4, 5),
            (40, 1, 40),
            (20, 8, 1),
            (37, 19, 27),
            (200, 200, 149),
            (230, 173, 230),
            (555, 444, 31),
            (999, 82, 9),
            (82, 999, 49)
        ]
    def testLast(self):
        for p, rhyme, result in self.cases:
            end = last_standing(p, rhyme)[0]
            print(end, result)
            assert(end == result)

#1A
#print(last_standing(6,4))
# if __name__ == '__main__':
#     unittest.main()

#1b -> 5 10 3 9 4 12 8 7 11 2 6 [1]
#print(last_standing(12,5))

#1c -> 64
def find_lowest(num_p):
    for w in range(1,1000):
        n_r = [1]+list(range(num_p,1,-1))
        n = list(range(1,num_p+1))
        p1 = 0
        removed = []
        while len(n) > 1:
            p1 += w-1
            p1 = p1 % len(n)
            removed.append(n.pop(p1))
            n_r.pop(p1)
        if n == n_r:
            print(removed)
            print(w)
            return n

        


print(find_lowest(100))
# print(last_standing_r(100,50))

 
