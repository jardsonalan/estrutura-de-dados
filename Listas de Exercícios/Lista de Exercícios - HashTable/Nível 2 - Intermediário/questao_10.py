def somar_notas(boletim: dict):
  somar_notas = {}

  for chave, valor in boletim.items():
    for nota in valor:
      if chave in somar_notas.keys():
        somar_notas[chave] += nota
      else:
        somar_notas[chave] = nota
  
  return somar_notas

boletim = { "Lucas": [10, 8, 6, 9], "Marcos": [7, 7, 8, 10] }

print(somar_notas(boletim))