# ----------------------------------------------------------------------------
# Title:  Directed Weighted Graph - Python
# Author: Amir Gillette, Gal Koaz
# Course: OOP
# ----------------------------------------------------------------------------

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        # __node_size = the graph' nodes amount.
        self.__node_size = 0
        # __edge_size = the graph' edges amount.
        self.__edge_size = 0
        # MC = mode counter of the graph.
        self.__MC = 0
        # vertices dictionary
        self.vertices = {}
        # A dictionary of dictionary for the edges.
        self.inEdges = {}
        # A dictionary of dictionary for the edges.
        self.outEdges = {}

    def v_size(self) -> int:
        """
        The method returns the graph's vertices amount, which is a property,
        updated by other methods.

        Returns
        -------
        :return: __node_size private property = the number of vertices in the graph.
        """
        return self.__node_size

    def e_size(self) -> int:
        """
        The method returns the graph's edges amount, which is a property,
        updated by other methods.

        Returns
        -------
        :return: __edge_size private property = the number of edges in the graph.
        """
        return self.__edge_size

    def get_all_v(self) -> dict:
        """
        The method returns the vertices' dictionary which
        stores the vertices with the positions as values of the key = node_id.

        Returns
        -------
        :return: vertices = vertices' dictionary.
        """
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        Method to have a dictionary of each vertex to point with an arrow
        on id1.

        Parameters
        ----------
        :param: id1: int
            an id of a certain node to look up for his neighbours points on it.

        Returns
        -------
        :return: outEdges dictionary = a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        return self.outEdges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        Method to have a dictionary of all id1's neighbours, means that
        id1 points with an arrow on them.

        Parameters
        ----------
        :param: id1: int
            an id of a certain node to look up for his neighbours.

        Returns
        -------
        :return: inEdges dictionary = a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        return self.inEdges.get(id1)

    def get_mc(self) -> int:
        """
        Method returns the mode counter which is a property,
        updated by other methods, especially in methods that
        change the graph (remove, addition, etc...).

        Returns
        -------
        :return: __MC private property = mode counter of the graph,
        """
        return self.__MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Method first checks for exceptional cases:
                1. if the indices are equivalent, then it couldn't be an edge so do nothing -> RETURN FALSE.
                2. if one of the nodes doesn't exist, then the method does nothing -> RETURN FALSE.
                3. if there is already an edge exist we pass (meaning the method does nothing -> RETURN FALSE).

        If these cases aren't corresponded to our case, then it shall add the
        edge as following:

                1. check if there is an initialized dictionary for the id1 node in the dictionary,
                   then the methods can recognize the key and add the value to the key.
                   O.w. method should initialize a dict for the key, then can add
                   the second key for edge normally.

                2. same procedure for initializing in outEdges dictionary.

        Finally, method updates edge size property, and the mode counter because graph change has made -> RETURN TRUE.

        Parameters
        ----------
        :param: id1: int
            an id of a certain node.

        :param: id2: int
            an id of a certain node.

        :param: weight: float
            Edge weight where edge is (id1 -> id2).

        Returns
        -------
        :return: True if the edge was added successfully, False o.w.
        """

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
        """
        Method first checks for exceptional cases: if the node already exist
        there is no point to override or to add, so do nothing, i.e. -> RETURN FALSE.

        O.W. if the node isn't already exist, we add it to the vertices' dictionary,
        update mode counter to point that a change on the graph has made,
        update the node size because we have added one more to the graph,
        finally, RETURN TRUE.

        Parameters
        ----------
        :param: node_id: int
            an id of a certain node.

        :param: pos: tuple
            a 3-tuple (x,y,z): resembles the node geolocation.

        Returns
        -------
        :return: True if the node was added successfully to the graph, False o.w.
        """
        if node_id not in self.vertices.keys():
            self.vertices[node_id] = pos
            self.__MC += 1
            self.__node_size += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        """
        Method first checks for exceptional cases: if a node isn't exist, then there is nothing
        to remove -> RETURN FALSE

        If these cases aren't corresponded to our case, then it shall add the
        edge as following:

                1. removes each edge related to the node_id vertex, meaning
                that it removes each edge starts or ends in the node. In the meanwhile,
                the method counts how many edges it removed, and updates the edge size
                property.

                Note: the method removes the edges both in inEdges and outEdges dicts.

                2. method removes the vertex from the vertices' dict.

        Finally, method updates node size property, and the mode counter because graph change has made -> RETURN TRUE.

        Parameters
        ----------
        :param: id1: int
            an id of a certain node to be removed.

        Returns
        -------
        :return: True if the node has removed successfully, False o.w.
        """
        if node_id not in self.vertices:
            return False
        else:
            removedE = 0
            self.vertices.pop(node_id)
            if node_id in self.inEdges:
                for key in self.inEdges.keys():
                    if node_id in self.inEdges[key].keys():
                        del self.inEdges[key][node_id]
                        removedE += 1
                removedE += len(self.inEdges.pop(node_id))

            if node_id in self.outEdges:
                for key in self.outEdges.keys():
                    if node_id in self.outEdges[key].keys():
                        del self.outEdges[key][node_id]
                self.outEdges.pop(node_id)
            self.__node_size -= 1
            self.__edge_size -= removedE
            self.__MC += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Method first checks for exceptional cases: if the edge already exist, it
        has nothing -> RETURN FALSE.


        If these cases aren't corresponded to our case, then it shall remove the
        edge as following:

                1. remove edge from inEdges and the equivalent edge in outEdges.

                2. update mode counter and edge size, because we removed an edge.

        Finally, RETURN TRUE.

        Parameters
        ----------
        :param: node_id1: int
            an id of a certain nodes.

        :param: node_id2: int
            an id of a certain node.

        Returns
        -------
        :return: True if the edge has removed successfully, False o.w.
        """
        if node_id1 in self.inEdges.keys() and node_id2 in self.inEdges[node_id1].keys():
            self.inEdges[node_id1].pop(node_id2)
            self.outEdges[node_id2].pop(node_id1)
            self.__MC += 1
            self.__edge_size -= 1
            return True
        else:
            return False

    def __repr__(self) -> str:
        """
        Method returns a string represents the graph's specifications as required.

        EXAMPLE:
              Graph: |V|=4 , |E|=5
              {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}

        Returns
        -------
        :return: the string represents the graph's specifications
        """
        s = "Graph: |V|={node_size} , |E|={edge_size}\n".format(node_size=self.__node_size, edge_size=self.__edge_size)
        cnt = 1
        s += '{'
        for v in self.get_all_v():
            in_dict = self.all_in_edges_of_node(v)
            out_dict = self.all_out_edges_of_node(v)

            in_len = 0
            out_len = 0

            if in_dict is not None:
                in_len = len(in_dict.values())

            if out_dict is not None:
                out_len = len(out_dict.values())

            if cnt is self.__node_size:
                s += "{node_id}: {node_id}: |edges out| {out_len} |edges in| {in_len}".format(node_id=v, out_len=out_len, in_len=in_len)
            else:
                s += "{node_id}: {node_id}: |edges out| {out_len} |edges in| {in_len}, ".format(node_id=v, out_len=out_len, in_len=in_len)

            cnt += 1

        s += '}'

        return s
