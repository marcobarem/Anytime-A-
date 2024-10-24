import heapq

# Labirinto 10x10
maze = [
    [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
]

# Função heurística (distância de Manhattan)
def heuristic(n, goal):
    (x1, y1) = n
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Função para pegar vizinhos válidos no labirinto
def get_neighbors(node, maze):
    neighbors = []
    x, y = node
    # Movimentos possíveis: cima, baixo, esquerda, direita
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # Verifica se o movimento está dentro dos limites da matriz e não é uma parede
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != 1:
            neighbors.append((new_x, new_y))
    
    return neighbors

# Algoritmo Anytime A*
def anytime_a_star(start, goal, w):
    open_list = []
    heapq.heappush(open_list, (0 + w * heuristic(start, goal), 0, start, []))

    best_solution = None
    best_cost = float('inf')

    while open_list:
        f_score, g_score, current_node, path = heapq.heappop(open_list)
        
        path = path + [current_node]

        # Se o nó atual é o objetivo, verifica se é a melhor solução até agora
        if current_node == goal:
            if g_score < best_cost:
                best_solution = path
                best_cost = g_score
                print(f"Solução encontrada: {best_solution} com custo {best_cost}")

        # Expandir os vizinhos do nó atual
        for neighbor in get_neighbors(current_node, maze):
            new_g_score = g_score + 1  # Cada movimento tem custo 1
            new_f_score = new_g_score + w * heuristic(neighbor, goal)
            heapq.heappush(open_list, (new_f_score, new_g_score, neighbor, path))

    return best_solution, best_cost

# Executa o algoritmo
start_node = (0, 0)  # Ponto inicial (2 no labirinto)
goal_node = (9, 9)   # Ponto final (3 no labirinto)
w = 2.0  # Fator de ponderação inicial

solution, cost = anytime_a_star(start_node, goal_node, w)

print(f"Melhor solução final: {solution} com custo {cost}")
