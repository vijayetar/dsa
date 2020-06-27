class Graph:
    '''Creates a Graph depicted by an AdjacencyList with key vertex and values as neighboring vertices'''

    def __init__(self):
        self._adjacency_dict = {}

    def add_vertex(self, value):
        '''Adds a new vertex to the graph of value given by the argument'''
        new_vertex = Vertex(value)
        self._adjacency_dict[value]= []
        return new_vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''Takes in two vertex arguments and adds a edge to the graph between the start_vertex and end_vertex'''
        if not isinstance(start_vertex, Vertex):
            raise ValueError ("Please add vertex to the graph first")
        if start_vertex not in self._adjacency_dict:
            raise KeyError ("Start Vertex not in the the dict")
        if end_vertex not in self._adjacency_dict:
            raise KeyError ("End Vertex not in the the dict")
        self._adjacency_dict[start_vertex].append(end_vertex.value)
        self._adjacency_dict[end_vertex].append(start_vertex.value)

    def __str__(self):
        for k,v in self._adjacency_dict.items():
            print("key: ",k, "--> value: ",v)




class Vertex:
    ''' Vertex has attribute value'''
    def __init__ (self, value):
        self.value = str(value)
    def __str__(self):
        return self.value


class Edge:
    pass


if __name__ == "__main__":
    graph= Graph()
    apple = Vertex("apple")
    bananas = Vertex("bananas")
    graph.add_vertex(apple)
    graph.add_vertex(bananas)
    graph.add_edge(apple,bananas)
    print(graph)

