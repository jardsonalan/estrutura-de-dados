from binarytree import bst, build, Node

arvore_binaria = bst(height=4, is_perfect=True)

soma_atual = 0

def verificar_caminho_valor(node, valor_alvo, soma_atual):
  if node is None:
    return False
  
  soma_atual += node.value

  if node.left is None and node.right is None:
    return soma_atual == valor_alvo
  
  return verificar_caminho_valor(node.left, valor_alvo, soma_atual) or verificar_caminho_valor(node.right, valor_alvo, soma_atual)

print(arvore_binaria)
print(f'Resultado: {verificar_caminho_valor(arvore_binaria, 34, soma_atual)}')