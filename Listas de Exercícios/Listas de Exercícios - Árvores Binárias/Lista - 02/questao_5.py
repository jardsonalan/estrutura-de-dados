from binarytree import bst, build, Node
from collections import deque

arvore_binaria = bst(height=4, is_perfect=True)

def percurso_em_nivel(node):
  if node is None:
    return []
  
  fila = deque([node])
  resultado = []

  while len(fila) > 0:
    no_atual = fila.popleft()
    resultado.append(no_atual.value)

    # Verifica se o nó tem filho na esquerda 
    if no_atual.left:
      fila.append(no_atual.left)
    # Verifica se o nó tem filho na direita
    if no_atual.right:
      fila.append(no_atual.right)
    
  return resultado

print(arvore_binaria)
print('Percurso em Nível:\n', percurso_em_nivel(arvore_binaria))