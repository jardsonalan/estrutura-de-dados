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

lista_desordenada = [3,1,5,10,15,90,2]
print("Lista Desordenada")
print(lista_desordenada)
lista_ordenada = shell_sort(lista_desordenada)
print("Lista Ordenada")
print(lista_ordenada)