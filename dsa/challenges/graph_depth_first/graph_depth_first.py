from dsa.data_structures.graph.graph import Graph
from dsa.data_structures.stack_and_queues.stack_and_queues import Stack, Queue

def graph_breadth_first(self, vertex):
    if vertex not in self.get_vertices():
        return f"{vertex} is not in graph"

    vertex_queue=Queue()
    visited_list=[vertex]
    vertex_queue.enqueue(vertex)
    while not vertex_queue.isEmpty():
        new_vertex = vertex_queue.peek()
        new_vertex_neighbors = self.get_neighbors(new_vertex)
        counter = 0
        for edge in new_vertex_neighbors:
            vert, wt = edge.split(" ")
            if vert not in visited_list:
                vertex_queue.enqueue(vert)
                visited_list.append(vert)
                counter+=1
        if counter == 0:
            vertex_queue.dequeue()
    return visited_list

def graph_depth_first(self, vertex):
    if vertex not in self.get_vertices():
        return f"{vertex} is not in graph"

    vertex_stack=Stack()
    visited_list=[vertex]
    vertex_stack.push(vertex)
    while not vertex_stack.isEmpty():
        new_vertex = vertex_stack.peek()
        new_vertex_neighbors = self.get_neighbors(new_vertex)
        counter = 0
        for edge in new_vertex_neighbors:
            vert, wt = edge.split(" ")
            if vert not in visited_list:
                vertex_stack.push(vert)
                visited_list.append(vert)
                counter+=1
        if counter == 0:
            vertex_stack.pop()
    return visited_list

Graph.depth_first = graph_depth_first
Graph.breadth_first = graph_breadth_first


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("bananas")
    print(graph.depth_first("apples"))
