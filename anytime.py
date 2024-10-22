import heapq

# Função heurística (estimativa do custo restante até o objetivo)
def heuristic(n, goal):
    heuristic_values = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 2,
        'E': 0  # goal node
    }
    return heuristic_values[n]

# Grafo de exemplo com custos
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1, 'E': 7},
    'D': {'E': 3},
    'E': {}  # goal node
}

# Algoritmo Anytime A*
def anytime_a_star(start, goal, w):
    open_list = []
    heapq.heappush(open_list, (0 + w * heuristic(start, goal), 0, start, []))

    best_solution = None
    best_cost = float('inf')

    while open_list:
        f_score, g_score, current_node, path = heapq.heappop(open_list)
        
        path = path + [current_node]

        if current_node == goal:
            if g_score < best_cost:
                best_solution = path
                best_cost = g_score
                print(f"Solução encontrada: {best_solution} com custo {best_cost}")

        for neighbor, cost in graph[current_node].items():
            new_g_score = g_score + cost
            new_f_score = new_g_score + w * heuristic(neighbor, goal)
            heapq.heappush(open_list, (new_f_score, new_g_score, neighbor, path))

    return best_solution, best_cost

# Executa o algoritmo
start_node = 'A'
goal_node = 'E'
w = 2.0  # Fator de ponderação inicial

solution, cost = anytime_a_star(start_node, goal_node, w)

print(f"Melhor solução final: {solution} com custo {cost}")
