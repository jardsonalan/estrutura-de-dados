import time

# Inserção Ordenada
def insertion(list: list[int], index: int) -> list[int]:
    # NOTE: Modifiquei o for para ele percorrer do index até 0
    for item in range(index, 0, -1):
        if list[item] < list[item-1]: # Verifica se o item atual é menor que o item que está a sua frente
            aux = list[item] # Variável auxiliar que armazena o item atual
            list[item] = list[item-1] # O item atual é trocado pelo item a sua frente
            list[item-1] = aux # O item atual, que está armazenado na variável auxiliar, percorre uma posição para frente

    # Retorna a lista ordenada
    return list

# Insertion Sort
def insertion_sort(list: list[int]) -> list[int]:
    index = 1 # Variável responsável por armazenar a quantidade de passos do laço
    while (index < len(list)): # Condição de parada
        list = insertion(list, index) # A lista irá receber uma nova lista até que ela esteja totalmente ordenada
        index += 1 # Acrescenta mais 1 a cada passo que o laço fizer

    # Retorna a lista ordenada, após a condição do laço não ser mais verdadeira
    return list

# Shell Sort
def shell_sort(list: list[int]) -> list[int]:
    # Divide o tamanho da lista pela metade, utilizando uma divisão inteira, para pegar o intervalo da operação
    gap = len(list) // 2
    # Verifica se o gap é maior que 0
    while gap > 0:
        # Insertion
        # Utiliza um for in range para percorrer o tamanho da lista
        for i in range(len(list)):
            # Armazena o valor atual da lista
            current_value = list[i]
            # Armazena a posição atual que a lista está sendo percorrida
            index = i

            # Verifica se o valor da posição atual é maior, ou igual, que o intervalo da operação
            # E verifica se um elemento, que está a uma certa distância, é maior que o atual
            while index >= gap and list[index - gap] > current_value:
                # Operação que executa a troca dos elementos
                # A posição atual recebe o valor da posição anterior (com a distância gap), se ele for maior
                list[index] = list[index - gap]
                # O valor da posição anterior (com a distância gap), recebe o valor atual que está armazenado na váriavel (current_value)
                list[index - gap] = current_value
                # Move o índice para trás, para a próxima posição a ser comparada
                index -= gap

        # A cada operação divide o gap pela metade, utilizando uma divisão inteira
        gap //= 2

    return list

lista = [i for i in range(10001)]

# Verificação do Insertion Sort
tempo_inicial_insertion_sort = time.time()
insertion_sort(lista)
tempo_final_insertion_sort = time.time()
tempo_de_execucao_insertion_sort = tempo_final_insertion_sort - tempo_inicial_insertion_sort
print(f'Insertion Sort: {tempo_de_execucao_insertion_sort} segundos')

# Verificação do Shell Sort
tempo_inicial_shell_sort = time.time()
shell_sort(lista)
tempo_final_shell_sort = time.time()
tempo_de_execucao_shell_sort = tempo_final_shell_sort - tempo_inicial_shell_sort
print(f'Shell Sort: {tempo_de_execucao_shell_sort} segundos')
