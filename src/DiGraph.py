# ----------------------------------------------------------------------------
# Title:  Directed Weighted Graph - Python
# Author: Amir Gillette, Gal Koaz
# Course: OOP
# ----------------------------------------------------------------------------

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.__node_size = 0
        self.__edge_size = 0
        self.__MC = 0
        self.vertices = {}
        # A dictionary of dictionary for the edges.
        self.inEdges = {}
        self.outEdges = {}

    def v_size(self) -> int:
        return self.__node_size

    def e_size(self) -> int:
        return self.__edge_size

    def get_all_v(self) -> dict:
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """

        :param: id1:

        :return: return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        return self.outEdges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.inEdges.get(id1)

    def get_mc(self) -> int:
        return self.__MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        # if the indices are equivalent, then it couldn't be an edge.
        if id1 == id2:
            return False

        # if one of the nodes doesn't exist, then the method does nothing.
        if id1 not in self.vertices.keys() or id2 not in self.vertices.keys():
            return False

        # if there is already an edge exist we pass (meaning the method does nothing -> RETURN FALSE).
        if id1 in self.inEdges.keys() and id2 in self.inEdges.get(id1):
            return False

        if id1 in self.inEdges.keys():
            self.inEdges[id1][id2] = weight
        else:
            self.inEdges[id1] = {}
            self.inEdges[id1][id2] = weight

        if id2 in self.outEdges.keys():
            self.outEdges[id2][id1] = weight
        else:
            self.outEdges[id2] = {}
            self.outEdges[id2][id1] = weight

        self.__edge_size += 1
        self.__MC += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.vertices.keys():
            self.vertices[node_id] = pos
            self.__MC += 1
            self.__node_size += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.vertices.keys():
            return False
        else:
            self.vertices.pop(node_id)
            if node_id in self.inEdges:
                for key in self.inEdges[node_id].keys():
                    self.remove_edge(node_id, key)
            self.__node_size -= 1
            self.__MC += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.inEdges.keys() and node_id2 in self.inEdges[node_id1].keys():
            self.inEdges[node_id1].pop(node_id2)
            self.outEdges[node_id2].pop(node_id1)
            self.__MC += 1
            self.__edge_size -= 1
        else:
            return False
