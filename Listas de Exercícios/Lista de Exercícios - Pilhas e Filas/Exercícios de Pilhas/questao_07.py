def infixa_para_posfixa(expressao):
  pilha = [] # Serve para armazenar operadores e parênteses
  saida = [] # Lista que forma a expressão na forma pós-fixa

  # Percorre cada caractere da expressão
  for caractere in expressao:
    if caractere.isalnum(): # Verifica se é um operando (letra ou número)
      saida.append(caractere) # Adiciona na saída (ordem pós-fixa)
    elif caractere == '(': # Verifica se é um parênteses de abertura
      pilha.append(caractere) # Armazena na pilha
    elif caractere == ')': # Verifica se é um parênteses de fechamento
      # Remove da pilha e adiciona na saida até encontrar o '('
      while pilha and pilha[-1] != '(':
        saida.append(pilha.pop())
      pilha.pop() # Remove o '(' da pilha, sem enviar para a saída
    else: # Caso seja um operador
      # Adiciona os operadores na sáida, exceto os '('
      while pilha and pilha[-1] != '(':
        saida.append(pilha.pop())
      pilha.append(caractere) # Empilha o operador atual

  # Serve para remover todos os operadores restantes da pilha
  while pilha:
    saida.append(pilha.pop())

  return saida

print(infixa_para_posfixa('A+B'))