def potenciacao(numero: int, potencia: int) -> int:
  if potencia == 0:
    return 1
  return numero * potenciacao(numero, potencia-1)

print(potenciacao(2,10))