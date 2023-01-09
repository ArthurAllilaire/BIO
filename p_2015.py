# Q1
import math
#Okay a block palindrome

def num_blocks_sub(txt):
    """Returns number of possibilities of block palindromes"""
    # This is the base case
    if len(txt)<=1:
        return 1
    total = 1
    #The middle one does not matter in odd one (so can ignore)
    #Start with the two largest ones possible
    p1 = (len(txt)//2) -1 # bottom pointer
    p2 = math.ceil(len(txt)/2)
    while p1 >= 0:
        #If they work
        if txt[:p1+1] == txt[p2:]:
            #Can be split into two :)
            total += num_blocks_sub(txt[p1+1:p2])

        p1 -= 1
        p2 += 1

    return total

def num_blocks(txt):
    #Have to remove top all the same one
    return num_blocks_sub(txt) -1 


tests = [
    ("BBACBB", 3),
    ("XX", 1),
    ("YZ", 0),
    ("OLYMPIAD", 0),
    ("RACECAR", 3),
    ("KKKKKKK", 7),
    ("BBIIOIIBB", 9),
    ("PPPQQQQPPP", 19),
    ("AAAAAAAAAA", 31),
    ("AABCBAA", "5")
]

#Uncomment to test
# for i,j in tests:
#     print(i, num_blocks(i), j)

#Q2
def is_valid(ships, coords, n=10):
    """Returns true if the ship can be put there, false if not"""
    #Ships is going to be a list of coords of other ships
    for x,y in ships:
        for n_x,n_y in coords:
            if abs(x-n_x) <=1 and abs(y-n_y) <=1:
                return False
    
    for n_x, n_y in coords:
        for i in n_x, n_y:
            if i < 0 or i > n-1:
                return False # OUt of bounds
    return True
        
def gen_coords(r, n, coords):
    result = []
    for i in range(n):
        if r%2 == 0: #Place horizontal to the right
            result.append((coords[0]+i, coords[1]))
        else:
            result.append((coords[0], coords[1]+i))
    return result

def output(coords, r):
    if r % 2 == 0:
        txt = "H"
    else:
        txt = "V"
    print(f"{coords[0]} {coords[1]} {txt}")

def place_ships(a,c,m):
    """Places the 4ship, 2*3 ships, 3*2ship, 4*1 ship"""
    ship_coords = [] # Array of coords of all ships
    ships = [4,3,3,2,2,2,1,1,1,1]
    r = 0
    while ships:
        #On a 10*10 square
        r = (a*r+c)%m # c mod m
        if r < 10:
            y = 0
        else:
            y = int(str(r)[-2])
        coords = (r%10, y)
        r = (a*r + c)%m
        #Need to start with 4 ship
        
        new_ship = gen_coords(r, ships[0], coords)
        #Need to remove ship from ships if valid
        if is_valid(ship_coords,new_ship):
            ship_coords += new_ship
            ships.pop(0)
            output(new_ship[0], r)

    return ship_coords

tests = [
    (10,5,9999, "")
]

for a,b,c,result in tests:
    print(a,b,c)
    print(result)
    print(place_ships(a,b,c))


def possible_perms(a,c,m,r):
    for i in range(30):
        r = (a*r+c)%m
        if i %2 ==0: # Only every 2
            print(r)

# possible_perms(2,3,17,0)
"""
2ai) 
(3, 0)
(4, 0)
(8, 0)
(7, 0)
Used place_ships(2,3,17) and added a print(coords) had to stop infinite loop
c) 18 count where two ships make a square invalid

d)
"""
#All possible permutations:
def all_perms():
    """Grid is 5*5"""
    pos = {1:[], 2:[], 3:[], 4:[]}
    for n in range(1,5):
        for x in range(5):
            for y in range(5):
                for r in [0,1]:
                    coords = gen_coords(r, n, (x,y))
                    #Check if not out of bounds
                    if is_valid([],coords, 5):
                        pos[n].append(coords)
    return pos

def valid_combinations(all_pos, ships=[]):
    
    for pos in all_pos[4]:

    
all_pos = all_perms()
valid_pos = valid_combinations(all_pos)
    

