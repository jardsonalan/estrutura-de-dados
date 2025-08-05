from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)
print(arvore_binaria)

def pos_ordem(node):
  if node is None:
    return []
  return pos_ordem(node.left) + pos_ordem(node.right) + [node.value]

print('Pós-Ordem:')
print(pos_ordem(arvore_binaria))