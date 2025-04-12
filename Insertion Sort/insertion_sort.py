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

# Teste
# list1 = [1, 5, 6, 4]
# print('Antes')
# print(list1)

# list2 = insertion(list1, 3)
# print('Depois')
# print(list2)

lista_desordenada = [3,1,5,10,15,90,2]
print("Lista Desordenada")
print(lista_desordenada)
lista_ordenada = insertion_sort(lista_desordenada)
print("Lista Ordenada")
print(lista_ordenada)