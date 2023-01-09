class Ant:
    def __init__(self, x, y, d) -> None:
        self.removed = False
        self.x = x
        self.y = y
        self.d = d
        self.orientations = ['T','R','B','L']
        self.movements = {
            'T': (0,1),
            'L': (-1,0),
            'R': (1,0),
            'B': (0,-1)
        }
    
    def move(self):
        """Moves one step forward in the current direction"""
        to_add = self.movements[self.d]
        self.x += to_add[0]
        self.y += to_add[1]
        return self.x, self.y

    def rotate(self, square):
        new_index = self.orientations.index(self.d)
        if square:
            new_index += 1 # Turn right
        else:
            new_index -= 1 # Turn left
        new_index = new_index % len(self.orientations)
        self.d = self.orientations[new_index]

    def remove(self):
        self.removed = True
        return self

class Grid:
    def __init__(self) -> None:
        #Landscape is matrix with 11*11 grid - 1 for white and 0 for black
        self.ants = []
        self.landscape = []
        for i in range(11):
            self.landscape.append([])
            for j in range(11):
                self.landscape[i].append(1)

        #print(self.landscape)

    def get_square(self, x, y):
        return self.landscape[y-1][x-1]

    def change(self, x,y):
        self.landscape[y-1][x-1] = self.landscape[y-1][x-1] == False

    def add_ants(self, lst_ants):
        for ant in lst_ants:
            self.ants.append(ant)

    def print_ants(self):
        for ant in self.ants:
            if isinstance(ant, str):
                print(ant)
            else:
                print(ant.x, ant.y, ant.d)

    def move_ants(self):
        to_remove = []
        for ant in self.ants:
            if ant == "Removed":
                continue
            x,y = ant.move()
            if x <=0 or y<= 0 or x>11 or y > 11:
                to_remove.append(ant.remove())
            else:
                #Now move the ant based on square
                square = self.get_square(x,y)
                ant.rotate(square)
                self.change(x,y)

        for ant in to_remove:
            i = self.ants.index(ant)
            self.ants[i] = "Removed"

    def __str__(self) -> str:
        for i in reversed(self.landscape):
            print()
            for j in i:
                if j:
                    print(".", end=" ")
                else:
                    print("*", end=" ")
        return ""

#minitest
# G = Grid()
# A1 = Ant(5,5,'T')
# A2 = Ant(3,9,'B')
# G.add_ants([A1, A2])
# for _ in range(6+1+59):
#     G.move_ants()
#     print(G)
# G.print_ants()
#G.change(11,11)
#print(G)

if __name__ == "__main__":
    G = Grid()
    for i in range(2):
        x,y,d = input().split()
        G.add_ants([Ant(int(x), int(y), d)])
    while True:
        num_moves = int(input())
        if num_moves == -1:
            break
        for _ in range(num_moves):
            G.move_ants()

        print(G)
        G.print_ants()

#B ->