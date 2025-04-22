# Inserção Ordenada
def insertion(list, index: int) -> list:
    for i in range(index, 0, -1):
        # Verifica se o item atual é menor que o item que está a sua frente
        if list[i][1] < list[i - 1][1]:
            aux = list[i] # Variável auxiliar que armazena o item atual
            list[i] = list[i - 1] # O item atual é trocado pelo item a sua frente
            list[i - 1] = aux # O item atual, que está armazenado na variável auxiliar, percorre uma posição para frente

    # Retorna a lista ordenada
    return list

# Insertion Sort
def insertion_sort(list) -> list:
    index = 1 # Variável responsável por armazenar a quantidade de passos do laço
    while index < len(list): # Condição de parada
        list = insertion(list, index) # A lista irá receber uma nova lista até que ela esteja totalmente ordenada
        index += 1 # Acrescenta mais 1 a cada passo que o laço fizer

    # Retorna a lista ordenada, após a condição do laço não ser mais verdadeira
    return list

lista = [
    ('Ana', 18),
    ('Marcos', 8),
    ('Lucas', 80),
    ('Maria', 8)
]

print(insertion_sort(lista))