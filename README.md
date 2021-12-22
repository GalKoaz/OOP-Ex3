# Object-Oriented Programming Exercise 3


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Content</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#plot-graph">Plot Graph</a></li>
    <li><a href="#algorithms">Algorithms</a></li>
    <li><a href="#code-details">Code Details</a></li>
    <li><a href="#how-to-run">How  to run</a></li>
    <li><a href="#languages-and-tools">Languages and Tools</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

----------------

<!-- ABOUT THE PROJECT -->
# About The Project
**_Object-Oriented Programming Exercise 3 - Directed Weighted Graph - python:_**

In this task we actually built data from a weighted and directed graph in Python, the implementation includes a class of graph as well as a class of algorithms on graphs. The center is to use your previous implementation (of [task 2](https://github.com/GalKoaz/OOP-Ex2)) and "translate" it into Python, 
it has come to implement your solution to your previous implementation in java.

"The origins of graph theory are humble, even frivolous :round_pushpin:"


----------------

<!-- Plot Graph -->
### Plot Graph

<p align="center">
<img align="center" src="https://s10.gifyu.com/images/myplot.png"/>
</p>
(For zoom in click on the image)

In this project we were asked to display the graph visually,

we chose to represent the graph using matplotlib  that allows uploading a graph using a JSON file.

----------------
<!-- algorithms -->
## Algorithms

In this project we used a number of algorithms, we will present the algorithms that were implemented in this project.

[Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the shortest path between a and b.
It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited (set to red) when done with neighbors.

[Graph Center](https://en.wikipedia.org/wiki/Graph_center) A graph with central points colored red. These are the three vertices A such that ```d(A, B) ≤ 3``` for all vertices B. Each black vertex is a distance of at least 4 from some other vertex.

[Traveling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) The travelling salesman problem (also called the travelling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an ```NP-hard``` problem in combinatorial optimization, important in theoretical computer science and operations research.

---------

<!-- code-details -->

## Code Details


Unified Modeling Language (UML) :

Click the image for zoom in.


<p align="center">
<img align="center" src="https://s10.gifyu.com/images/UML1a2275cf5dbed2c7.png" />
</p>

As you can see in UML we implement the main Directed Weighted Graph interfaces that with the help of other interfaces and class we can build the whole project.
The interface is implemented
GraphInterface.

We have Class GraphAlgo receives a JSON file and initializes the entire graph using the interfaces mentioned above.
Sends all data to GraphAlgo, so we can build a graph. In the same class there are options for saving a given graph as a JSON file.

The GraphAlgo class contains all the algorithms that can be run on the given graph such as DijkstraAlgorithm, in addition you can find other functions related to solving various problems in directed graphs.

In addition to all the departments and interfaces mentioned above, we have prepared a test folder that checks all the functions that are in the project, from the simplest function to the most complex function and algorithms that appear in the project.

We have prepared a folder for the graphical interface which contains all the departments of the interface we need from the visual graph presentation to the structure and execution of the algorithms within it, the option to delete and add edges and vertices.

---------

<!-- how-to-run -->
# How to run


First, it's important to make sure you clone this project in Pycharm through Terminal.
To be sure:
```
git clone https://github.com/GalKoaz/OOP-Ex3.git
```

In order to run the algorithms, we will do the following:

we choose check function or you can create by yourself and run the main for example:

```
def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()
    
if __name__ == '__main__':
    check0()

```

_**Python Version:**_ ```3.9```

---------


## Languages and Tools

  <div align="center">
  
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"></code>  <code><img height="40" width="70" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/UML_logo.svg"/></code>
 <code><img height="40" width="80" src="https://matplotlib.org/_static/logo2_compressed.svg"/></code>
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png"/></code>
 <code><img height="40" height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
 <code><img height="40" height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png"></code>
  </div>


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)
* [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
* [Git](https://git-scm.com/)
* [Pycharm](https://www.jetbrains.com/pycharm/)
* [Git-scm](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


<!-- CONTACT -->
## Contact <small>[Top▲](object-oriented-programming-exercise-3)</small>


 Gal - [here](https://github.com/GalKoaz/)
 
 Amir - [here](https://github.com/amirg00/)

Project Link: [here](https://github.com/GalKoaz/OOP-Ex3)

___

Copyright © _This Project was created on Dec 21, 2021, by [Gal](https://github.com/GalKoaz/)  & [Amir](https://github.com/amirg00/)_.
