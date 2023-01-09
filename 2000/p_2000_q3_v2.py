def generateDice(self):
    pass

class Iterator:
    def __init__(self, p) -> None:
        self.p = p
        self.len_counters = []
        self.counters = []
        for i in self.p:
            self.counters.append(0)
            self.len_counters.append(len(i))


    def update_counter(self):
        not_finished = False
        for i in range(len(self.counters)-1,0,-1):
            self.counters[i] += 1
            if self.counters[i] == self.len_counters[i]:
                self.counters[i] = 0
            else:
                not_finished = True
                break
        return not_finished


    def __iter__(self):
        while self.update_counter():
            result = []
            for lst, i in zip(self.p, self.counters):
                result.append(lst[i])
            yield(result)


class Dice:
    def __init__(self, d1, d2) -> None:
        self.d1 = d1
        self.d2 = d2
        self.sum_map = self.gen_sum_map()
        self.needed = self.generate_needed()

    def gen_sum_map(self):
        result = {}
        for i in self.d1:
            for j in self.d2:
                i,j = int(i), int(j)
                sum = i+j
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

    def add(self, pos):
        from collections import Counter
        d1 = Counter(self.d1)
        d2 = Counter(self.d2)
        num1 = Counter()
        num2 = Counter()
        for n1, n2 in pos:
            num1.update(str(n1))
            num2.update(str(n2))

        d1r = []
        d2r = []
        for c,d,die in zip([num1,num2], [d1,d2], [d1r,d2r]):
            c.subtract(d)
            +c
            for num, freq in c.items():
                die.append(num*freq)
        self.d1 += "".join(d1r)
        self.d2 += "".join(d2r)
            
    def copy(self):
        return Dice(self.d1, self.d2)

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
    def not_same(self, D2) -> bool:
        """Checks D2 is not itself"""
        samed1 = self.d1 == D2.d2 or self.d1 == D2.d1
        samed2 = self.d2 == D2.d2 or self.d2 == D2.d1
        return samed1 or samed2

    def brute_force(self):
        import itertools
        posibilities = []
        for i in self.needed:
            pairs, tally = i
            posibilities.append([])
            for pos in itertools.combinations_with_replacement(pairs, tally):
                posibilities[-1].append(pos)

        #To pick one from each one
        pos = Iterator(posibilities)
        for i in pos:
            #print(i)
            d = Dice("","")
            for pairs in i:
                d.add(pairs)
            #print(d)
            if self.compatible(d):
                return d

        #print(posibilities)


    def generate_dice(self, d2=None, i=0):
        import itertools
        if d2 == None:
            d2 = Dice("","")
        print(d2)
        if i == 0:
            print(d2)
            if self.compatible(d2) and self.not_same(d2):
                return d2
            else:
                return None
        pairs, tally = self.needed[i]
        for pos in itertools.combinations_with_replacement(pairs, tally):
            new_d = d2.copy()
            new_d.add(pos)
            if self.compatible(new_d):
                new_d = self.generate_dice(new_d, i-1)
                if new_d:
                    return new_d
        return None

    def __str__(self) -> str:
        return(f"{self.d1} \n{self.d2}")




# D = Dice("","")
# D.add(((1, 1),))
# print(D)




D = Dice("241356", "642315")
print(D.needed)
print(D.brute_force())
#print(D.generate_dice(Dice("",""),len(D.needed)-1))