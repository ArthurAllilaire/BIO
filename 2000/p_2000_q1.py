def password_validator(password):
    #Easiest is check for double letters, double double so on till length of word reached
    #abcdabc - which is 7 - so half is 3
    for i in range(1, len(password)//2 + 1):
        for j in range(len(password)-2*i + 1):
        #i is the length of the window
            w1 = password[j:j+i]
            w2 = password[j+i:j+2*i]
            if w1 == w2:
                print("Rejected")
                return False
    print("Accepted")
    return True
import unittest
class TestPass(unittest.TestCase):
    def setUp(self):
        Accepted = True
        Rejected = False
        self.cases = [
            ("A", Accepted),
            ("LONDON", Accepted),
            ("BIOGRAPHY", Accepted),
            ("APRICOT", Accepted),
            ("AA", Rejected),
            ("QUININE", Rejected),
            ("RINGRING", Rejected),
            ("COMMITTEE", Rejected)
        ]

    def testPassValidator(self):
        for p, result in self.cases:
            assert(password_validator(p) == result)

if __name__ == '__main__':
    unittest.main()
#Not what was asked but pretty cool nonetheless
def longestabc(password, result):
    if password_validator(password) == False:
        #if we get to a point which doesn't pass
        return False
    if len(password) > len(result[0]):
        result[0] = password
    for i in range(len(password)+1):
        for char in ['A', 'B', 'C']:
            new_p = password[:i] + char + password[i:]
            longestabc(new_p, result)
            print(result)
    return result
# CBCACBC -> 7
#Started with ABC and made it through each one
# CABABA
password_validator("")
result = [""]
#longestabc("", result)
print(insert("", "A", 0))