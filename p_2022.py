encrypted = "ESVNMCW"
decrypted = "ENCRYPT"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(word):
    nums = intoNums(word)
    p1 = 0
    new_nums = []
    while p1 < len(nums)-1:
        new_num = nums[p1] + nums[p1+1] -1
        new_nums.append(new_num%26)
        p1 += 1
    new_nums.append(nums[0])
    print(nums, reversed(new_nums))
    return reversed(new_nums)



# word = "OLYMPIAD"
# counter = 1
# word = encrypt(word)
# while word != "OLYMPIAD":
#     counter += 1
#     word = 
    

def decrypt2(encrypted):
    """This time we're going to use pointers and maybe think from time to time. For example: W = """
    #First convert string to numbers
    nums = intoNums(encrypted)
    p1 = len(nums) -1
    p2 = p1 - 1
    new_nums = []
    while p2 >= 0:
        new_num = nums[p1] - nums[p2] -1
        if new_num < 0:
            new_num += 26

        new_nums.append(new_num%26)
        p1 -= 1
        p2 -= 1
    new_nums.append(nums[0])
    print(nums, reversed(new_nums))
    return reversed(new_nums)


def decrypt(encrypted):
    """
    Takes in the encrypted text and returns decrytped text
    """
    #The last letter (W) was made from actual + C therefore replac actual - W
    decrypted = []
    nums = list(reversed(intoNums(encrypted)))
    for i in range(len(nums)-1):
        d_num = (nums[i] - nums[i+1] -1) % 25
        if d_num < 0:
            d_num += 26
        print(d_num)
        nums[i] = d_num
        decrypted.append(d_num)
        print(nums[i])
    return decrypted
        

def intoNums(encrypted):
    result = []
    for i in encrypted:
        result.append(ALPHA.index(i))
    return result

def intoLets(decrypted):
    result = []
    for i in decrypted:
        result.append(ALPHA[i])
    return "".join(result)

# d_nums = decrypt2(encrypted)
# print(intoLets(d_nums))

# print(intoLets(encrypt(decrypted)))

## PROBLEM 3
parked = "cabd"
def car_prefs(parked):
    """Need to find a - that first car had to have that as its position"""
    occupied = []
    pos = {}
    for i in range(len(parked)):
        car = ALPHA[i].lower()
        spot = parked.index(car) # for every letter in the n first letters find the index its parked in
        pos[car] = [ALPHA[spot]] # Add that car and first possibility
        #Once you have the index need to check all preceding spots till one is unoccupied
        j = 1
        while (spot - j) in occupied:
            pos[car].append(ALPHA[spot-j])
            j += 1

        occupied.append(spot)

    return pos

#Takes in pos and returns the nth posibiltiy in alphabetic order
#Based on the the len should be able to get it - i.e. 
#1,2,3,4 - get the 13th one well - every 4 change the next one by minus one - then every 12 do next one - so 13th is 1,1,3,3
    

class PermMachine:
    """Takes a pos dictionary and can get the nth althabetical permuation"""
    def __init__(self, pos) -> None:
        self.pos = list(pos.items())
        print(self.pos)

    def ntharr(self, n) -> str:
        start_index = [len(place[1]) for place in self.pos]
        for i in range(n-1):
            start_index[-1] -= 1
            start_index = self.validate(start_index)
            print(start_index)

        return self.indexToNum(start_index)

    def indexToNum(self, index):
        result = []
        for i in range(len(index)):
            result.append(self.pos[i][1][index[i]-1])
        return "".join(result)
            


    def validate(self, index, i=1):
        """Checks to make sure no zero, if zero resets based on lenof lists in self.pos, i is how deep into the validation we are"""
        if index[-1] == 0:
            return self.validate(index[:-2] + [(index[-2] - 1)], i+1) + [len(self.pos[-i][1])]
        return index 
        




    

        

prefs = car_prefs(parked)
print(prefs)
prefs = PermMachine(prefs)
print(prefs.ntharr(5))
            
            
