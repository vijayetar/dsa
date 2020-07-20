import pytest
from dsa.challenges.graph_depth_first.graph_depth_first import Graph

def test_graph_import():
    assert Graph.depth_first

def test_graph_depth_first_absent_vertex(graph):
    actual = graph.depth_first("f")
    assert actual == "f is not in graph"

def test_graph_depth_first_absent_vertex(graph):
    actual = graph.depth_first("e")
    assert actual == ['e']

def test_graph_depth_first_absent_vertex(graph):
    actual = graph.depth_first("p")
    assert actual == ['p', 'a', 'n', 'd']

def test_graph_import():
    assert Graph.breadth_first

def test_graph_breadth_first_absent_vertex(graph):
    actual = graph.breadth_first("f")
    assert actual == "f is not in graph"

def test_graph_breadth_first_absent_vertex(graph):
    actual = graph.breadth_first("e")
    assert actual == ['e']

def test_graph_breadth_first_absent_vertex(graph):
    actual = graph.breadth_first("p")
    assert actual == ['p', 'a', 'n', 'd']

def test_breadth_first_3_edges(graph1):
    actual = graph1.breadth_first("p")
    assert actual == ['p', 'n', 'o', 'e']

def test_breadth_first_one_edge(graph1):
    actual = graph1.breadth_first("e")
    assert actual == ['e', 'p', 'n', 'o']

def test_breadth_traversal_island(graph1):
    actual = graph1.breadth_first("z")
    assert actual == ['z']

@pytest.fixture
def graph():
    graph=Graph()
    graph.add_vertex("p")
    graph.add_vertex("a")
    graph.add_vertex("n")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_edge("p","a")
    graph.add_edge("a","n")
    graph.add_edge("n", "d")
    graph.add_edge("a", "d")
    return graph

@pytest.fixture
def graph1():
    graph1= Graph()
    graph1.add_vertex("p")
    graph1.add_vertex("o")
    graph1.add_vertex("n")
    graph1.add_vertex("e")
    graph1.add_vertex("z")
    graph1.add_edge("p", "n", 9)
    graph1.add_edge("p", "o")
    graph1.add_edge("p", "e")
    graph1.add_edge("n", "o")
    return graph1
