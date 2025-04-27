import unittest

from a_heapsort import Competitor, heapsort


class TestHeapSort(unittest.TestCase):
    def setUp(self):
        # Test competitors with different characteristics
        self.comp1 = Competitor("Alice", 5, 100)  # solved=5, penalty=100
        self.comp2 = Competitor("Bob", 3, 150)  # solved=3, penalty=150
        self.comp3 = Competitor("Charlie", 5, 80)  # solved=5, penalty=80
        self.comp4 = Competitor("Dave", 6, 50)  # solved=6, penalty=50
        self.comp5 = Competitor("Eve", 5, 100)  # same as comp1

    def test_empty_list(self):
        self.assertEqual(heapsort([]), [])

    def test_single_competitor(self):
        competitors = [self.comp1]
        self.assertEqual(heapsort(competitors), [self.comp1])

    def test_already_sorted(self):
        competitors = [self.comp4, self.comp1, self.comp2]
        expected = [self.comp4, self.comp1, self.comp2]
        self.assertEqual(heapsort(competitors), expected)

    def test_reverse_sorted(self):
        competitors = [self.comp2, self.comp1, self.comp4]
        expected = [self.comp4, self.comp1, self.comp2]
        self.assertEqual(heapsort(competitors), expected)

    def test_full_sorting_logic(self):
        competitors = [
            self.comp1,  # (5, 100)
            self.comp2,  # (3, 150)
            self.comp3,  # (5, 80)
            self.comp4,  # (6, 50)
            self.comp5,  # (5, 100)
        ]
        expected = [
            self.comp4,  # highest solved (6)
            self.comp3,  # solved=5, lowest penalty (80)
            self.comp1,  # solved=5, penalty=100
            self.comp5,  # same as comp1
            self.comp2,  # lowest solved (3)
        ]
        result = heapsort(competitors)
        self.assertEqual(result, expected)

    def test_duplicate_competitors(self):
        competitors = [self.comp1, self.comp5]  # identical competitors
        expected = [self.comp1, self.comp5]
        self.assertEqual(heapsort(competitors), expected)

    def test_stability(self):
        """Test that equal competitors maintain their relative order"""
        comp_a = Competitor("A", 5, 100)
        comp_b = Competitor("B", 5, 100)
        competitors = [comp_a, comp_b]
        # Since they're equal, order should be preserved
        self.assertEqual(heapsort(competitors), [comp_a, comp_b])

    def test_large_input(self):
        import random

        # Generate 1000 random competitors
        competitors = [
            Competitor(
                f"Comp{i}",
                random.randint(1, 10),  # noqa: S311
                random.randint(50, 200),  # noqa: S311
            )
            for i in range(1000)
        ]
        sorted_competitors = heapsort(competitors)

        # Verify sorted order
        for i in range(len(sorted_competitors) - 1):
            current = sorted_competitors[i]
            next_comp = sorted_competitors[i + 1]

            # Verify either:
            # 1. current has more solved, or
            # 2. same solved but lower penalty, or
            # 3. same solved and penalty but name ordered
            self.assertTrue(
                (current.solved > next_comp.solved)
                or (current.solved == next_comp.solved and current.penalty < next_comp.penalty)
                or (
                    current.solved == next_comp.solved
                    and current.penalty == next_comp.penalty
                    and current.name <= next_comp.name
                ),
            )


if __name__ == "__main__":
    unittest.main()
