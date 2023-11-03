import unittest

from src.main import find_min_depth


class TestFindMinDepth(unittest.TestCase):

    def test_min_depth(self):
        edges = ["1,2", "1,3", "2,4", "2,5", "3,6", "3,7", "4,8", "5,9", "7,10", "7,11", "8,12"]
        self.assertEqual(find_min_depth(1, edges), 3)

if __name__ == '__main__':
    unittest.main()