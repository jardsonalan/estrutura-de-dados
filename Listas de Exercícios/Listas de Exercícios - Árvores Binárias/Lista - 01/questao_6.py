from binarytree import bst, Node

arvore_binaria = bst(height=4, is_perfect=True)
print(arvore_binaria)

def busca(node, valor):
  if node is None:
    return 'Valor não encontrado.'
  if valor == node.value:
    return 'Valor encontrado.'
  elif valor < node.value:
    return busca(node.left, valor)
  return busca(node.right, valor)
      
print('Resultado:', busca(arvore_binaria, 6))