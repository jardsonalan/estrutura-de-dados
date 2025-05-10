def soma_elementos(vetor: list, tamanho: int) -> int:
  if tamanho == 0:
    return 0
  return vetor[tamanho - 1] + soma_elementos(vetor, tamanho - 1)

vetor = [1, 2, 3, 4, 5]

print(soma_elementos(vetor, len(vetor)))