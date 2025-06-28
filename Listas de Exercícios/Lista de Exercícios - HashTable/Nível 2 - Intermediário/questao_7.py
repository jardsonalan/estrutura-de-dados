def inverter_dicionario(dicionario: dict):
  novo_dicionario = {}

  for chave, valor in dicionario.items():
    novo_dicionario[valor] = chave

  return novo_dicionario

dicionario = { 
  "Bola" : 1,
  "Casa" : 2,
  "Carro" : 3,
}
print(inverter_dicionario(dicionario))