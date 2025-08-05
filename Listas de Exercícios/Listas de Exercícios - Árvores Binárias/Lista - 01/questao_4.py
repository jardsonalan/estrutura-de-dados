from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)
print(arvore_binaria)

def in_order(node):
  if node is None:
    return []
  return in_order(node.left) + [node.value] + in_order(node.right)

print('In-Order:')
print(in_order(arvore_binaria))