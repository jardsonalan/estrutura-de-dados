from binarytree import bst, build, Node

arvore_binaria = bst(height=4, is_perfect=True)

def contador_nos_internos(node):
  if node is None:
    return 0
  
  # Verifica se o nó não é None, ou seja, tem pelo menos um filho
  if node.left or node.right:
    return 1 + contador_nos_internos(node.left) + contador_nos_internos(node.right)
  
  # Caso seja folha, retorna 0
  return 0

print(arvore_binaria)
print(f'Total de nós internos: {contador_nos_internos(arvore_binaria)}')