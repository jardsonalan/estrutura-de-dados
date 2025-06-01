class Navegador:
  def __init__(self) -> None:
    self.pilha_atual: list[str] = []
    self.pilha_historico: list[str] = []

  def avancar(self, pesquisa: str) -> str:
    if len(self.pilha_atual) == 0 and len(self.pilha_historico) == 0:
      self.pilha_atual.append(pesquisa)
      self.pilha_historico.append(pesquisa)
      return f'Pesquisa atual: {self.pilha_atual} | Histórico: {self.pilha_historico}'

    pesquisa_atual = self.pilha_atual.pop()

    if self.pilha_historico.count(pesquisa_atual) > 0:
      self.pilha_historico.remove(pesquisa_atual)
      self.pilha_atual.append(pesquisa)
      self.pilha_historico.append(pesquisa_atual)
    else:
      self.pilha_atual.append(pesquisa)
      self.pilha_historico.append(pesquisa_atual)

    return f'Pesquisa atual: {self.pilha_atual} | Histórico: {self.pilha_historico}'

  def voltar(self) -> str:
    if len(self.pilha_historico) == 0:
      return 'Histórico vazio.'
    
    pesquisa_anterior = self.pilha_historico.pop()
    self.pilha_atual.pop()
    self.pilha_atual.append(pesquisa_anterior)

    return f'Pesquisa atual: {self.pilha_atual} | Histórico: {self.pilha_historico}'

navegador = Navegador()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Pesquisar\n[2] Voltar\n[0] Sair\n-> '))

  if opcao == 0:
    break

  elif opcao == 1:
    pesquisa = input('O que deseja pesquisar? ')
    print(navegador.avancar(pesquisa))

  elif opcao == 2:
    print(navegador.voltar())

  else:
    print('Opção inválida.')