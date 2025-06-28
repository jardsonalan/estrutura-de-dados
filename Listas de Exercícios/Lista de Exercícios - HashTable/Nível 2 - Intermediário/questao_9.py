def mesclagem_dicionario(dict_1: dict, dict_2: dict):
  resultado = {}
  
  for chave, valor in dict_1.items():
    if chave in resultado.keys():
      resultado[chave] += valor
    else:
      resultado[chave] = valor
  
  for chave, valor in dict_2.items():
    if chave in resultado.keys():
      resultado[chave] += valor
    else:
      resultado[chave] = valor

  return resultado

dicionario_1 = {
  "João" : 10,
  "Marcos" : 8,
  "Lucas" : 7,
}

dicionario_2 = {
  "Maria" : 10,
  "Marcos" : 2,
  "Joana" : 7,
}

print(mesclagem_dicionario(dicionario_1, dicionario_2))