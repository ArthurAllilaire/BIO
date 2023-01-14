from collections import Counter
class Node:
    def __init__(self, n) -> None:
        self.n = n
        self.c = self.get_letters()
        self.connections = set()

    def get_letters(self):
        """Returns Counter object with number of letters for self.num"""
        self.words = [
            "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
        ]
        c = Counter()
        for char in str(self.n):
            c.update(self.words[int(char)])

        return c
            

    def transforms(self, n2):
        """Returns true if can transform to n2 in 5 or less changes"""
        c1 = self.c - n2.c #All the letters c has over
        c2 = n2.c - self.c
        if c1.total() + c2.total() <= 5:
            return True
        return False

    def add_connection(self,n2):
        """Adds connection between nodes to self and n2"""
        self.connections.add(n2)
        n2.connections.add(self)
        return True

class Graph:
    def __init__(self) -> None:
        self.nums = []
        for i in range(1000):
            self.add(Node(i))

    def add(self, n1):
        for n2 in self.nums:
            if n1.transforms(n2):
                n1.add_connection(n2)

        self.nums.append(n1)

    def get_size(self):
        #I know what to do (look below)
        overall_count = Counter()
        # total_seen = set()
        for n1 in self.nums:
            seen = set()
            seen.add(n1)
            queue = [(i,1) for i in n1.connections]
            while queue:
                n,i = queue.pop(0)
                if n in seen:
                    continue
                if i > 6:
                    pass
                seen.add(n)
                # if n not in total_seen:
                overall_count[i] += 1
                for j in n.connections:
                    queue.append((j,i+1))
            # total_seen.add(n1)
        return overall_count

    def get_num_tree(self, n1, n2):
        if isinstance(n1, int):
            n1 = self.nums[n1]
        if isinstance(n2, int):
            n2 = self.nums[n2]
        seen = set()
        seen.add(n1)
        queue = [(i,1) for i in n1.connections]
        while queue:
            n,i = queue.pop(0)
            if n in seen:
                continue
            seen.add(n)
            if n == n2:
                return i
            for j in n.connections:
                queue.append((j,i+1))

#3B -> 15
# G = Graph()
# print(len(G.nums[0].connections)) # 15

#3C -> Counter({3: 174825, 2: 119699, 4: 113937, 5: 44345, 1: 32469, 6: 10886, 7: 1783, 8: 288, 9: 31, 10: 1})
# 669 to 100, 966 to 100, 566 to 100, 666 to 101
# G = Graph()
# count = G.get_size()
# print(count)
# total = 0
# max = 0
# for n,c in count.items():
#     if n > max:
#         max = n
#         total = c
# print(max, total)


#3d -> yes cos you can change every section in groups of 3...
#print(G.nums)
#print(G.get_num_tree(26,61))
import unittest

#Tests
class TestGraph(unittest.TestCase):
    def setUp(self):
        self.testCases = [
    ([(26, 61),(1, 94),(1, 610)], (1,1,2)),
    ([(1, 2),(1, 3),(1, 4)], (1,2,1)),
    ([(14, 543),(5, 75),(71, 713)], (2,1,1)),
    ([(21, 911),(329, 927),(66, 71)], (2,2,3)),
    ([(250, 361),(34, 756),(18, 735)], (3,4,3)),
    ([(77, 383),(48, 677),(232, 471)], (5,4,4)),
    ([(220, 691),(198, 222),(410, 666)], (5,5,6)),
    ([(402, 788),(203, 959),(404, 777)], (6,6,6))
        ]

    def testNums(self):
        G = Graph()
        for pairs, results in self.testCases:
            for coords,n in zip(pairs, results):
                x,y = coords
                end = G.get_num_tree(x,y)
                print(end,n)
                assert(end == n)
# if __name__ == '__main__':
#     unittest.main()
    #Actual code to hand in
    # G = Graph()
    # for _ in range(3):
    #     print(G.get_num_tree(int(input("Number 1: ")), int(input("Number 2: "))))

























# class Number:
#     def __init__(self, n) -> None:
#         self.words = [
#             "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
#         ]
#         self.overall = Counter()
#         self.counts = {}
#         for w in self.words:
#             self.counts[w] = Counter(w)
#             self.overall.update(w)

#         self.n = n
#         self.number = []
#         for char in str(n):
#             self.number.append(self.words[int(char)])
    
#     def transforms(self, n2):
#         """Returns all possible transformations of the number"""
#         #Start with getting letters in current number
#         #This could be done with a graph problem
#         c = Counter()
#         for num in self.number:
#             c.update(num)

#         for i in self.overall.values():
#             pass


        

#         #Now need to check all other numbers, see if we can make them

# class Graph:
#     def __init__(self) -> None:
#         self.nums = []
#         self.connections = []
#         for i in range(1000):
#             self.add(Number(i))

#     def add(self, n1):
#         for n2 in self.nums:
#             if n1.transforms(n2):
#                 self.connections.add((n1,n2))

#         self.nums.append(n1)

#     def get_connection(self, n1, n2):
        



