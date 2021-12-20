import json
from typing import List

import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        """

        :param graph:
        """
        self.graph = graph

    def get_graph(self) -> DiGraph:
        """

        :return:
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """

        :param file_name:
        :return:
        """
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

    def save_to_json(self, file_name) -> bool:
        """

        :param file_name:
        :return:
        """
        try:
            with open(file_name, "w") as outfile:
                json.dump(self.graph, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4, fp=outfile)
        except Exception as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):


     def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        return None

    def centerPoint(self) -> (int, float):
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
