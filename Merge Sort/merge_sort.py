import math
from time import time

def merge_sort(list: list[int]) -> list[int]:
  if len(list) == 1:
    return list

  metade = len(list) // 2
  
  return shell_sort(merge_sort(list[:metade]) + merge_sort(list[metade:]))


def shell_sort(list: list[int]) -> list[int]:
  gap = math.ceil(len(list) / 2)

  while gap > 0:
    for index in range(0, len(list) - gap):
      aux = list[index]

      if list[index + gap] < aux:
        list[index] = list[index + gap]
        list[index + gap] = aux

    gap -= 1

  print('Shell Sort:', list)
  return list

lista = [3, 1, 5, 2, 4, 9]

tempo_inicial = time()
print('Lista Ordenada:', merge_sort(lista))
tempo_final = time()
tempo_total = tempo_final - tempo_inicial
print('Tempo Total:', tempo_total)