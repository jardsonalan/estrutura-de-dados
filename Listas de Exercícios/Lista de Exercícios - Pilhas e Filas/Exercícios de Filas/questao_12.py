from collections import deque
from time import sleep

class Sistema_Impressao:
  def __init__(self) -> None:
    self.fila_impressao: deque[dict[str, int]] = deque([])
  
  def adicionar_arquivo(self, nome: str, quantidade_paginas: int):
    arquivo: dict[str, int] = { nome: quantidade_paginas }
    self.fila_impressao.append(arquivo)

    verificacao = input('Deseja adicionar mais um arquivo? [S/N] ').upper()

    if verificacao == 'S':
      return 'Arquivo adicionado para impressão.'
    
    return self.imprimir()
  
  def exibir_impressoes(self):
    if len(self.fila_impressao) == 0:
      print('Nenhuma impressão na fila.')
      return
    
    for i in range(len(self.fila_impressao)):
      for key, values in self.fila_impressao[i].items():
        print(f'[{i+1}] Nome do arquivo: {key} | Total de páginas: {values}')

  def imprimir(self) -> str:
    index = 0
    while True:
      for key, values in self.fila_impressao[index].items():
        print(f'Imprimindo: {key}')
        sleep(values)
        self.fila_impressao.popleft()

      if len(self.fila_impressao) > 0:
        return self.imprimir()

      break
    
    return 'Arquivos impressos com sucesso.'
    
sistema_impressao = Sistema_Impressao()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Adicionar arquivo\n[2] Exibir fila de arquivos\n[0] Sair\n-> '))

  if opcao == 0:
    break

  elif opcao == 1:
    nome_arquivo = input('Nome do arquivo: ')
    total_paginas = int(input('Total de páginas: '))
    print(sistema_impressao.adicionar_arquivo(nome_arquivo, total_paginas))

  elif opcao == 2:
    sistema_impressao.exibir_impressoes()

  else:
    print('Opção inválida.')