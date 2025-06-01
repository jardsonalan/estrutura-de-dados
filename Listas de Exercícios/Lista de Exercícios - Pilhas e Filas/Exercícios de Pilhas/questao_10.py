def verificar_palindromo(numero: int) -> str:
  pilha: list[str] = []
  converter_em_string = str(numero)

  for i in converter_em_string:
    pilha.append(i)

  junta_string = ''
  
  index = len(pilha)
  while index > 0:
    junta_string += pilha.pop()
    index -= 1
  
  converter_em_inteiro = int(junta_string)

  if numero == converter_em_inteiro:
    return f'O número {numero} é um palíndromo.'
  
  return f'O número {numero} NÃO é um palíndromo.'

print(verificar_palindromo(12321))