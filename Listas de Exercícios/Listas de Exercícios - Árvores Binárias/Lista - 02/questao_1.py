from binarytree import bst, build, Node

arvore_binaria = bst(height=4, is_perfect=True)

def verificar_propriedade_bst(node):
  if node is None:
    return True
  
  # Verifica se o valor da subárvore da esquerda é maior que o valor atual
  if node.left and node.left.value >= node.value:
    return False
  
  # Verifica se o valor da subárvore da direita é menor que o valor atual
  if node.right and node.right.value <= node.value:
    return False
  
  return verificar_propriedade_bst(node.left) and verificar_propriedade_bst(node.right)

print(arvore_binaria)
print(f'Resultado: {verificar_propriedade_bst(arvore_binaria)}')