# Bubble Sort
def bubble_sort(list: list[int]) -> list[int]:
  for j in range(len(list)):
    # j: armazena a quantidade de passos já feitos
    for i in range(len(list)-j-1): # len(list)-j-1: serve para controlar a quantidade de comparações que serão feitas a cada rodada da ordenação
      # i: serve para percorrer os index da lista
      if list[i] > list[i+1]:
        aux = list[i]
        list[i] = list[i+1]
        list[i+1] = aux
  return list

list = [5, 3, 15, 8, 1]
print(bubble_sort(list))