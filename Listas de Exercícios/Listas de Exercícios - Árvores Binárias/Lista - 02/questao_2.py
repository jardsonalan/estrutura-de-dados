from binarytree import bst, build, Node

arvore_binaria = bst(height=4, is_perfect=True)

def contador_folhas(node):
  if node is None:
    return 0
  
  # Verifica se o nó é None, ou seja, não tem filhos
  if node.left is None and node.right is None:
    return 1
  
  # Recursividade para contar folhas na esquerda e direita
  return contador_folhas(node.left) + contador_folhas(node.right)

print(arvore_binaria)
print(f'Total de folhas: {contador_folhas(arvore_binaria)}')