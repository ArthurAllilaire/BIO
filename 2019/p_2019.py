import math
def gen_pali(num, len_original):
    """Takes in the first half of a num (int or str) and len of original num and generates the pali returns int"""
    n = str(num)
    middle = math.floor(len_original/2)
    return int(n + n[:middle][::-1])



def smallestPaliAbove(n):
    """Returns the smallest Palindrome above n (int)"""
    #Need to get the first half of the number
    #Get middle 
    n = str(n)
    middle = math.ceil(len(n)/2)
    middle = n[:middle]
    #Try smallest pali as middle repeated
    pali = gen_pali(int(middle), len(n))
    if pali > int(n):
        return pali
    else:
        #for 9
        new_middle = str(int(middle) + 1)
        n_len = len(n)
        if len(new_middle) > len(n):
            new_middle = new_middle[:-1]
            n_len += 1
        return gen_pali(new_middle, n_len)
    #Otherwise return 1 more than middle repeated

    #Return the pali of that
def isPali(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            return False
    return True
#SMALL TESTS FOR 1A
#print(gen_pali(123, 6))
print(smallestPaliAbove(9))
import unittest
class TestPali(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
        (9876543219123456789, 9876543220223456789),
        (5, 6),
        (9, 11),
        (33, 44),
        (84, 88),
        (45653, 45654),
        (36460000, 36466463),
        (24355343, 24366342),
        (123450000, 123454321),
        (234567890, 234575432),
        (678999876, 679000976),
        (99999999999999, 100000000000001),
        (999999999999999, 1000000000000001),
        (123456789000000000, 123456789987654321),
        (987654321123456789, 987654322223456789),
        (1234567890000000000, 1234567890987654321),
        (9876543210123456789, 9876543211123456789),
        (9876543219123456789, 9876543220223456789)]

    def testPaliAbove(self):
        for n, pali in self.cases:
            #print(n, pali, smallestPaliAbove(n))
            assert(smallestPaliAbove(n)== pali)
        
#1A - TESTCASES
# if __name__ == '__main__':
#     unittest.main()

#1b -> would be from 20 9's to 1 lower difference of 1.1*10^10
#1c -> 1 and 99999 good guess - 9031
def not_sum(n):
    """Get all palindromes below n"""
    palis = set()
    possibilties = set()
    for i in range(n+1):
        if isPali(i):
            palis.add(i)   
        else:
            possibilties.add(i)
    import itertools
    for nums in itertools.combinations(palis, 2):
        sum = nums[0] + nums[1]
        try:
            possibilties.remove(sum)
        except KeyError:
            continue
    print(possibilties)
    return len(possibilties)
            
#print(not_sum(99999)) #-> 9031 but answers say 9030 no idea where I have gone wrong? Helpppp
