# Shell Sort
def shell_sort(lista: list[int]) -> list[int]:
  gap = len(lista) // 2 # Divide a lista pela metade para definir o primeiro intervalo (gap)

  while gap > 0: # Executa o loop enquanto o valor do gap for maior que 0
    for i in range(len(lista)): # Percorre os index da lista do início ao fim
      aux = lista[i] # Variável auxiliar que armazena o valor da vez

      # Verifica se o index atual é maior ou igual ao gap
      # e se o valor localizado 'gap' posições antes é maior que o valor atual (aux)
      while i >= gap and lista[i - gap] > aux:
        lista[i] = lista[i - gap] # Move o valor anterior (mais distante) para frente
        i -= gap # Volta 'gap' posições para continuar a verificação

      lista[i] = aux # Insere o valor original (aux) na posição correta após os deslocamentos
    
    gap //= 2 # Divide o valor do gap pela metade a cada iteração
   
  return lista # Retorna a lista ordenada

lista_desordenada = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
print(shell_sort(lista_desordenada))