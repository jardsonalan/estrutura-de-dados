class Capacidade_Limitada:
  def __init__(self) -> None:
    self.pilha: list[str] = []
    self.capacidade: int = 10

  def inserir(self, elemento: str) -> str:
    if len(self.pilha) == self.capacidade:
      return 'A pilha está cheia.'
    
    self.pilha.append(elemento)
    return f'Pilha: {self.pilha}'
  
  def remover(self) -> str:
    if len(self.pilha) == 0:
      return 'A pilha está vazia.'
    
    self.pilha.pop()

    if len(self.pilha) == 0:
      return 'A pilha está vazia.'

    return f'Pilha: {self.pilha}'
  
capacidade_limitada = Capacidade_Limitada()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Inserir elemento\n[2] Remover elemento\n[0] Sair\n-> '))

  if opcao == 0:
    break

  elif opcao == 1:
    elemento = input('Informe o que deseja inserir na lista: ')
    print(capacidade_limitada.inserir(elemento))

  elif opcao == 2:
    print(capacidade_limitada.remover())
  
  else:
    print('Opção inválida.')