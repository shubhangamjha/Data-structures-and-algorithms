def shortest_path(graph, N):
    cost = [0 for _ in range(N)]
    path = [0 for _ in range(N)]
    cost[N-1] = 0
    for i in range(N-2, -1, -1):
        min_cost = float('inf')
        for j in range(i+1, N):
            if graph[i][j] == float('inf'):
                continue
            temp_cost = graph[i][j] + cost[j]
            if temp_cost < min_cost:
                min_cost = temp_cost
                path[i] = j
        cost[i] = min_cost
    return cost, path

graph = [[float('inf'), 1, 2, 5, float('inf'), float('inf'), float('inf'), float('inf')],
         [float('inf'), float('inf'), float('inf'), float('inf'), 4, 11, float('inf'), float('inf')],
         [float('inf'), float('inf'), float('inf'), float('inf'), 9, 5, 16, float('inf')],
         [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf')],
         [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 18],
         [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 13],
         [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2]]

N = len(graph)
cost, path = shortest_path(graph, N)
print("Minimum cost:", cost[0])
print("Path:", end=" ")
i = 0
while i < N:
    print(i, end=" ")
    i = path[i]
print()
