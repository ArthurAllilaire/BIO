import math
def get_prime_factors_below(n):
    primes = []
    nums = [i for i in range(2,n+1)]
    while nums:
        n = nums.pop(0)
        primes.append(n)
        for i in range(len(nums)-1,-1,-1):
            if (nums[i] / n).is_integer():
                del nums[i]
    return primes

def get_primes_fast(n):
    """Same as above but hopefully faster"""
    p = []
    if n >= 2:
        p.append(2)
    if n >=3:
        p.append(3)
    for i in range(n+1):
        pass
        #if 
    

            
print(get_prime_factors_below(3))
def distinct_factors(n, primes=None):
    """returns prime factors of n"""
    if primes == None:
        primes = get_prime_factors_below(math.floor(n**0.5)+1)
    result = set()
    for i in primes:
        if (n / i).is_integer():
            a = int(n/i)
            a_primes = []
            result.add(i)
            for i in primes:
                if int(a**0.5)+1 >= i:
                    a_primes.append(i)
                else:
                    break
            for j in distinct_factors(a,a_primes):
                result.add(j)
    if len(result) == 0:
        result.add(n)
    return result #Means it is prime

def multiply(lst):
    total = 1
    for i in lst:
        total *= i
    return total

import unittest
class TestPrimes(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (100, 10),
            (101, 101),
            (2, 2),
            (1001, 1001),
            (371293, 13),
            (789774, 789774),
            (999883, 999883),
            (561125, 335),
            (661229, 4379)
        ]
    def testProduct(self):
        for n,result in self.test_cases:
            p = multiply(distinct_factors(n))
            print(p,result)
            assert(p == result)
            

#b -> 10,20,40,50,80,100,160,200,
def print_nums():
    result = []
    for i in range(1,10):
        for j in range(1,5):
            result.append(2**i * 5**j)

    print(sorted(result))


#c -> Could definitely use a cache to make this faster esepcially when generating primes
def most_freq(n):
    """Returns the most frequent product"""
    from collections import Counter
    #Firstly get all the prime factors
    primes = get_prime_factors_below(int(n**0.5)+1)
    print(primes)
    i_primes = []
    c = Counter()
    for i in range(1,n+1):
        while primes and int(i**0.5)+1 >= primes[0]:
            i_primes.append(primes.pop(0))

        p = multiply(distinct_factors(i, i_primes))        
        c.update([p])
    print(c.total())
    print(c[210])
    print(c[2])
    #print(c)

    return c.most_common(10)

print(most_freq(1000000)) # This will take a couple of minutes but should get:[(210, 260), (30, 241), (330, 194), (42, 189), (390, 175), (462, 149), (510, 148), (66, 144), (570, 139), (546, 134)] so 210 is most frequent


# if __name__ == '__main__':
#     print_nums() #-> b
#     unittest.main()
#     n = int(input("Integer: "))
#     print(multiply(distinct_factors(n)))
