def fibonacci(numero: int) -> int:
  if numero <= 2:
    return 1
  return fibonacci(numero-1) + fibonacci(numero-2)

print(fibonacci(6))