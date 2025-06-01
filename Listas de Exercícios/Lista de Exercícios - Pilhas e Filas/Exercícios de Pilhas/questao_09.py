class Save_Point:
  def __init__(self) -> None:
    self.pilha_estado: list[str] = []
  
  def salvar_estado(self) -> str:
    descricao = input('Qual nome deseja colocar nesse estado? ')
    self.pilha_estado.append(descricao)

    return f'Estado atual: {self.pilha_estado[-1]}'

  def voltar_estado(self) -> str:
    if len(self.pilha_estado) == 0:
      return 'Nenhum estado salvo.'
    
    print(self.exibir_estados_salvos())
    print('[0] Apagar todos os estados')

    index = int(input('Informe a numeração do estado que deseja voltar: '))

    tamanho_pilha = len(self.pilha_estado)
    while tamanho_pilha > index:
      self.pilha_estado.pop()
      tamanho_pilha -= 1

    if index == 0 and len(self.pilha_estado) == 0:
      return 'Todos os estados foram apagados.'
    
    return f'Estado atual: {self.pilha_estado[-1]}'
  
  def exibir_estados_salvos(self) -> str:
    if len(self.pilha_estado) == 0:
      return 'Nenhum estado salvo.'
    
    listar_estado = ''

    print(' Estados Salvos '.center(20, '-'))
    for i in range(len(self.pilha_estado)):
      listar_estado += f'[{i+1}] {self.pilha_estado[i]}\n'

    return listar_estado

save_point = Save_Point()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Salvar estado\n[2] Voltar estado\n[3] Exibir estados salvos\n[0] Sair\n-> '))

  if opcao == 0:
    break

  elif opcao == 1:
    print(save_point.salvar_estado())

  elif opcao == 2:
    print(save_point.voltar_estado())

  elif opcao == 3:
    print(save_point.exibir_estados_salvos())
  
  else:
    print('Opção inválida.')