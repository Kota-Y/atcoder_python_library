def create_graph(n: int, l: list) -> list:
    graph = [[] for _ in range(n)]
    for a, b in l:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph