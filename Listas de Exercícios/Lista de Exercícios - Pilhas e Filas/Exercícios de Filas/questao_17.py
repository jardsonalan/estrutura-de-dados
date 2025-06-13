from collections import deque

def bfs_labirinto(labirinto, inicio, fim):
    # Lista de movimentos possíveis: cima, baixo, esquerda, direita
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    
    # Matriz para marcar as posições já visitadas
    visitado = [[False] * colunas for _ in range(linhas)]
    
    fila = deque()
    fila.append(inicio)  # Adiciona o ponto inicial na fila
    visitado[inicio[0]][inicio[1]] = True  # Marca como visitado
    
    while fila:
        x, y = fila.popleft()  # Pega a próxima posição da fila
        
        # Se chegou no fim, retorna True (caminho encontrado)
        if (x, y) == fim:
            return True
        
        # Verifica os vizinhos possíveis
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            
            # Confere se o vizinho está dentro dos limites e se é caminho livre (0)
            if 0 <= nx < linhas and 0 <= ny < colunas:
                if not visitado[nx][ny] and labirinto[nx][ny] == 0:
                    fila.append((nx, ny))       # Adiciona vizinho na fila
                    visitado[nx][ny] = True     # Marca vizinho como visitado
    
    # Se esgotou a fila e não encontrou o fim, retorna False
    return False

labirinto = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

inicio = (0, 0)
fim = (2, 2)

if bfs_labirinto(labirinto, inicio, fim):
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado.")
