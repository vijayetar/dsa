from dsa.data_structures.graph.graph import Graph

def get_direct_route(graph, origin, destination, *args):
    if origin not in graph.get_vertices():
        return f"{origin} is not in graph"
    original = [origin]
    sum = 0
    found = False
    places = []
    places.append(destination)
    places.extend(list(args))
    print(places)
    for destination in places:
        print("this is destintaion", destination)
        if destination not in graph.get_vertices():
            return f"{destination} is not in graph"
        for edge in graph.get_neighbors(origin):
            print("this is edge", edge)
            city, price = edge.split(" ")
            if city == destination:
                found = True
                sum += int(price)
                print("true sum",sum)
                break
            found = False
            sum = 0
        if found:
            print("sum", sum)
            origin = destination
        else:
            break
    places = original + places
    return f"{places}   {found} ${sum}"


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("Pandora")
    graph.add_vertex("Narnia")
    graph.add_vertex("Arendelle")
    graph.add_vertex("Z")
    graph.add_vertex("Zingo")
    graph.add_edge("Z", "Zingo", 100)
    graph.add_edge("Narnia", "Z", 100)
    graph.add_edge("Pandora", "Narnia",100)
    graph.add_edge("Pandora", "Arendelle",100)
    print(get_direct_route(graph, "Pandora", "Narnia", "Z"))
    # print(get_direct_route(graph, "Pandora", "Zak"))
