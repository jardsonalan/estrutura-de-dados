def inverter_string(palavra: str) -> str:
  pilha_palavra: list[str] = []
  string_invertida = ''

  for i in palavra:
    pilha_palavra.append(i)

  index = len(pilha_palavra)
  while index > 0:
    string_invertida += pilha_palavra.pop()
    index -= 1

  return f'A inverção da palavra {palavra} é: {string_invertida}'

print(inverter_string('abelha'))