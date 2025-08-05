from binarytree import bst, Node

arvore_binaria = bst(height=4, is_perfect=True)
print(arvore_binaria)

def encontrar_index(node, valor):
  contador = 0
  for i in node:
    if i.value == valor:
      return contador
    contador += 1

index = encontrar_index(arvore_binaria, 5)

def remover_no(node, index):
  if index is None:
    return 'Valor não encontrado.'
  del node[index]
  return node

print(remover_no(arvore_binaria, index))