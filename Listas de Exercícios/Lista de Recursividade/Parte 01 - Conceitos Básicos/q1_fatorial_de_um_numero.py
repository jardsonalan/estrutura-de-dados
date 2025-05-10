def fatorial(numero: int) -> int:
  if numero == 0:
    return 1
  return numero * fatorial(numero-1)

print(fatorial(3))