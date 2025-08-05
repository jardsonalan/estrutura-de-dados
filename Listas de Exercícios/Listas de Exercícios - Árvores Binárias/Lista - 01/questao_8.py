from binarytree import bst, Node

arvore_binaria = bst(height=4, is_perfect=True)
print(arvore_binaria)

def valor_minimo(node):
  if node.left is None:
    return node.value
  return valor_minimo(node.left)
  
print(f'Valor mínimo: {valor_minimo(arvore_binaria)}')