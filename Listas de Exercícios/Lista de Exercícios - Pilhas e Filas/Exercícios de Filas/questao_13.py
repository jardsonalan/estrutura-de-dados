from collections import deque

class Fila_Circular:
  def __init__(self, tamanho_fila):
    self.fila = deque(maxlen=tamanho_fila)
    self.tamanho_maximo = tamanho_fila

  def inserir(self, valor):
    if len(self.fila) == self.tamanho_maximo:
      return 'Fila cheia.'
    self.fila.append(valor)
    print(f'Inserido: {valor}')
    return self.mostrar_fila()
  
  def remover(self):
    if len(self.fila) == 0:
      return 'Fila vazia.'
    valor = self.fila.popleft()
    print(f'Removido: {valor}')
    return self.mostrar_fila()
  
  def mostrar_fila(self):
    return list(self.fila)
  
fila_circular = Fila_Circular(5)

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Inserir\n[2] Remover\n[3] Mostrar fila\n[0] Sair\n-> '))

  if opcao == 0:
    break
  elif opcao == 1:
    valor = int(input('Informe o valor que deseja inserir: '))
    print(fila_circular.inserir(valor))
  elif opcao == 2:
    print(fila_circular.remover())
  elif opcao == 3:
    print(fila_circular.mostrar_fila())
  else:
    print('Opção inválida.')