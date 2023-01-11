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

    def run_sim(self, start, n_steps):
        #First go through start one
        s = self.stations[start[1]].next_stop(start[0])
        past = start[1]
        for _ in range(n_steps-1):
            #Need the past station as well
            s=self.stations[s]
            temp = s.name
            s=s.next_stop(past)
            past = temp
        
        return past+s



    def __str__(self) -> str:
        result = ""
        for i in self.junctions:
            print(i)
        return result




        #{Junction("A","E","F","D"), Junction("E","M","N","A"), Junction("F", "N","O","A"), Junction("G", "O","P","B"), Junction("B", "G","H","C")}

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

# R = Rail()
# R.add_flips("GHIJKL")
# print(R.run_sim("AE",100))

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

if __name__ == "__main__":
    unittest.main()