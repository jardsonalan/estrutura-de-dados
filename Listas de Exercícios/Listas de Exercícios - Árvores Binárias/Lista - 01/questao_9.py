from binarytree import bst, Node

arvore_binaria = bst(height=4, is_perfect=True)
print(arvore_binaria)

def valor_maximo(node):
  if node.right is None:
    return node.value
  return valor_maximo(node.right)
  
print(f'Valor máximo: {valor_maximo(arvore_binaria)}')