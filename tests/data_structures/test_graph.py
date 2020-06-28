import pytest
from dsa.data_structures.graph.graph import Graph, Edge, Vertex

def test_import():
    assert Graph
    assert Edge
    assert Vertex

def test_empty_graph():
    graph = Graph()
    assert graph.get_vertices() == None
    assert graph.get_neighbors("key") == None
    assert len(graph)==0

def test_create_vertex():
    apples = Vertex("apples")
    actual = isinstance(apples, Vertex)
    expected = True
    assert actual == expected

def test_graph_add_vertex():
    graph=Graph()
    actual = str(graph.add_vertex("apples"))
    expected = "apples"
    assert actual == expected

def test_graph_add_vertex_raise_error():
    graph=Graph()
    graph.add_vertex("apples")
    with pytest.raises(ValueError):
        graph.add_vertex("apples")

def test_add_edge_raise_error():
    graph = Graph()
    graph.add_vertex("apples")
    with pytest.raises(KeyError):
        graph.add_edge("apples", "bananas")

def test_add_edge(graph):
    actual = str(graph)
    expected = "key: apples --> ['bananas 0']\nkey: bananas --> ['apples 0', 'oranges 5']\nkey: oranges --> ['bananas 5']\n"
    assert actual == expected

def test_get_vertices(graph):
    actual = graph.get_vertices()
    expected = ['apples', 'bananas', 'oranges']
    assert actual == expected

def test_len_graph(graph):
    actual = len(graph)
    expected = 3
    assert actual == expected

def test_get_neighbors(graph):
    actual = graph.get_neighbors("oranges")
    expected = ['bananas 5']
    assert actual == expected

def test_get_neighbors_reverse(graph):
    actual = graph.get_neighbors("bananas")
    expected = ['apples 0', 'oranges 5']
    assert actual == expected

@pytest.fixture()
def graph():
    graph=Graph()
    graph.add_vertex("apples")
    graph.add_vertex("bananas")
    graph.add_vertex("oranges")
    graph.add_edge("apples","bananas")
    graph.add_edge("oranges","bananas",5)
    return graph
