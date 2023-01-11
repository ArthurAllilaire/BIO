import unittest
from p_2015 import *

class TestPerms(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testNumPerms(self):
        print(num_perms([2,2,2,2]))


if __name__ == "__main__":
    unittest.main()