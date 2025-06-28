def filtragem_produtos(produtos: dict):
  produtos_filtrados = {}

  for chave, valor in produtos.items():
    if valor > 50:
      produtos_filtrados[chave] = valor
    else:
      pass

  return produtos_filtrados

produtos = {
  "Carro" : 1200,
  "Bola" : 10,
  "Moto" : 500,
}
print(filtragem_produtos(produtos))