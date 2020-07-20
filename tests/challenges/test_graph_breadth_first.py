import pytest
from dsa.challenges.graph_breadth_first.graph_breadth_first import Graph

def test_import():
    assert Graph

def test_breadth_traversal_3_edges(graph):
    actual = graph.breadth_traversal_graph("p")
    assert actual == ['p', 'n', 'o', 'e']

def test_breadth_traversal_one_edge(graph):
    actual = graph.breadth_traversal_graph("e")
    assert actual == ['e', 'p', 'n', 'o']

def test_breadth_traversal_island(graph):
    actual = graph.breadth_traversal_graph("z")
    assert actual == ['z']


@pytest.fixture
def graph():
    graph= Graph()
    graph.add_vertex("p")
    graph.add_vertex("o")
    graph.add_vertex("n")
    graph.add_vertex("e")
    graph.add_vertex("z")
    graph.add_edge("p", "n", 9)
    graph.add_edge("p", "o")
    graph.add_edge("p", "e")
    graph.add_edge("n", "o")
    return graph
