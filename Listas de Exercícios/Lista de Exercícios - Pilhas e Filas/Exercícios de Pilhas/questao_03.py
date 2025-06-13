def expressao_balanceada(expressao):
  pilha = []
  pares = { ')': '(', ']': '[', '}': '{' } # Mapeia cada símbolo de fechamento para seu símbolo de abertura

  # Percorre cada caractere da expressão
  for caractere in expressao:
    # Verifica se o caractere é um símbolo de abertura
    if caractere in '([{':
      # Se for, adiciona a pilha
      pilha.append(caractere)
    # Verifica se é um símbolo de fechamento
    elif caractere in '}])':
      # Verifica se a pilha está vazia, ou seja, não tem símbolo de abertura
      # ou se o topo da pilha não corresponde ao símbolo de fechamento atual
      if not pilha or pilha[-1] != pares[caractere]:
        return False # Retorna False, indicando que a expressão está desbalanceada
      # Remove o símbolo de abertura que corresponde ao topo da pilha
      pilha.pop()
  
  # Após toda a verificação, verifica se a pilha está vazia
  # Se tiver, indica que todos os símbolos foram corretamente fechados e balanceados
  return not pilha

expressao = '()[]}'
if expressao_balanceada(expressao):
  print('A expressão está balanceada.')
else:
  print('A expressão NÃO está balanceada.')