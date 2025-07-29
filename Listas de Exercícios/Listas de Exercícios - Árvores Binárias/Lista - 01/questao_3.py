from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)
print(arvore_binaria)

def preordem(node):
  if node is None:
    return []
  return [node.value] + preordem(node.left) + preordem(node.right)

print('Pré-Ordem:')
print(preordem(arvore_binaria))