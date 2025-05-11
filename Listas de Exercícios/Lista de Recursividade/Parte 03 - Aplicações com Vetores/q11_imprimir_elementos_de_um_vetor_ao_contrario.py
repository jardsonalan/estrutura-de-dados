def elementos_ao_contrario(vetor: list, tamanho: int) -> list:
  if tamanho < 0:
    return []
  return [vetor[tamanho]] + elementos_ao_contrario(vetor, tamanho - 1)

vetor = ['ana', 1, 'gato', 2, 'casa']
print(elementos_ao_contrario(vetor, len(vetor) - 1))