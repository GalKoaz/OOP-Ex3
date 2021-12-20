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
        self.assertEqual(self.G1.get_mc(), 15)

        self.G1.add_node(6, (3.5151, 3.515435451, 0.0))
        self.assertEqual(self.G1.v_size(), 7)
        self.assertEqual(self.G1.get_mc(), 16)

        self.G1.add_node(7, (3.5151, 3.515435451, 0.0))
        self.assertEqual(self.G1.v_size(), 8)
        self.assertEqual(self.G1.get_mc(), 17)

        self.G1.remove_node(8)
        self.assertEqual(self.G1.v_size(), 8)
        self.assertEqual(self.G1.get_mc(), 17)

        self.G1.remove_node(3)
        self.assertEqual(self.G1.v_size(), 7)
        self.assertEqual(self.G1.get_mc(), 18)

    def test_e_size(self):
        self.assertEqual(self.G1.e_size(), 9)
        self.assertEqual(self.G1.get_mc(), 15)

        self.G1.add_edge(5, 2, 1.21451)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 16)

        self.G1.add_edge(4, 2, 0.47564)
        self.assertEqual(self.G1.e_size(), 11)
        self.assertEqual(self.G1.get_mc(), 17)

        self.G1.remove_edge(4, 2)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 18)

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
        """
        Tests the in edges of a node.
        :return: None
        """
        """
        >>> E = None
        True  
        """
        E = self.G1.all_in_edges_of_node(2)
        self.assertIsNone(E)
        """
        >>> G = E(v,v3) | v3 ∈ N(v)
        >>> E = {4: 1.2541625654}  
        True
        """
        E = self.G1.all_in_edges_of_node(3)
        E_compare = {4: 1.2541625654}
        self.assertEqual(E, E_compare)
        self.assertEqual(self.G1.get_mc(), 15)

    def test_all_out_edges_of_node(self):
        """
        Tests the in edges out of a certain node.
        :return: None
        """
        """
        >>> G = (V,E)| E(v2) = {5,4,1}
        >>> E = {5: 1.2541625654, 4: 1.2541625654, 1: 1.2541625654}  
        True
        """
        E = self.G1.all_out_edges_of_node(2)
        E_compare = {5: 1.2541625654, 4: 1.2541625654, 1: 1.2541625654}
        self.assertEqual(E, E_compare)
        """
        >>> G = (V,E)| E(v2) = {5,4,1}
        >>> E = {5: 1.2541625654, 1: 1.2541625654}  
        True
        """
        E = self.G1.all_out_edges_of_node(3)
        E_compare = {5: 1.2541625654, 1: 1.2541625654}
        self.assertEqual(E, E_compare)
        self.assertEqual(self.G1.get_mc(), 15)

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

        self.assertEqual(self.G1.e_size(), 9)
        self.assertEqual(self.G1.get_mc(), 15)

        flag = self.G1.add_edge(5, 2, 1.21451)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 16)
        self.assertTrue(flag)

        flag = self.G1.add_edge(4, 2, 0.47564)
        self.assertEqual(self.G1.e_size(), 11)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertTrue(flag)

        flag = self.G1.add_edge(3, 1, 0.47564)  # This edge already exist in G1.
        self.assertEqual(self.G1.e_size(), 11)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertFalse(flag)

    def test_add_node(self):
        self.assertEqual(self.G1.v_size(), 6)
        self.assertEqual(self.G1.get_mc(), 15)

        flag = self.G1.add_node(10, (5.23523, 3.15135, 0.0))
        self.assertEqual(self.G1.v_size(), 7)
        self.assertEqual(self.G1.get_mc(), 16)
        self.assertTrue(flag)

        flag = self.G1.add_node(95, (3.136136, 3.13561, 0.0))
        self.assertEqual(self.G1.v_size(), 8)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertTrue(flag)

    def test_remove_node(self):
        self.assertEqual(self.G1.v_size(), 6)
        self.assertEqual(self.G1.get_mc(), 15)

        flag = self.G1.add_node(6, (5.363, 3.364453, 0.0))
        self.assertEqual(self.G1.v_size(), 7)
        self.assertEqual(self.G1.get_mc(), 16)
        self.assertTrue(flag)

        flag = self.G1.add_node(7, (3.362, 3.23462, 0.0))
        self.assertEqual(self.G1.v_size(), 8)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertTrue(flag)

        self.assertEqual(self.G1.e_size(), 9)
        flag = self.G1.remove_node(10)  # node doesn't exist in graph G1.
        self.assertEqual(self.G1.v_size(), 8)
        self.assertEqual(self.G1.e_size(), 9)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertFalse(flag)

        self.assertEqual(self.G1.e_size(), 9)
        flag = self.G1.remove_node(3)
        self.assertEqual(self.G1.v_size(), 7)
        self.assertEqual(self.G1.e_size(), 6)  # 3 edges related with node 3 removed: {(3,5),(3,1),(4,3)}
        self.assertNotIn(3, self.G1.inEdges)
        self.assertNotIn(3, self.G1.outEdges)
        self.assertNotIn(3, self.G1.outEdges[4])
        self.assertEqual(self.G1.get_mc(), 18)
        self.assertTrue(flag)

    def test_remove_edge(self):
        self.assertEqual(self.G1.get_mc(), 15)
        self.G1.add_edge(0, 4, 3.65846514)
        self.assertEqual(self.G1.e_size(), 10)  # Adding the same edge to see if size changes
        self.assertEqual(self.G1.get_mc(), 16)
        self.G1.add_edge(0, 4, 3.21541)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 16)
        self.assertIsNotNone(self.G1.all_in_edges_of_node(4).get(0))
        self.assertIsNotNone(self.G1.all_out_edges_of_node(0).get(4))

        self.assertEqual(self.G1.e_size(), 9)
        self.assertEqual(self.G1.get_mc(), 15)

        flag = self.G1.add_edge(5, 2, 1.26523)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 16)
        self.assertTrue(flag)

        flag = self.G1.add_edge(4, 2, 0.2623)
        self.assertEqual(self.G1.e_size(), 11)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertTrue(flag)

        flag = self.G1.add_edge(3, 1, 0.26342)  # This edge already exist in G1.
        self.assertEqual(self.G1.e_size(), 11)
        self.assertEqual(self.G1.get_mc(), 17)
        self.assertFalse(flag)

        flag = self.G1.remove_edge(3, 1)
        self.assertEqual(self.G1.e_size(), 10)
        self.assertEqual(self.G1.get_mc(), 18)
        self.assertTrue(flag)

        flag = self.G1.add_edge(3, 1, 0.26342)  # This edge DOES NOT exist in G1.
        self.assertEqual(self.G1.e_size(), 11)
        self.assertEqual(self.G1.get_mc(), 19)
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
