def detecta_anagramas(lista):
  hashtable_anagramas = {}
  
  for palavra in lista:
    chave = ''.join(insertion_sort(list(palavra)))

    if chave in hashtable_anagramas.keys():
      hashtable_anagramas[chave].append(palavra)
    else:
      hashtable_anagramas[chave] = [palavra]
  
  return hashtable_anagramas

def insertion(lista, index):
  for item in range(index, 0, -1):
    if lista[item] < lista[item - 1]:
      aux = lista[item]
      lista[item] = lista[item - 1]
      lista[item - 1] = aux
  return lista

def insertion_sort(lista):
  index = 1
  while index < len(lista):
    lista = insertion(lista, index)
    index += 1
  return lista

lista = ['amor', 'lento', 'rico', 'morro', 'roma', 'ramo', 'moro', 'oram', 'notel', 'cori', 'romro']

print(detecta_anagramas(lista))