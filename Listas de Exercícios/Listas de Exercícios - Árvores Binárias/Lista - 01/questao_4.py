from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)
print(arvore_binaria)

def inorder(node):
  if node is None:
    return []
  return inorder(node.left) + [node.value] + inorder(node.right)

print('In-Order:')
print(inorder(arvore_binaria))