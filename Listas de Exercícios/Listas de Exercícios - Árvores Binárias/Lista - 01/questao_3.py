from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)
print(arvore_binaria)

def pre_ordem(node):
  if node is None:
    return []
  return [node.value] + pre_ordem(node.left) + pre_ordem(node.right)

print('Pré-Ordem:')
print(pre_ordem(arvore_binaria))