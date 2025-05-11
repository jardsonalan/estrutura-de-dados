def verificar_polindromo(palavra: str) -> str:
  if len(palavra) <= 1:
    return f'{palavra} é um políndromo'
  if palavra[0] != palavra[-1]: # Verifica se as primeiras e as últimas letras são diferentes, a cada chamada da função recursiva
    return f'{palavra} NÃO é um políndromo'
  return verificar_polindromo(palavra[1:-1])

print(verificar_polindromo('amor'))