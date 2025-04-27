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

            # Verifica se o ano posterior (com o gap) é igual ao ano atual armazenado na variável auxiliar (aux)
            if list[index + gap][6:] == aux[6:]:
                # Verifica se o mês posterior (com o gap) é igual ao mês atual armazenado na variável auxiliar (aux)
                if list[index + gap][3:5] == aux[3:5]:
                    # Verifica se o dia posterior (com o gap) é igual ao dia atual armazenado na variável auxiliar (aux)
                    if list[index + gap][0:2] == aux[0:2]:
                        pass
                    # Se os dias não forem iguais
                    else:
                        # Verifica se o dia posterior (com o gap) é menor que o dia atual armazenado na variável auxiliar (aux)
                        if list[index + gap][0:2] < aux[0:2]:
                            # Operação que executa a troca dos elementos
                            # A posição atual recebe o valor da posição posterior (com a distância gap), se ele for menor
                            list[index] = list[index + gap]
                            # O valor da posição posterior (com a distância gap), recebe o valor atual que está armazenado na váriavel auxiliar (aux)
                            list[index + gap] = aux
                # Se os meses não forem iguais
                else:
                    # Verifica se o mês posterior (com o gap) é menor que o mês atual armazenado na variável auxiliar (aux)
                    if list[index + gap][3:5] < aux[3:5]:
                        # Operação que executa a troca dos elementos
                        # A posição atual recebe o valor da posição posterior (com a distância gap), se ele for menor
                        list[index] = list[index + gap]
                        # O valor da posição posterior (com a distância gap), recebe o valor atual que está armazenado na váriavel auxiliar (aux)
                        list[index + gap] = aux
            # Se os anos não forem iguais
            else:
                # Verifica se o ano posterior (com o gap) é menor que o ano atual armazenado na variável auxiliar (aux)
                if list[index + gap][6:] < aux[6:]:
                    # Operação que executa a troca dos elementos
                    # A posição atual recebe o valor da posição posterior (com a distância gap), se ele for menor
                    list[index] = list[index + gap]
                    # O valor da posição posterior (com a distância gap), recebe o valor atual que está armazenado na váriavel auxiliar (aux)
                    list[index + gap] = aux

        # A cada operação subtrai 1 do gap
        gap -= 1

    return list

datas = ['30/07/2015', '20/10/2001', '01/12/1998', '05/04/2025', '01/01/1999']
print(shell_sort(datas))