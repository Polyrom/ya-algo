import unittest

from a_heapsort import Competitor, MaxHeap


class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.comp1 = Competitor("Alice", 5, 100)
        self.comp2 = Competitor("Bob", 3, 150)
        self.comp3 = Competitor("Charlie", 5, 80)
        self.comp4 = Competitor("Dave", 4, 200)
        self.comp5 = Competitor("Eve", 6, 50)

    def test_initialization(self):
        # Test empty heap
        empty_heap = MaxHeap([])
        self.assertEqual(len(empty_heap.values), 1)

        # Test single element
        single_heap = MaxHeap([self.comp1])
        self.assertEqual(len(single_heap.values), 2)
        self.assertEqual(single_heap.values[1], self.comp1)

        # Test multiple elements
        multi_heap = MaxHeap([self.comp1, self.comp2, self.comp3])
        self.assertEqual(len(multi_heap.values), 4)

    def test_add(self):
        heap = MaxHeap([])
        heap.add(self.comp1)
        self.assertEqual(heap.values[1], self.comp1)
        
        # comp5 has higher solved (6) than comp1 (5)
        heap.add(self.comp5)
        self.assertEqual(heap.values[1], self.comp5)  # comp5 should be root
        self.assertEqual(heap.values[2], self.comp1)

    def test_pop_max(self):
        # Test empty heap
        empty_heap = MaxHeap([])
        self.assertIsNone(empty_heap.pop_max())

        # Test single element
        single_heap = MaxHeap([self.comp1])
        self.assertEqual(single_heap.pop_max(), self.comp1)
        self.assertIsNone(single_heap.pop_max())

        # Test proper ordering
        heap = MaxHeap([self.comp1, self.comp2, self.comp3, self.comp4, self.comp5])
        expected_order = [self.comp5, self.comp3, self.comp1, self.comp4, self.comp2]
        for expected in expected_order:
            self.assertEqual(heap.pop_max(), expected)


    def test_heap_property(self):
        heap = MaxHeap([self.comp1, self.comp2, self.comp3, self.comp4, self.comp5])
        # Verify max-heap property for all parent nodes
        for i in range(1, len(heap.values) // 2 + 1):
            left = 2 * i
            right = 2 * i + 1
            if left < len(heap.values):
                self.assertGreaterEqual(heap.values[i], heap.values[left]) # type: ignore
            if right < len(heap.values):
                self.assertGreaterEqual(heap.values[i], heap.values[right]) # type: ignore

    def test_edge_cases(self):
        # Test adding duplicate competitors
        heap = MaxHeap([self.comp1, self.comp1])
        self.assertEqual(len(heap.values), 3)
        first = heap.pop_max()
        second = heap.pop_max()
        self.assertEqual(first, second)
        self.assertEqual(first, self.comp1)
