class Graph:
    '''Creates a Graph depicted by an AdjacencyList with key vertex and values as neighboring vertices'''

    def __init__(self):
        self._adjacency_dict = {}

    def add_vertex(self, value):
        '''Adds a new vertex to the graph of value given by the argument'''
        if value in self._adjacency_dict:
            raise ValueError ("value already in the graph")
        new_vertex = Vertex(value)
        self._adjacency_dict[new_vertex.value]= []
        return new_vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''Takes in two vertex arguments and adds a edge to the graph between the start_vertex and end_vertex'''
        if start_vertex not in self._adjacency_dict:
            raise KeyError("start_vertex not in dictionary")
        if end_vertex not in self._adjacency_dict:
            raise KeyError("end_vertex not in dictionary")
        self._adjacency_dict[start_vertex].append(str(Edge(Vertex(end_vertex), weight)))
        self._adjacency_dict[end_vertex].append(str(Edge(Vertex(start_vertex), weight)))

    def get_vertices(self):
        '''
        Returns all of the vertices in the graph as a collection list
        '''
        if not self._adjacency_dict:
            return None
        return [str(i) for i in self._adjacency_dict.keys()]

    def get_neighbors(self, the_key):
        '''
        Takes in a vertex as argument and returns edges with their weights
        '''
        if not self._adjacency_dict:
            return None
        return self._adjacency_dict[the_key]

    def __len__(self):
        '''
        Returns the length of the graph
        '''
        if not self.get_vertices():
            return 0
        return len(self.get_vertices())

    def __str__(self):
        returned_string = ""
        for k,v in self._adjacency_dict.items():
            returned_string+= f"key: {k} --> {v}\n"
        return returned_string

class Vertex:
    ''' Vertex has attribute value'''
    def __init__ (self, value):
        self.value = value
        self.visited = False
    def __str__(self):
        return self.value

class Edge:
    ''' Edge Class with vertex and weight'''
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
    def __str__(self):
        return f"{self.vertex} {str(self.weight)}"

if __name__ == "__main__":
    graph= Graph()
    print(len(graph))
    # graph.add_vertex("apple")
    # graph.add_vertex("bananas")
    # graph.add_vertex("oranges")
    # graph.add_edge("apple", "oranges")
    # print("vertices", graph.get_vertices())
    # print("length", len(graph))
    # graph.add_edge("apple", "bananas")
    # graph.add_edge("oranges", "apple", 4)
    # print(graph)
    # print("get neighbors", graph.get_neighbors("oranges"))
    # print("get neighbors", graph.get_neighbors("apple"))

