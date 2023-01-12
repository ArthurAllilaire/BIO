import itertools
def shortest(side1, side2=[], time=[0]):
    """Assume side 1 is sorted"""
    #print(side1)
    if len(side1) == 2:
        return max(side1)

    min_time = 1000000
    for pair in itertools.combinations(side1,2):
        #print(pair)
        time = max(pair)
        new_s1 = side1.copy()
        new_s2 = side2.copy()
        for p in pair:
            new_s1.remove(p)
            new_s2.append(p)
        min_s2 = min(new_s2)
        new_s2.remove(min_s2)
        new_s1.append(min_s2)
        time += min_s2
        #print(new_s1, new_s2)
        time += shortest(new_s1, new_s2)
        if time < min_time:
            min_time = time

    return min_time

print(shortest([4, 23, 40, 41,80, 90], []))
import unittest
class TestTime(unittest.TestCase):
    def setUp(self) -> None:
        self.testCases = (
            ([4, 23, 40, 41, 80, 90], 252),
        ([1, 6, 8, 19, 20, 30, 40], 101), 
        ([99, 99, 99, 99, 99, 99, 99, 99], 1287), 
        ([1, 20, 38, 39, 95, 96, 97, 98], 375), 
        ([11, 12, 13, 14, 15, 16, 17, 18], 165)
        )
        print(self.testCases)

    def testFunc(self):
        for times, result in self.testCases:
            end = shortest(times)
            print(end,result)
            assert(end == result)

if __name__ == '__main__':
    unittest.main()
#3C -> 