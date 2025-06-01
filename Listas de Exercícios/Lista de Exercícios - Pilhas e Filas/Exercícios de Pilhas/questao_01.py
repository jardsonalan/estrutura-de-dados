from typing import Any, Union

def calcula_pos_fixa(notacao: str) -> str:
  pilha_numeros: list[Any] = []
  pilha_invertida: list[Any] = []
  pilha_resultado: list[Union[int, float]] = []

  # Serve para armazenar a notação em uma pilha
  for i in notacao.split():
    if i in ['+', '-', '*', '/']: # Verifica se o elemento é um operador
      pilha_numeros.append(i) # Adiciona os operadores em formato string
    else:
      converter_em_inteiro = int(i) # Converte os números para inteiro
      pilha_numeros.append(converter_em_inteiro) # Armazena os números convertidos na pilha

  # Serve para armazenar os elementos da pilha_numeros em outra pilha, com os valores invertidos
  index = len(pilha_numeros)
  while index > 0:
    pilha_invertida.append(pilha_numeros.pop())
    index -= 1

  # Serve para percorrer a pilha_invertida
  index_pilha_invertida = len(pilha_invertida)
  while index_pilha_invertida > 0:
    elemento = pilha_invertida.pop() # Armazena o último elemento da pilha
    if type(elemento) == int: # Verifica se o tipo do elemento é igual a int
      pilha_resultado.append(elemento) # Adiciona na pilha_resultado
    else:
      # Se não for int, verifica o tipo do operador
      # Armazena o último número na variável ultimo_numero
      # Armazena o penúltimo número na variável penultimo_numero
      if elemento == '+':
        ultimo_numero = pilha_resultado.pop()
        penultimo_numero = pilha_resultado.pop()
        pilha_resultado.append(penultimo_numero+ultimo_numero) # Faz a seguinte operação: penultimo_numero + ultimo_numero
      
      elif elemento == '-':
        ultimo_numero = pilha_resultado.pop()
        penultimo_numero = pilha_resultado.pop()
        pilha_resultado.append(penultimo_numero-ultimo_numero) # Faz a seguinte operação: penultimo_numero - ultimo_numero
      
      elif elemento == '*':
        ultimo_numero = pilha_resultado.pop()
        penultimo_numero = pilha_resultado.pop()
        pilha_resultado.append(penultimo_numero*ultimo_numero) # Faz a seguinte operação: penultimo_numero x ultimo_numero
      
      elif elemento == '/':
        ultimo_numero = pilha_resultado.pop()
        penultimo_numero = pilha_resultado.pop()
        pilha_resultado.append(penultimo_numero/ultimo_numero) # Faz a seguinte operação: penultimo_numero / ultimo_numero
    
    index_pilha_invertida -= 1

  return f'Resultado: {pilha_resultado[0]}'

print(calcula_pos_fixa("5 1 2 + 4 * + 3 -"))