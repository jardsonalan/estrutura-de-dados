from binarytree import bst, build, Node

arvore_binaria = bst(height=4, is_perfect=True)

def soma_nos(node):
  if node is None:
    return 0
  
  return node.value + soma_nos(node.left) + soma_nos(node.right)

print(f'Soma de todos os nós: {soma_nos(arvore_binaria)}')