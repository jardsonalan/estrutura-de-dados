from binarytree import bst, Node

arvore_binaria = bst(height=4, is_perfect=True)
print(arvore_binaria)

def calcula_altura(node):
  if node is None:
    return -1
  return 1 + max(calcula_altura(node.left), calcula_altura(node.right))

print(f'Altura da árvore: {calcula_altura(arvore_binaria)}')