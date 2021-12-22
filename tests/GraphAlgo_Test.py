# ----------------------------------------------------------------------------
# Title:  Directed Weighted Graph - Python
# Author: Amir Gillette, Gal Koaz
# Course: OOP
# ----------------------------------------------------------------------------
import copy
import unittest
from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class GraphAlgoTest(TestCase):
    """
        Tests for class: GraphAlgo
    """
    EPSILON = .01

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self) -> None:
        self.G = GraphAlgo()
        self.G.load_from_json("../data/A0.json")
        self.G1 = GraphAlgo()
        self.G1.load_from_json("../data/A1.json")
        self.G2 = GraphAlgo()
        self.G2.load_from_json("../data/A2.json")
        self.G3 = GraphAlgo()
        self.G3.load_from_json("../data/A3.json")
        self.G4 = GraphAlgo()
        self.G4.load_from_json("../data/A4.json")
        self.G5 = GraphAlgo()
        self.G5.load_from_json("../data/A5.json")

    def test_load_from_json(self):
        self.assertEqual(True, False)

    def test_save_to_json(self):
        self.assertEqual(True, False)

    def test_shortest_path(self):
        t = self.G1.shortest_path(0, 3)
        self.assertAlmostEqual(4.09, t[0], delta=self.EPSILON)
        self.assertEqual([0, 1, 2, 3], t[1])
        t = self.G1.shortest_path(3, 12)
        self.assertAlmostEqual(12.086, t[0], delta=self.EPSILON)
        self.assertEqual([3, 2, 6, 7, 8, 9, 10, 11, 12], t[1])
        t = self.G1.shortest_path(4, 2)
        self.assertAlmostEqual(3.281, t[0], delta=self.EPSILON)
        self.assertEqual([4, 3, 2], t[1])

    def test_TSP(self):
        lst = []
        for i in range(0, 17):
            lst.append(i)
        lst_copy = copy.copy(lst)
        t = self.G1.TSP(lst)
        self.assertEqual(lst_copy, t[0])
        self.assertAlmostEqual(22.634, t[1], delta=self.EPSILON)

    def test_path_cost(self):
        lst = []
        for i in range(0, 17):
            lst.append(i)
        self.G.path_cost(lst)

    def test_centerPoint(self):
        t = self.G.centerPoint()
        self.assertEqual(7, t[0])
        self.assertAlmostEqual(6.8, t[1], delta=self.EPSILON)
        t = self.G1.centerPoint()
        self.assertEqual(8, t[0])
        self.assertAlmostEqual(9.925, t[1], delta=self.EPSILON)
        t = self.G2.centerPoint()
        self.assertEqual(0, t[0])
        self.assertAlmostEqual(7.819, t[1], delta=self.EPSILON)
        t = self.G3.centerPoint()
        self.assertEqual(2, t[0])
        self.assertAlmostEqual(8.182, t[1], delta=self.EPSILON)
        t = self.G4.centerPoint()
        self.assertEqual(6, t[0])
        self.assertAlmostEqual(8.071, t[1], delta=self.EPSILON)
        t = self.G5.centerPoint()
        self.assertEqual(40, t[0])
        self.assertAlmostEqual(9.291, t[1], delta=self.EPSILON)


if __name__ == '__main__':
    unittest.main()
