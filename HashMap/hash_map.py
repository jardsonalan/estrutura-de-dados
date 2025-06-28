def numeros_duplicados(lista: list[int]) -> list[int]:
  hash_map = {}
  chaves = []
  resultado = []

  for i in lista:
    if str(i) not in hash_map.keys():
      hash_map[str(i)] = 1
      chaves.append(str(i))
    else:
      hash_map[str(i)] += 1
  
  for c in chaves:
    if hash_map[c] > 1:
      resultado.append(c)
  
  return resultado

lista_completa = [1, 1, 5, 2, 3, 4, 3, 5]
duplicados = numeros_duplicados(lista_completa)
print(duplicados)