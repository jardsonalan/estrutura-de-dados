from collections import deque

class Caixa_Supermecado:
  def __init__(self) -> None:
    self.fila: deque[int] = deque([])
    self.cliente: int = 1

  def chegada_cliente(self) -> str:
    self.fila.append(self.cliente)
    self.cliente += 1

    return 'Chegou um cliente.'

  def atendimento_cliente(self) -> str:
    if len(self.fila) == 0:
      return 'Não tem nenhum cliente na fila.'
    
    atendido = self.fila.popleft()
    return f'O cliente de número {atendido} foi atendido.'

  def estado_atual(self) -> str:
    if len(self.fila) == 0:
      return f'Ainda não chegou nenhum cliente.'
    elif len(self.fila) == 1:
      return f'Tem {len(self.fila)} cliente na fila.'  
    return f'Tem {len(self.fila)} clientes na fila.'
  

caixa_supermecado = Caixa_Supermecado()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Chegada de Cliente\n[2] Atendimento de Cliente\n[3] Estado da Fila\n[0] Sair\n-> '))

  if opcao == 0:
    break

  elif opcao == 1:
    print(caixa_supermecado.chegada_cliente())

  elif opcao == 2:
    print(caixa_supermecado.atendimento_cliente())

  elif opcao == 3:
    print(caixa_supermecado.estado_atual())

  else:
    print('Opção inválida.')