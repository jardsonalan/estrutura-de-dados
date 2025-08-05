from binarytree import bst, Node

arvore_binaria = bst(height=4, is_perfect=True)
print(arvore_binaria)

def calcula_altura(node):
  # Ordem de parada
  if node is None:
    # Retorna -1 para que uma folha tenha altura 0
    return -1
  
  # Calcula a altura da esquerda e da direita de forma recursiva
  # e compara qual das duas subárvores é mais alta
  if calcula_altura(node.left) > calcula_altura(node.right):
  # Soma 1 para incluir o nível do nó atual
    return 1 + calcula_altura(node.left)
  return 1 + calcula_altura(node.right)

print(f'Altura da árvore: {calcula_altura(arvore_binaria)}')