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
