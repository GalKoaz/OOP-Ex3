# ----------------------------------------------------------------------------
# Title:  Directed Weighted Graph - Python
# Author: Amir Gillette, Gal Koaz
# Course: OOP
# ----------------------------------------------------------------------------

import unittest
from unittest import TestCase
from DiGraph import DiGraph


class DiGraphTest(TestCase):
    """
       Tests for class: DiGraph
    """

    def setUp(self) -> None:
        self.G1 = DiGraph()
        self.G1.add_node(0, (3.5151, 3.515435451, 0.0))
        self.G1.add_node(1, (3.531351, 3.515435451, 0.0))
        self.G1.add_node(2, (3.714351, 3.515435451, 0.0))
        self.G1.add_node(3, (3.786351, 3.31465651, 0.0))
        self.G1.add_node(4, (3.62243, 3.36212352353, 0.0))
        self.G1.add_node(5, (3.261674, 3.563634232, 0.0))
        self.G1.add_edge(0, 1, 1.2541625654)
        self.G1.add_edge(1, 0, 1.2541625654)
        self.G1.add_edge(2, 5, 1.2541625654)
        self.G1.add_edge(3, 5, 1.2541625654)
        self.G1.add_edge(2, 4, 1.2541625654)
        self.G1.add_edge(3, 1, 1.2541625654)
        self.G1.add_edge(1, 4, 1.2541625654)
        self.G1.add_edge(2, 1, 1.2541625654)
        self.G1.add_edge(4, 3, 1.2541625654)

    def test_v_size(self):
        self.assertEqual(self.G1.v_size(), 6)

    def test_e_size(self):
        self.assertEqual(self.G1.e_size(), 9)
        self.assertEqual(self.G1.get_mc(), 15)

        self.G1.add_edge(5, 2, 1.21451)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 16)

        self.G1.add_edge(5, 2, 1.21451)

        self.G1.add_edge()

        self.G1.add_edge()


        self.G1.remove_edge()

        self.G1.remove_edge()

        self.G1.remove_edge()

        self.assertEqual(True, True)

    def test_get_all_v(self):
        V = self.G1.get_all_v()
        V_compare = {0: (3.5151, 3.515435451, 0.0),
                     1: (3.531351, 3.515435451, 0.0),
                     2: (3.714351, 3.515435451, 0.0),
                     3: (3.786351, 3.31465651, 0.0),
                     4: (3.62243, 3.36212352353, 0.0),
                     5: (3.261674, 3.563634232, 0.0)}
        self.assertEqual(V, V_compare)

    def test_all_in_edges_of_node(self):
        self.assertEqual(True, True)

    def test_all_out_edges_of_node(self):
        self.assertEqual(True, True)

    def test_get_mc(self):
        self.assertEqual(True, True)

    def test_add_edge(self):
        self.assertEqual(self.G1.get_mc(), 15)
        self.G1.add_edge(0, 4, 3.65846514)
        self.assertEqual(self.G1.e_size(), 10)  # Adding the same edge to see if size changes
        self.assertEqual(self.G1.get_mc(), 16)
        self.G1.add_edge(0, 4, 3.21541)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 16)
        self.assertIsNotNone(self.G1.all_in_edges_of_node(4).get(0))
        self.assertIsNotNone(self.G1.all_out_edges_of_node(0).get(4))

    def test_add_node(self):
        self.assertEqual(True, True)

    def test_remove_node(self):
        self.assertEqual(True, True)

    def test_remove_edge(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
