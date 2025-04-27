# Inserção Ordenada
def insertion(list: list[str], index: int) -> list[str]:
    # NOTE: Modifiquei o for para ele percorrer do index até 0
    for item in range(index, 0, -1):
        if list[item] < list[item-1]: # Verifica se o item atual é menor que o item que está a sua frente
            aux = list[item] # Variável auxiliar que armazena o item atual
            list[item] = list[item-1] # O item atual é trocado pelo item a sua frente
            list[item-1] = aux # O item atual, que está armazenado na variável auxiliar, percorre uma posição para frente

    # Retorna a lista ordenada
    return list

# Insertion Sort
def insertion_sort(list: list[str]) -> list[str]:
    index = 1 # Variável responsável por armazenar a quantidade de passos do laço
    while (index < len(list)): # Condição de parada
        list = insertion(list, index) # A lista irá receber uma nova lista até que ela esteja totalmente ordenada
        index += 1 # Acrescenta mais 1 a cada passo que o laço fizer

    # Retorna a lista ordenada, após a condição do laço não ser mais verdadeira
    return list

# Função que serve para verificar se duas palavras são anagramas
# Recebe as duas palavras como parâmetros
def verificar_anagrama(palavra1: str, palavra2: str) -> str:
    # palavra1_ordenada: serve para executar a ordenação da primeira palavra utilizando o insertion sort
    # list: serve para separar a palavra1 como elementos de uma lista
    # join: serve para juntar a palavra1, que está separada como elementos de uma lista, após a ordenação
    palavra1_ordenada = ''.join(insertion_sort(list(palavra1)))
    # palavra2_ordenada: serve para executar a ordenação da segunda palavra utilizando o insertion sort
    # list: serve para separar a palavra2 como elementos de uma lista
    # join: serve para juntar a palavra2, que está separada como elementos de uma lista, após a ordenação
    palavra2_ordenada = ''.join(insertion_sort(list(palavra2)))

    # Verifica se após a ordenação a palavra1_ordenada é igual a palavra2_ordenada
    if palavra1_ordenada == palavra2_ordenada:
      # Se for, retorna que as palavras são anagramas
      return f'{palavra1} e {palavra2} são anagramas.'
    
    # Se não for, retorna que as palavras não são anagramas
    return f'{palavra1} e {palavra2} NÃO são anagramas.'

primeira_palavra = 'amor'
segunda_palavra = 'roma'
print('Resultado:', verificar_anagrama(primeira_palavra, segunda_palavra))