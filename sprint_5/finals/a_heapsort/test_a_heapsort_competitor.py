import unittest
from a_heapsort import Competitor


class TestCompetitor(unittest.TestCase):
    def setUp(self):
        # Test competitors
        self.high_score = Competitor("High", 5, 50)  # Highest solved, mid penalty
        self.mid_score = Competitor("Mid", 5, 100)  # Same solved, higher penalty
        self.low_score = Competitor("Low", 4, 50)  # Lower solved, same penalty
        self.low_score_alt = Competitor("ZLow", 4, 50)  # Same stats, different name
        self.high_copy = Competitor("High", 5, 50)  # Equal to high_score

    # Equality tests
    def test_equality(self):
        self.assertTrue(self.high_score == self.high_copy)
        self.assertFalse(self.high_score == self.mid_score)
        self.assertTrue(self.high_score != self.mid_score)
        self.assertFalse(self.high_score != self.high_copy)

    # Less than tests
    def test_less_than(self):
        # Solved dominates (more solved = greater)
        self.assertTrue(self.low_score < self.high_score)
        self.assertFalse(self.high_score < self.low_score)

        # Penalty breaks tie (lower penalty = greater)
        self.assertTrue(self.mid_score < self.high_score)  # 100 > 50
        self.assertFalse(self.high_score < self.mid_score)

        # Name breaks further tie (reverse alphabetical)
        self.assertTrue(self.low_score_alt < self.low_score)  # 'Z' > 'L'
        self.assertFalse(self.low_score < self.low_score_alt)

    # Greater than tests
    def test_greater_than(self):
        # Solved dominates
        self.assertTrue(self.high_score > self.low_score)
        self.assertFalse(self.low_score > self.high_score)

        # Penalty breaks tie
        self.assertTrue(self.high_score > self.mid_score)  # 50 < 100
        self.assertFalse(self.mid_score > self.high_score)

        # Name breaks further tie
        self.assertTrue(self.low_score > self.low_score_alt)
        self.assertFalse(self.low_score_alt > self.low_score)

    # Less than or equal tests
    def test_less_or_equal(self):
        self.assertTrue(self.low_score <= self.high_score)
        self.assertTrue(self.mid_score <= self.high_score)
        self.assertTrue(self.low_score_alt <= self.low_score)
        self.assertTrue(self.high_score <= self.high_copy)  # Equal case
        self.assertFalse(self.high_score <= self.mid_score)

    # Greater than or equal tests
    def test_greater_or_equal(self):
        self.assertTrue(self.high_score >= self.low_score)
        self.assertTrue(self.high_score >= self.mid_score)
        self.assertTrue(self.low_score >= self.low_score_alt)
        self.assertTrue(self.high_score >= self.high_copy)  # Equal case
        self.assertFalse(self.mid_score >= self.high_score)

    # Edge cases
    def test_identical_comparisons(self):
        self.assertFalse(self.high_score < self.high_copy)
        self.assertFalse(self.high_score > self.high_copy)
        self.assertTrue(self.high_score <= self.high_copy)
        self.assertTrue(self.high_score >= self.high_copy)
        self.assertTrue(self.high_score == self.high_copy)
        self.assertFalse(self.high_score != self.high_copy)


if __name__ == "__main__":
    unittest.main()
