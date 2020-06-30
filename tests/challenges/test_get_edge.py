import pytest
from dsa.challenges.get_edge.get_edge import get_direct_route
from dsa.data_structures.graph.graph import Graph

def test_get_direct_route_absent_origin(graph):
    actual = get_direct_route(graph, "testing","Narnia")
    expected = "testing is not in graph"
    assert actual == expected

def test_get_direct_route_absent_destination(graph):
    actual = get_direct_route(graph, "Pandora","testing")
    expected = "testing is not in graph"
    assert actual == expected

def test_get_direct_route_one_destination(graph):
    actual = get_direct_route(graph, "Pandora","Narnia")
    expected = "['Pandora', 'Narnia']   True $45"
    assert actual == expected

def test_get_direct_route_reverse_destination(graph):
    actual = get_direct_route(graph, "Narnia", "Pandora")
    expected = "['Narnia', 'Pandora']   True $45"
    assert actual == expected


@pytest.fixture
def graph():
    graph = Graph()
    graph.add_vertex("Pandora")
    graph.add_vertex("Narnia")
    graph.add_vertex("Arendelle")
    graph.add_edge("Pandora", "Narnia",45)
    graph.add_edge("Pandora", "Arendelle",99)
    return graph
