class Dice:
    def __init__(self, d1, d2) -> None:
        self.d1 = d1
        self.d2 = d2
        self.sum_map = self.gen_sum_map()
        #self.needed = self.generate_needed()

    def gen_sum_map(self):
        self.highest = 0
        result = {}
        for i in self.d1:
            for j in self.d2:
                i,j = int(i), int(j)
                sum = i+j
                if sum > self.highest:
                    self.highest = sum
                if sum in result:
                    result[sum] += 1
                else:
                    result[sum] = 1      
        return result

    def generate_needed(self):
        needed = []
        for sum, tally in self.sum_map.items():
            #Therefore needs to have 5 of 7,6,5,4,3,2,1 and their pair on each one
            pos = []
            for i in range(1,sum):
                pos.append((i, sum-i))
            #For each one shows that we need
            needed.append((pos, tally))
            #Need to start with shortest ones
            needed = sorted(needed, key=lambda x:len(x[0]))

        return needed

    def compatible(self, D2):
        """Checks if both die are still compatible"""
        from collections import Counter
        #Two checks:
        #1. Not too long
        if len(D2.d1) > len(self.d1) or len(D2.d2) > len(self.d2):
            return False
        #2. All sums of d2 are a subset of self
        c1 = Counter(self.sum_map)
        c2 = Counter(D2.sum_map)
        if c2 <= c1: #If c1 includes c1
            return True
        else:
            return False
    def same(self, D2) -> bool:
        """Checks D2 is not itself"""
        samed1 = self.d1 == D2.d2 or self.d1 == D2.d1
        samed2 = self.d2 == D2.d2 or self.d2 == D2.d1
        return samed1 or samed2

    def brute_force(self):
        import itertools
        for i in itertools.combinations_with_replacement(range(1,9), len(self.d1)):
            #print(i)
            result = ""
            for char in i:
                result += str(char)
            for j in itertools.combinations_with_replacement(range(1,9), len(self.d1)):
                resultj = ""
                for char in j:
                    resultj += str(char)
                #print(result, resultj)
                D2 = Dice(result,resultj)
                if self.compatible(D2) and self.same(D2) == False:
                    print(D2)
                    return D2
        return "Impossible"

    def __str__(self) -> str:
        return(f"{self.d1} \n{self.d2}")


#
D = Dice("123456", "123456")
D2 = D.brute_force()
