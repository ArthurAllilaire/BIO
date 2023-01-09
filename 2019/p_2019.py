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
class Trail:
    def __init__(self, trial_time) -> None:
        self.trial_time = trial_time
        self.trail = []

    def add(self, coords):
        self.trail.append(coords)
        if len(self.trail) > self.trial_time:
            self.trail.pop(0)

    def isin(self, coords):
        return coords in self.trail

    def __str__(self) -> str:
        result = []
        for i in self.trail:
            result.append(str(i))
        return " ".join(result)

class Coords:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __eq__(self, coords2) -> bool:
        if isinstance(coords2, tuple):
            return self.get_x() == coords2[0] and self.get_y() == coords2[1]
        return self.get_y() == coords2.get_y() and self.get_x() == coords2.get_x()

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, coords2):
        return Coords(self.get_x()+coords2.get_x(), self.get_y()+coords2.get_y())

    def __str__(self) -> str:
        return f"({self.get_x()}, {self.get_y()})"

class Facing(Coords):
    def __init__(self, c1):
        self.pos = [Coords(0,1), Coords(-1,0), Coords(0,-1), Coords(1,0)]
        self.facing = self.pos.index(c1)
    def get_x(self):
        return self.pos[self.facing].get_x()

    def get_y(self):
        return self.pos[self.facing].get_y()
        
    def change_direction(self, instruction):
        """Returns the Coords of the new direction"""
        if instruction == 'L':
            self.facing += 1
        if instruction == 'R':
            self.facing -= 1

        self.facing = self.facing % len(self.pos)
        return self.get_facing()

    def get_facing(self):
        return self.pos[self.facing]
#Q2
class Grid:
    def __init__(self, trail, instructions, moves):
        self.trail = Trail(trail) # How long till it dissapears
        self.instructions = instructions #UPPERCASE list of instructions
        self.step = 0
        self.moves = moves #How many moves needed till output current coords
        self.coords = Coords(0,0)
        self.facing = Facing(Coords(0,1))

    def next_step(self, i=None):
        if i == None:
            i = self.instructions[self.step%len(self.instructions)]
        self.facing.change_direction(i)
        next_square = self.facing + self.coords
        if self.trail.isin(next_square):
            return False
        else:
            self.trail.add(next_square)
            #print(self.trail)
            self.coords = next_square
            return True


    def move(self):
        """Returns coordinates of ending position"""
        self.trail.add(self.coords)
        for i in range(self.moves):
            if i == 1006:
                pass
            self.step = i
            if self.next_step() == False:
                #means we've hit the trail
                #So go right three times then give up
                no_sol = True
                for _ in range(3):
                    if self.next_step('R'):
                        no_sol = False
                        break

                if no_sol:
                    print(f"Failure at go {i}")
                    return self.coords

        return self.coords

    
#Q2 A
# explorer = Grid(8, 'FL', 9)
# print(explorer.move())
#TESTCASES
class TestGrid(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            (8, "FL", 2, (-1, 1)),
            (100, "FLF", 591, (9, -6)),
            (39, "LLLRFFF", 50, (1, -1)),
            (100, "LLRR", 5000, (-2500, 0)),
            (10, "LLRFLR", 5000, (-3, -3)),
            (1, "F", 1000, (0, 1000)),
            (100, "L", 1000, (-4, -12)),
            (39, "LRFRRF", 5000, (0, -1)),
            (1, "L", 999, (0, -1)),
            (9, "LLR", 5000, (0, -2)),
            (100, "R", 1000, (0, -12)),
            (10, "FFRFRFFRRR", 100, (1, 1))
            ]
    def testGrid(self):
        for t,i,m,c in self.testCases:
            G = Grid(t,i,m)
            coord = G.move()
            # print(coord, c)
            assert(coord == c)
# if __name__ == '__main__':
#     unittest.main()
# #B
# explorer = Grid(8, 'FL', 16)
# print(explorer.move())
# #(2, -1) (2, 0) (2, 1) (1, 1) (0, 1) (0, 0) (-1, 0) (-1, -1) - trail
# #(-1, -1)Current position
# #C -> 21*21 = 440
# G = Grid(100000, 'L', 440)
# print(G.move())
# print(G.trail)

#D -> didn't work :(((
G = Grid(1200, 'LLRFFF', 1200)
print(G.move())
import sys
import pygame
from pygame.locals import KEYDOWN, K_q

#CONSTANTS
SCREENSIZE = WIDTH, HEIGHT = 600,400
BLACK = (0,0,0)
GREY = (160,160,160)
#print(G.trail)