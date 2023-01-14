class Rail:
    def __init__(self) -> None:
        self.j = [["A", "B", "C", "D"], ["E", "F", "G", "H", "I", "J", "K", "L"], ["M", "N", "O", "P", "Q", "R", "S", "T"],["U", "V", "W", "X"]]
        self.extra = [("A", "D"), ("B", "C"), ("U", "V"), ("W", "X")]
        self.junctions = set()
        p1 = 0
        for s in self.j[0]:
            self.junctions.add(Junction(s,self.j[1][p1], self.j[1][p1+1], ""))
            p1 += 2

        p1 = 0
        p2 = 0
        for s in self.j[1]:
            self.junctions.add(Junction(s,self.j[2][p1], self.j[2][(p1+1)%len(self.j[1])], self.j[0][p2//2]))
            p2 += 1
            p1 += 1
        p1 = -1
        p2 = 0
        for s in self.j[2]:
            self.junctions.add(Junction(s, self.j[1][p1], self.j[1][p1+1], self.j[3][p2//2]))
            p2 += 1
            p1 += 1

        p1 = 0
        for s in self.j[-1]:
            self.junctions.add(Junction(s,self.j[2][p1], self.j[2][p1+1], ""))
            p1 += 2
        self.stations = {}
        for j in self.junctions:
            for j1, j2 in self.extra:
                if j.name == j1:
                    j.update_up(j2)
                elif j.name == j2:
                    j.update_up(j1)
            self.stations[j.name] = j
            
    def add_flips(self, juncs):
        for j in juncs:
            self.stations[j].set_flips(True)

    def reset(self):
        for j in self.junctions:
            j.p1 = 0
            j.lazy = True
        return True 

    def move(self, start):
        """Returns the just the next junction and updates the state of the Rail"""
        pass
    def run_sim(self, start, n_steps):
        #First go through start one
        s = self.stations[start[1]].next_stop(start[0])
        past = start[1]
        for _ in range(n_steps-1):
            #Need the past station as well
            #print(past,s)# for 2b
            s=self.stations[s]
            temp = s.name
            s=s.next_stop(past)
            past = temp
        
        return past+s

    def get_safety(self):
        starts = set()
        for j in self.junctions:
            starts.add(j.name+j.up)
            for i in range(2):
                starts.add(j.name+j.down[i])
        total = 0
        moves = 100
        #starts = {'AD', 'EA', 'TK'}
        for i in starts:
            for j in starts:
                self.reset()
                add = True
                n_i = i
                n_j = j
                for _ in range(moves):
                    if n_i[1]==n_j[1] or (n_i[0] == n_j[1] and n_i[1]==n_j[0]):
                        add = False
                        break
                    n_i = self.run_sim(n_i,1)
                    n_j = self.run_sim(n_j,1)
                if add:
                    total += 1

        return total


        #Stop if they have the same junction (or they have just switched junciton (used to be A now D ad vice versa))

    def __str__(self) -> str:
        result = ""
        for i in self.junctions:
            print(i)
        return result

class Junction:
    def __init__(self, name, left, right, straight) -> None:
        self.name = name
        self.p1 = 0
        self.down = [left, right]
        self.up = straight
        self.lazy = True #Could be 'F' for flipflop

    def set_flips(self, b=True):
        if b:
            self.lazy = False

    def update_up(self, up):
        self.up = up

    def next_stop(self, past):
        if past == self.up:
            s = self.down[self.p1]
            if self.lazy:
                pass 
            else:
                #Change it to opposite
                self.p1 = int(self.p1 == 0)
            return s

        s = self.up
        if self.lazy:
            self.p1 = self.down.index(past)
        return s
        
    def __str__(self) -> str:
        return f"{self.up} - {self.name} - {self.down[0]} or {self.down[1]}"

#2B -> V->U U->M M->L L->D D->A A->E E->M M->U U->V V->P 
#R = Rail()
#R.add_flips("GHIJKL")
#print(R.run_sim("PV",100))
#

#2c
"""
There is no way to narrow it down to a single station, just find the pattern as to which level it will be on, 10**18 is divisible by 8 so same position as stratin (in terms of row and facing)
"""
#2d
# R = Rail()
# total = R.get_safety()
# print(total)
import unittest
class TestRail(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("GHIJKL","AE",6,"FA"),
            ("ABCDEF","HP",1,"PV"),
            ("ABCDEF","PH",1,"HB"),
            ("AEFMNO","DK",13,"SK"),
            ("AEFMNS","DK",13,"SJ"),
            ("ABCDEF","GO",100,"QI"),
            ("FJLMQU","GO",100,"RJ"),
            ("FDEGNQ","AE",9876,"WQ")
        ]
    def testRail(self):
        for flips, start, n, result in self.test_cases:
            R = Rail()        
            R.add_flips(flips)
            end = R.run_sim(start,n)
            print(end, result)
            assert(end == result)

# if __name__ == "__main__":
#     unittest.main()