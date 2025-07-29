from binarytree import bst, Node

arvore_binaria = bst(height=3, is_perfect=True)

def insercao(node, valor):
  # Verifica se não existe mais nó
  if node is None:
    # Insere o valor na posição
    return Node(valor)
  # Verifica se o valor é menor que o nó atual
  if valor < node.value:
    # Chama a função novamente, com o valor do nó da esquerda
    node.left = insercao(node.left, valor)
  else:
    # Caso o valor seja maior que o nó atual
    # Chama a função novamente, com o valor do nó da direita
    node.right = insercao(node.right, valor)
  # Após a inserção ocorrer corretamente
  # retorna o nó atual para que árvore seja atualizada
  return node

arvore = insercao(arvore_binaria, 5)
arvore = insercao(arvore_binaria, 2)

print(arvore)