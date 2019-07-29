def bfs(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while queue:
        v = pop(0)
        nodes = graph[v]
        for n in nodes:
            if n not in seen:
                queue.append(n)
                seen.add(node)
        print(v)
