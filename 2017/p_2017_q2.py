class Board:
    def __init__(self, p1, m1, p2, m2) -> None:
        """Sets up the board, with two players, nodes and squares"""
        self.nodes = []
        for y in range(6):
            row = []
            for x in range(6):
                row.append(Node(x,y))
            self.nodes.append(row)
        self.edges = set()
        self.players = [(p1,m1),(p2,m2)]
        self.curr = 0
        self.squares = []
        for y in range(5):
            row = []
            for x in range(5):
                s = Square(x,y,0)
                for i in [x,x+1]:
                    for j in [y,y+1]:
                        s.add_nodes(self.nodes[j][i])
                        #Also adds the square to the node
                row.append(s)
            self.squares.append(row)

    def simulate(self,n):
        for i in range(n):
            if i == 39:
                pass
            self.move(i)
        self.result()

    def move(self,j):
        pos, mod = self.players[self.curr]
        pos += mod
        if pos > 36:
            pos -= 36
        n2 = False
        clock = bool(self.curr) == False
        i = 0
        while not n2 and i< 37:
            #Get node that works
            n1 = self.get_node(pos)
            n2 = self.get_neighbour(n1, clock)
            if n2: # Node back
                self.edges.add((n1.coords,n2.coords))
                n1.add_connection(n2)
                #Check for squares
                new_square = self.check_square(n1,n2)
                #Check with edges
            else:
                pos += 1
                if pos > 36:
                    i += 1
                    pos -= 36
        #Update the pos
        self.players[self.curr] = (pos,mod)
        if not new_square:
            self.curr = int(self.curr == 0)#switch player at end#

    def get_squares(self,x,y):
        squares = []
        for i in [y,y-1]:
            for j in [x,x-1]:
                s1 = self.get_xy_square(j,i)
                if s1:
                    squares.append(s1)
        return squares

    def nodes_to_square(self, nodes):
        coords = [n1.coords for n1 in nodes]
        x,y = coords[0]
        s1 = set(self.get_squares(x,y))
        for x,y in coords:
            for s in self.get_squares(x,y):
                s1 = s1.intersection(s)
        return s1.pop()

    def check_square(self, n1, n2):
        """Return True if a new square owned, false otherwise"""
        #To get the same square
        s1 = n1.get_squares()
        s2 = n2.get_squares()
        squares = s1.intersection(s2)
        #Remove all sqaures that are already owned:
        squares = [s for s in squares if s.get_owner() == 0]
        if len(squares) == 0:
            return False # no possible squares
        #Need to check each node to see if connected
        found = False
        for s in squares:
            if s.encircled():
                found = True
                s.set_owner(self.curr + 1)
        return found


    def get_node(self, pos):
        x = (pos-1) % 6
        y = (pos-1) // 6
        return self.nodes[y][x]

    def get_neighbour(self, n1, clock):
        x,y = n1.coords
        add = [(0,-1), (1,0), (0,1), (-1,0)]
        if not clock:
            add = [add[0]] + add[:0:-1]
        for x2,y2 in add:
            n2 = self.get_xy_node(x+x2, y+y2)
            if n2 and n2 not in n1.get_edges():
                return n2
        return False
    
    def get_xy_node(self, x,y):
        if y >= 0 and y < len(self.nodes):
            if x >=0 and x < len(self.nodes[0]):
                return self.nodes[y][x]
        return False

    def get_xy_square(self, x,y):
        if y >= 0 and y < len(self.squares):
            if x >=0 and x < len(self.squares[0]):
                return self.squares[y][x]
        return False

    def result(self):
        markers = ["*", "X","O"]
        t_1 = 0
        t_2 = 0
        for row in self.squares:
            result = []
            for square in row:
                owner = square.get_owner()
                if owner == 1:
                    t_1 += 1
                elif owner == 2:
                    t_2 += 1
                result.append(markers[owner])

            result = " ".join(result)
            print(result)
        print(t_1, t_2)

           
class Node:
    def __init__(self, x, y) -> None:
        self.edges = set() #Other nodes its connected to
        self.num = x + y*6 + 1
        self.coords = (x,y)
        self.squares = set()

    def get_edges(self):
        return self.edges

    def add_connection(self, n2):
        self.edges.add(n2)
        n2.edges.add(self)

    def add_square(self, s):
        self.squares.add(s)

    def get_squares(self):
        return self.squares

    def __str__(self):
        return(f"{self.coords}")

class Square:
    def __init__(self,x,y,won) -> None:
        self.x = x
        self.y = y
        self.won = won
        self.nodes = set()

    def add_nodes(self, n1):
        self.nodes.add(n1)
        n1.add_square(self)
    def set_owner(self,n):
        self.won = n
    def encircled(self):
        #Each node has to be connected to two other nodes
        for n in self.nodes:
            in_common = n.get_edges().intersection(self.nodes)
            if len(in_common) < 2:
                return False
        return True
    def get_owner(self):
        return self.won



if __name__ == '__main__': 
    # p1,m1,p2,m2,t = (4,10,14,23, 47) 
    p1,m1,p2,m2,t = [int(x) for x in input().split()]
    B = Board(p1,m1,p2,m2)
    B.simulate(t)