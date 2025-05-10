def numeros_decrescentes(numero: int) -> 1:
  if numero == 1:
    return 1
  print(numero)
  return numeros_decrescentes(numero-1)

print(numeros_decrescentes(5))