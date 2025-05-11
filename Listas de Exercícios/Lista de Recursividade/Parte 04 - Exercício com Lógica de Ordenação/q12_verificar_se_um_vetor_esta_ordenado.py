def verificar_vetor_ordenado(vetor: list, tamanho: int) -> str:
  if tamanho <= 1:
    return 'O vetor está ordenado.'
  
  if vetor[tamanho] < vetor[tamanho - 1]:
    return 'O vetor NÃO está ordenado.'
  
  return verificar_vetor_ordenado(vetor, tamanho - 1)

vetor = [1, 2, 3, 4, 5]
print(verificar_vetor_ordenado(vetor, len(vetor)-1))