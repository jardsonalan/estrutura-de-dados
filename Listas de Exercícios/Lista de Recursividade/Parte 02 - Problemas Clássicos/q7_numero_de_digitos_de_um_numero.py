def numeros_digitos(numero: int) -> int:
  if numero == 0:
    return numero
  return numeros_digitos(numero//10) + 1

print(numeros_digitos(12))