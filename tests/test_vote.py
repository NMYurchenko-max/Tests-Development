import unittest
from tasks.vote import vote


class TestVoteFunction(unittest.TestCase):
    def test_vote(self):
        self.assertEqual(vote([1, 1, 1, 2, 3]), 1)
        self.assertEqual(vote([1, 2, 2, 3, 3, 3]), 3)

    def test_one_element(self):
        self.assertEqual(vote([1]), 1)

    @unittest.expectedFailure
    def test_all_different(self):
        self.assertEqual(vote([1, 2, 3, 4, 5]), None)

    def test_all_same(self):
        self.assertEqual(vote([1, 1, 1, 1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
