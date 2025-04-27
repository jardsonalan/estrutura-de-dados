import math

# Shell Sort
def shell_sort(list: list[int]) -> list[int]:
    # Divide o tamanho da lista pela metade para pegar o intervalo da operação
    # Utiliza o método ceil, da biblioteca math, para pegar o teto da divisão
    gap = math.ceil(len(list) / 2)

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

    # Retorna a lista ordenada
    return list

def elementos_duplicados(list: list[int]) -> list[int]:
    # Lista que irá armazenar os valores duplicados
    lista_duplicatas = []

    # Serve para percorrer a lista ordenada pelo shell sort
    for i in range(len(shell_sort(list))-1):
        print(list[i], list[i+1]) # Exibe as comparações feitas
        # Verifica se o valor atual é igual ao próximo valor da sequência
        # E verifica se esse valor duplicado ainda não está armazenado na lista de duplicatas
        if list[i] == list[i + 1] not in lista_duplicatas:
            # Armazena o valor duplicado na lista de duplicatas
            lista_duplicatas.append(list[i])

    # Retorna a lista de duplicatas
    return lista_duplicatas

lista = [1, 4, 3, 1, 5, 6, 8, 5]
print(f'Elementos duplicados: {elementos_duplicados(lista)}')
# print(f'Lista Ordenada: {shell_sort(lista)}')