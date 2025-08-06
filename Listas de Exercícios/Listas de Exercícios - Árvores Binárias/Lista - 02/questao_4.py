from binarytree import bst, build, Node

arvore_binaria = bst(height=4, is_perfect=True)

def verificar_altura_balanceada(node):
  if node is None:
    return True
  
  # Armazena a altura da subárvore da esquerda
  subarvore_esquerda = 0
  if node.left:
    subarvore_esquerda = node.left.height
  
  # Armazena a altura da subárvore da direita
  subarvore_direita = 0
  if node.right:
    subarvore_direita = node.right.height

  # Verifica a diferença de altura entre as subárvores
  if subarvore_esquerda - subarvore_direita > 1:
    return False
  
  return verificar_altura_balanceada(node.left) and verificar_altura_balanceada(node.right)

print(arvore_binaria)
print(f'Resultado da verificação: {verificar_altura_balanceada(arvore_binaria)}')