class Playfair:
    def __init__(self, l, r) -> None:
        """Where l and r are the two words to do the encoding"""
        self.lg = self.create_grid(l, False)
        self.rg = self.create_grid(r, True)

    def create_grid(self, word, rev):
        A = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
        result = []
        for _ in range(5):
            result.append([])
        index = 0
        for char in word:
            try:
                A.remove(char)
                result[index//5].append(char)
                index += 1
            except ValueError:
                continue

        for char in A:
            result[index//5].append(char)
            index += 1

        if rev:
            result = [list(reversed(i)) for i in result]
            return list(reversed(result))

        return result

    def decrypt(self, word):
        result = []
        for i in range(0, len(word), 2):
            result.append(self.get_new_lets(word[i], word[i+1], decrypt=True))
        result = "".join(result)
        if result[-1] == "X":
            return result[:-1]
        return result

    def encrypt(self, word):
        if len(word) % 2: #Odd word
            word += "X"
        result = []
        for i in range(0, len(word), 2):
            result.append(self.get_new_lets(word[i], word[i+1]))
        return "".join(result)

    def get_coords(self, char, grid):
        for i in range(len(grid)):
            if char in grid[i]:
                return [grid[i].index(char),i]

    def get_new_lets(self, char1, char2, decrypt=False):
        if decrypt:
            pass
        c1 = self.get_coords(char1, self.lg)
        c2 = self.get_coords(char2, self.rg)
        if c1[1] == c2[1]:
            #Same row so += 1 to x val
            for c in c1, c2:
                if decrypt:
                    c[0] -= 1
                else:
                    c[0] += 1
                c[0] = c[0]%len(self.lg[0])
        else:
            #Otherwise swap y vals and return coords
            c1_y = c1[1]
            c1 = [c1[0], c2[1]]
            c2 = [c2[0], c1_y]
        return self.get_letters(self.lg, c1) + self.get_letters(self.rg, c2)

    def get_letters(self, grid, *c):
        result = []
        for x,y in c:
            result.append(grid[y][x])
        return "".join(result)

    def __str__(self) -> str:
        for l, r in zip(self.lg, self.rg):
            print(" ".join(l), '\t', " ".join(r))
        return ""

#2A TESTS
P = Playfair("ROMULUS", "REMUS")
print(P)
print(P.encrypt("PLAYFAIR"))
print(P.decrypt("XGTJRO"))
print(P.decrypt("CAOPKGZG"))

#2B -> A could go to: O,B,F,K,W,F,G,R,L,V (9 distinct ways)

#2C -> Can change all the columns (so 25 possiblities - 5*5 as can only be rotated, all still have to be next to the same one so 5 possible rotations for each one 5 rotations on opposite grid), can change all the rows in any order, as long as both change - only thing that matters is the rows match up so 5! ways of arranging 5 distinct objects in a line (120) so 25 * 120 = 3000
if __name__ == '__main__':
    w1 = input()
    w2 = input()
    P = Playfair(w1, w2)
    print(P)
    while True:
        let = input()
        if let == 'E':
            print(P.encrypt(input()))
        elif let == 'D':
            print(P.decrypt(input()))
        elif  let == 'Q':
            break



