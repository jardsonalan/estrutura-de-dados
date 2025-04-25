import math

# Shell Sort
def shell_sort(list: list[int]) -> list[int]:
    # Divide o tamanho da lista pela metade, utilizando uma divisão inteira, para pegar o intervalo da operação
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

    return list

lista_desordenada = [3, 1, 5, 10, 15, 90, 2, 23, 8]
print("Lista Desordenada")
print(lista_desordenada)
lista_ordenada = shell_sort(lista_desordenada)
print("Lista Ordenada")
print(lista_ordenada)