# -------------------------------------------------------------------------- #
# Title:  Directed Weighted Graph - Python                                   #
# Author: Amir Gillette, Gal Koaz                                            #
# Course: OOP                                                                #
# -------------------------------------------------------------------------- #

import copy
import heapq
import json
import math
import random

import matplotlib.pyplot as plt
from typing import List, Union, Any

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        """
        The Method returns a graph.
        :param graph:
        """
        self.graph = graph

    def get_graph(self) -> DiGraph:
        """
        The method returns a initialized graph.
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        The method loads the given file with the JSON_Operation class.
        Afterwards, the method initialize the graph with the json.
        @returns true if the method successfully read the json file.
        """
        try:
            with open(file_name) as file:
                load = json.load(file)
                self.graph = DiGraph()
                for nodes in load["Nodes"]:
                    if "pos" in nodes:
                        pos = tuple(map(float, str(nodes["pos"]).split(",")))
                    else:
                        pos = None
                    self.graph.add_node(nodes["id"], pos)
                for edge in load["Edges"]:
                    self.graph.add_edge(edge["src"], edge["dest"], edge["w"])

            return True
        except Exception as e:
            print(e)
            return False
        finally:
            file.close()

    def save_to_json(self, file_name) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        he method saves the graph as a json file in the given name.
        @returns true if the method have successfully written the json file
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
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return None

        parent = {id1: -1}
        dist = {}
        for node_id in self.graph.get_all_v():
            dist[node_id] = math.inf
        dist[id1] = 0  # update id1 (src node) to be zero

        heap = [(0, id1)]  # cost from start node,end node
        visited = set()
        while heap:
            weight, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            visited.add(curr)

            if self.graph.all_out_edges_of_node(curr) is None:
                continue
            for key, w in self.graph.all_out_edges_of_node(curr).items():
                if key in visited:
                    continue
                curr_w = dist[curr] + w
                if dist[key] > curr_w:
                    dist[key] = curr_w
                    parent[key] = curr
                heapq.heappush(heap, (dist[key], key))
            if curr == id2:
                break

        path = []
        curr_parent = id2
        if dist[id2] != math.inf:
            while curr_parent != -1:
                path.insert(0, curr_parent)
                curr_parent = parent[curr_parent]

        return dist[id2], path

    def dijkstra(self, id1: int) -> dict[Union[int, Any], Union[Union[float, int], Any]]:
        dist = {}
        for node_id in self.graph.get_all_v():
            dist[node_id] = math.inf
        dist[id1] = 0  # update id1 (src node) to be zero

        heap = [(0, id1)]  # cost from start node,end node
        visited = set()
        while heap:
            (weight, curr) = heapq.heappop(heap)
            if curr in visited:
                continue
            visited.add(curr)
            if self.graph.all_out_edges_of_node(curr) is None:
                continue
            for key, w in self.graph.all_out_edges_of_node(curr).items():
                if key in visited:
                    continue
                curr_w = dist[curr] + w
                if dist[key] > curr_w:
                    dist[key] = curr_w
                    heapq.heappush(heap, (dist[key], key))
        return dist

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) <= 1:
            return node_lst, 0

        cities = node_lst
        ans = []
        src = cities.pop(0)
        dest = cities.pop(1)
        ans += self.shortest_path(src, dest)[1]

        while cities:
            curr_city = cities.pop(0)
            if ans.__contains__(curr_city):
                continue
            last = ans.pop(len(ans) - 1)
            curr = self.shortest_path(last, curr_city)[1]
            ans += curr
        return ans, self.path_cost(node_lst)

    def path_cost(self, node_lst: List[int]) -> float:
        s = 0
        for i in range(0, len(node_lst) - 1):
            s += self.graph.all_out_edges_of_node(node_lst[i])[node_lst[i + 1]]

        return s

    def centerPoint(self) -> (int, float):
        minimum = math.inf
        center = 0
        for v in self.graph.get_all_v():
            maximum = 0
            dist = self.dijkstra(v)
            for d in dist.values():
                if d > maximum:
                    maximum = d
            e = maximum
            if e < minimum:
                minimum = e
                center = v
        return center, minimum

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        We Update all Node with pos if they not have we create a random
        Position, we draw the lines with the arrow of each, and we
        skip if the Edge between the vertex is null.
        @return: None
        """
        for v in self.graph.get_all_v():
            if self.graph.vertices[v] is None:
                self.graph.vertices[v] = (random.uniform(0, 36), random.uniform(0, 33), 0.0)
        for v in self.graph.get_all_v():
            t = self.graph.vertices[v]
            x = t[0]
            y = t[1]
            plt.plot(x, y, color='blue', marker='o', markersize=8, scalex=True, scaley=True)
            if self.graph.all_out_edges_of_node(v) is not None:
                for u in self.graph.all_out_edges_of_node(v):
                    t2 = self.graph.vertices[u]
                    x2 = t2[0]
                    y2 = t2[1]
                    plt.annotate("", xy=(x, y), xytext=(x2, y2),
                                 arrowprops=dict(arrowstyle='- >', color='red', shrinkA=7, shrinkB=7, patchA=None,
                                                 patchB=None))
            plt.text(x, y, str(v), horizontalalignment='center',
                     verticalalignment='center',
                     bbox=dict(facecolor='blue', edgecolor='red', boxstyle='circle, pad=0.15'), color='white')
            plt.title("Directed Weighted Graph by Gal & Amir", fontsize=15)
            plt.xlabel("Nodes Size: ${}$, Edges Size: ${}$".format(self.graph.v_size(), self.graph.e_size()),
                       fontsize=13)
            # (v,u) N(v) = u (v -> u)
        plt.show()
