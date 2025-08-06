from binarytree import bst, build, Node

def inserir_bst(node, valor):
  # Verifica se um nó não tem filhos e insere o valor
  if node is None:
    return Node(valor)
  
  # Verifica se o valor é menor que o valor do nó atual
  if valor < node.value:
    # Insere o valor na subárvore da esquerda
    node.left = inserir_bst(node.left, valor)
  else:
    # Se não, insere o valor na subárvore da direita
    node.right = inserir_bst(node.right, valor)
  
  return node

def construir_bst(pre_ordem):
  node = None

  for valor in pre_ordem:
    node = inserir_bst(node, valor)
  
  return node

pre_ordem = [8, 5, 1, 7, 10, 12]
print(construir_bst(pre_ordem))