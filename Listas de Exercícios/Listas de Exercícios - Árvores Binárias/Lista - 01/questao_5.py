from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)
print(arvore_binaria)

def posordem(node):
  if node is None:
    return []
  return posordem(node.left) + posordem(node.right) + [node.value]

print('Pós-Ordem:')
print(posordem(arvore_binaria))