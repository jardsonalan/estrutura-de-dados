from time import time

# Merge Sort
def merge_sort(list: list[int]) -> list[int]:
  # Caso base: se a lista tiver apenas um elemento, indica que ela já está ordenada
  if len(list) == 1:
    return list # Retorna a lista ordenada

  # Divide a lista pela metade utilizando uma divisão inteira
  metade = len(list) // 2
  
  # Aplica recursivamente o merge_sort nas duas metades
  # Depois junta as duas listas e aplica o shell_sort para ordená-las
  return shell_sort(merge_sort(list[:metade]) + merge_sort(list[metade:]))

def shell_sort(lista: list[int]) -> list[int]:
  gap = len(lista) // 2

  while gap > 0:
    for i in range(len(lista)):
      aux = lista[i]

      while i >= gap and lista[i - gap] > aux:
        lista[i] = lista[i - gap]
        i -= gap

      lista[i] = aux
    
    gap //= 2
   
  return lista

lista = [3, 1, 5, 2, 4, 9]

tempo_inicial = time()
print('Lista Ordenada:', merge_sort(lista))
tempo_final = time()
tempo_total = tempo_final - tempo_inicial
print('Tempo Total:', tempo_total)