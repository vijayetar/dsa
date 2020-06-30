import pysnooper
from dsa.data_structures.stack_and_queues.stack_and_queues import Queue

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
        self._adjacency_dict[start_vertex].append(Edge(Vertex(end_vertex), weight))
        self._adjacency_dict[end_vertex].append(Edge(Vertex(start_vertex), weight))

    def add_vertex_and_edge(self, start_vertex, end_vertex, weight = 0):
        if start_vertex not in self._adjacency_dict:
            self.add_vertex(start_vertex)
        elif end_vertex not in self._adjacency_dict:
            self.add_vertex(start_vertex)
        self._adjacency_dict[start_vertex].append(Edge(Vertex(end_vertex), weight))
        self._adjacency_dict[end_vertex].append(Edge(Vertex(start_vertex), weight))

    def get_vertices(self):
        '''
        Returns all of the vertices in the graph as a collection list
        '''
        if not self._adjacency_dict:
            return None
        return [i for i in self._adjacency_dict.keys()]

    def get_neighbors(self, the_key):
        '''
        Takes in a vertex as argument and returns edges with their weights
        '''
        if not self._adjacency_dict:
            return None
        return self._adjacency_dict[the_key]


    @pysnooper.snoop()
    def breadth_traversal_graph(self, node_value):
        '''
        Method to class Graph to do breadth_traversal
        '''
        ## check node_value exists in the graph
        if node_value not in self._adjacency_dict:
            return ("entered vertex does not exist in the graph")
        vertices = []
        breadth = Queue()

        node_vertex = Vertex(node_value)
        breadth.enqueue(node_vertex)
        node_vertex.visited = True
        print("value of inserted vertex", self._adjacency_dict[node_vertex.value])
        vertices.append(node_vertex.value)
        # test = breadth.dequeue()
        # print("testing for visited", test.value)
        while breadth.front:
            front = breadth.dequeue()
            # if front.visited == False:
                # front.visited = True
            print("this si front", front, "this is front.visited", front.visited)
            edges = self.get_neighbors(front.value)
            if edges:
                for edge in edges:
                    if edge.vertex.visited == False:
                        edge.vertex.visited = True
                        breadth.enqueue(edge.vertex)
                if front.value != node_value:
                    vertices.append(front.value)
        return vertices

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
    graph=Graph()
    # graph.add_vertex("node")
    # graph.add_vertex("friend")
    # graph.add_edge("node", "friend")
    # graph.add_vertex("pandora")
    # graph.add_vertex()
    # print(graph.breadth_traversal_graph("node"))
    graph.add_vertex("p")
    graph.add_vertex("o")
    graph.add_vertex("n")
    graph.add_vertex("e")
    graph.add_edge("p", "n", 9)
    graph.add_edge("p", "o")
    graph.add_edge("p", "e")
    graph.add_edge("n", "o")
    print(graph.breadth_traversal_graph("n"))

