class Editor_Texto:
  def __init__(self):
    self.acoes = []

  def escrever(self):
    self.acoes.append('escrever')
    print(self.acoes)
    return 'Escreveu.'

  def apagar(self):
    self.acoes.append('apagar')
    print(self.acoes)
    return 'Apagou.'

  def desfazer(self):
    if len(self.acoes) == 0:
      return 'Nenhuma ação registrada.'
    
    self.acoes.pop()
    print(self.acoes)
    return 'Alteração desfeita.'

editor_texto = Editor_Texto()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Escrever\n[2] Apagar\n[3] Desfazer\n[0] Sair\n-> '))

  if opcao == 0:
    break
  elif opcao == 1:
    print(editor_texto.escrever())
  elif opcao == 2:
    print(editor_texto.apagar())
  elif opcao == 3:
    print(editor_texto.desfazer())