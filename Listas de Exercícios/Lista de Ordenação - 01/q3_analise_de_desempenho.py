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
    
    # Verifica se o valor do gap é ímpar e adiciona mais 1 no ciclo da operação, para executar todas as rodadas de troca
    if gap % 2 != 0:
        gap += 1

    # Verifica se o gap é maior que 0 e executa o laço
    while gap > 0:
        # Utiliza um for in range para percorrer de 0 até o tamanho da lista, menos o gap
        for index in range(0, len(list) - gap):
            # Variável auxiliar que armazena o valor atual da lista
            aux = list[index]

            # Verifica se o próximo elemento, que está a uma certa distância, é menor que o atual
            if list[index + gap] < aux:
                # Operação que executa a troca dos elementos
                # A posição atual recebe o valor da posição posterior (com a distância gap), se ele for menor
                list[index] = list[index + gap]
                # O valor da posição posterior (com a distância gap), recebe o valor atual que está armazenado na váriavel auxiliar (aux)
                list[index + gap] = aux

        # A cada operação subtrai 1 do gap
        gap -= 1

    return list

# Lista Desordenada - 10000 até 0
lista = [i for i in range(10000, -1, -1)]

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
