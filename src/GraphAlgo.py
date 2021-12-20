import json
from typing import List

import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph

    def get_graph(self):

        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as file:
                load = json.load(file)
                graph = DiGraph()
            for edge in load["Edges"]:
                graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = graph
            for nodes in load["Nodes"]:
                if "pos" in nodes:
                    pos = tuple(map(float, str(nodes["pos"]).split(",")))
                else:
                    pos = None
                graph.add_node(nodes["id"], pos)
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            file.close()

        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        raise NotImplementedError

    def save_to_json(self, file_name):
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """

    def shortest_path(self, id1, id2):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        raise NotImplementedError

    def TSP(self, node_lst):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """


