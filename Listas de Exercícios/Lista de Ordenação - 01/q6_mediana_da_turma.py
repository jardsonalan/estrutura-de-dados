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
    mediana = 0 # Variável responsável por receber o valor da mediana

    while (index < len(list)): # Condição de parada
        list = insertion(list, index) # A lista irá receber uma nova lista até que ela esteja totalmente ordenada
        index += 1 # Acrescenta mais 1 a cada passo que o laço fizer

    # Verifica se o tamanho da lista é ímpar
    if len(list) % 2 != 0:
        # armazena_mediana: armazena o valor da metade da lista, utilizando uma divisão inteira
        armazena_mediana = len(list) // 2
        # mediana: recebe o valor que está no index da metade da lista
        mediana = list[armazena_mediana]
    # Caso a lista seja de tamanho par
    else:
        # Divide a lista por 2, através de uma divisão inteira, e armazena o valor da metade do tamanho da lista, na variável (elemento)
        elemento = len(list) // 2
        # calcula_mediana: pega o valor que está na metade da lista, através do index, e o valor que está antes dele
        # Faz a soma desses valores e depois divide por 2
        calcular_mediana = (list[elemento] + list[elemento - 1]) / 2
        # mediana: recebe o resultado da operação de calcular_mediana
        mediana = calcular_mediana


    # Retorna a lista ordenada, após a condição do laço não ser mais verdadeira
    # Retorna a mediana da lista
    return list, mediana

lista = [3, 6, 1, 2, 8, 4, 10]
print(f'Lista Ordenada: {insertion_sort(lista)[0]}\nMediana: {insertion_sort(lista)[1]}')