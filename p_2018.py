#Problem 1
"""
repayments after
"""
from decimal import *

def repayments(interest, repayment):
    """Start with £100"""
    debt = Decimal(100.00)
    last_debt = debt
    paid = 0
    getcontext().prec = 5
    # getcontext().rounding = ROUND_UP
    counter = 0
    while debt > 0:
        counter += 1
        #Need to add interest
        debt *= Decimal(1 + (interest/100))
        print(debt)
        debt = debt.quantize(Decimal('0.01'), rounding=ROUND_UP)
        print(debt)
        due = debt * Decimal(repayment/100)
        due = due.quantize(Decimal('0.01'), rounding=ROUND_UP)
        if due >= 50:
            paid += due
            debt -= due
        else:
            debt -= 50
            if debt < 0:
                paid += 50 + debt
            else:
                paid += 50
        #Added for part c
        if debt >= last_debt:
            return 0
        last_debt = debt
    print(counter)
    return paid
#1b) 5 months - ran it with extra counter in while loop

#1C
def getMaxRepayment():
    #Just brute foricing it... Don't mind me
    max_paid = 0
    magic_nums = (0,0)
    for i in range(0,100):
        for j in range(0,100):
            paid = repayments(i,j)
            if paid > max_paid:
                magic_nums = (i,j)
                max_paid = paid
    return (magic_nums, max_paid)


#print(repayments(96,49))
#1c) 96% interst and 49% repayment, had to modify original ocde to stop if debt was getting bigger to not be in an infinite loop
#print(getMaxRepayment())

#Q2
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Dials:
    def __init__(self, n):
        self.n = n
        self.dial1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rem_lets = [i for i in self.dial1]
        print(rem_lets)
        self.dial2 = ""
        p1 = 0  #for indexing mismatch
        while len(self.dial2) < 26:
            p1 += n-1 
            p1 = p1 % len(rem_lets)
            self.dial2 += rem_lets.pop(p1)
            
        print(self.dial2[:6])

    def encrypt(self, word):
        """Word between 1 and 8 upper case letters"""
        encrypted = ""
        p1 = 0 #Start pointer at zero
        for char in word:
            i = self.dial1.index(char)
            encrypted += self.dial2[(p1+i)%26]
            p1 += 1
        
        return encrypted

#2A) d = Dials(5)
#print(d.encrypt("ABCD"))
    
#2B) d = Dials(1000000000)
# LKBXIY

#2C) 
# d = Dials(6)
# print(d.encrypt(ALPHA))


# PROBLEM 3
#3A

class SerialNum:
    def __init__(self, n, serial):
        self.n = n
        self.serial = serial
        self.neighbours = {0: [serial]} #depth -> list of serials at this depth
        self.nborset = {serial}

    def get_all_serials(self, justSet=False):
        """Returns all serials, in dictionary with order"""
        i = 0
        while True:
            empty = True
            for j in self.neighbours[i]:
                next_search = self.get_neighbour_serials(j)
                for s in next_search:
                    #If not already in a higher list
                    if s not in self.nborset:
                        empty = False
                        self.nborset.add(s)
                        if self.neighbours.get(i+1, 1) != 1:
                            self.neighbours[i+1].append(s)
                        else:
                            self.neighbours[i+1] = [s]
            if empty:
                if justSet:
                    return self.nborset
                return self.neighbours
            #print(self.neighbours)
            i += 1

    def get_neighbour_serials(self, serial=None):
        if serial == None:
            serial = self.serial
        result = []
        #So now get range between the two
        for i in range(len(serial)-1):
            valid = self.get_range(int(serial[i]), int(serial[i+1]))
            neighbours = set()
            if i > 0:
                neighbours.add(serial[i-1])
            if i < len(serial) - 2:
                neighbours.add(serial[i+2])
            #print(neighbours, valid, neighbours & valid)
            if neighbours & valid: #union
                #Then can swap
                result.append(self.swap(serial, i))
        return result
    
    def get_depth(self):
        serials = self.get_all_serials()
        j = 0
        for i in serials.keys():
            if j < i:
                j = i
        return j

    def swap(self, serial, i):
        #Uses the current self.serial
        return serial[:i] + serial[i+1] + serial[i] + serial[i+2:]

    def greatest_distance(self):
        """Returns the greatest distance between two similar serials"""
        max_depth = self.get_depth()
        for serial in self.nborset:
            S = SerialNum(len(serial), serial)
            n_depth = S.get_depth()
            if n_depth > max_depth:
                max_depth = n_depth
            
        return max_depth

        
    def get_range(self, num1, num2):
        """Returns a set of strings of all numbers in the range"""
        if num1 > num2:
            num2, num1 = num1, num2 #Make sure num1 if smaller
        result = set()
        #print(num1, num2)
        for i in range(num1+1, num2):
            result.add(str(i))

        return result

##MINI TESTS
# S = SerialNum(6, "146235")
# print(S.greatest_distance())
# print(S.get_neighbour_serials("142635"))
# print(S.get_all_serials())

# S2 = SerialNum(6, "461235")
# print(S2.get_depth())

#3B - therefore 7 and 16
# S = SerialNum(6, "326451")
# print(S.greatest_distance())

# S = SerialNum(9, "183654792")
# print(S.greatest_distance())
import itertools
#3C 

def largest_set(n):
    """Gets length of largest set of differnet serial numbers (non-equivalent) that contain numbers 1,2,..,n iwth no repeats"""
    group = 0    
    perms = set()
    for serial in itertools.permutations(range(1,n+1)):
        serial = [str(i) for i in serial]
        serial = "".join(serial)
        perms.add(serial)

    while perms:
        serial = perms.pop()
        S = SerialNum(n, serial)
        equiv_serials = S.get_all_serials(True)
        for s in equiv_serials:
            try:
                perms.remove(s)
            except KeyError:
                continue
        group += 1
    
    return group

# print(largest_set(5)) # 26
# print(largest_set(9)) # 2620


## Tests for 3A
from unittest import TestCase
import unittest
class TestSerialNum(TestCase):
    def setUp(self) -> None:
        self.tests = [
            (6, "461235", 6),
            (6, "412365", 3),
            (9, "123456789", 0),
            (1, "1", 0),
            (3, "132", 1),
            (5, "41235", 3),
            (6, "254631", 5),
            (7, "2756413", 9),
            (7, "7521436", 10),
            (8, "51438672", 8),
            (8, "51432687", 13),
            (9, "547389126", 19)
        ]

    def testDepth(self):
        for num, serial, depth in self.tests:
            S = SerialNum(num, serial)
            assert(S.get_depth() == depth)

#UNCOMMENT THIS FOR TESTS
# if __name__ == '__main__':
#     unittest.main()