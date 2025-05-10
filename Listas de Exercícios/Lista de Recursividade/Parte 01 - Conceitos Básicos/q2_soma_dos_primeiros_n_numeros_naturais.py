def soma(numero: int) -> int:
  if numero == 1:
    return numero
  return numero + soma(numero-1)

print(soma(5))