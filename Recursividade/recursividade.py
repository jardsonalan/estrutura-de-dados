# Recursividade

# Fatorial
def fatorial(numero: int) -> int:
  if numero == 0:
    return 1
  return numero * fatorial(numero-1)

print(fatorial(5))

# Potenciação
def potenciacao(numero: int, potencia: int) -> int:
  if potencia == 0:
    return 1
  return numero * potenciacao(numero, potencia-1)

print(potenciacao(2, 10))

# Fibonnaci
def fibonnaci(numero: int) -> int:
  if numero <= 2:
    return 1
  return fibonnaci(numero-1) + fibonnaci(numero-2)

print(fibonnaci(6))