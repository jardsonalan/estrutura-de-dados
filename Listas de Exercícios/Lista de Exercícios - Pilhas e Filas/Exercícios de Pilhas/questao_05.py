def fatorial(numero: int) -> str:
  pilha_fatorial: list[int] = []
  resultado_fatorial = 1

  for i in range(1, numero+1):
    pilha_fatorial.append(i)

  index = len(pilha_fatorial)
  while index > 0:
    resultado_fatorial *= pilha_fatorial.pop()
    index -= 1

  return f'Fatorial de {numero} é: {resultado_fatorial}'

print(fatorial(5))