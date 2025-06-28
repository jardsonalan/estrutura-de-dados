def contador_frequencia(texto):
  frequencia = {}

  for i in texto:
    if i not in frequencia.keys():
      frequencia[i] = 1
    else:
      frequencia[i] += 1
  
  return frequencia

texto = 'alan'
print(contador_frequencia(texto))