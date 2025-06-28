class Gerenciador_Pessoas:
  def __init__(self):
    self.dicionario_pessoas = {}

  # Questão 1
  def armazena_nomes(self, nome, idade):
    self.dicionario_pessoas[nome] = idade
    return self.dicionario_pessoas
  
  # Questão 2
  def acessa_valor(self, valor):
    if valor in self.dicionario_pessoas.keys():
      return f'{valor} tem {self.dicionario_pessoas[valor]} anos.'
    return 'Pessoa não encontrada.'
  
  # Questão 3
  def adiciona_e_remove(self, nome, idade, remove_pessoa):
    if remove_pessoa in self.dicionario_pessoas.keys():
      self.dicionario_pessoas[nome] = idade
      del self.dicionario_pessoas[remove_pessoa]
      return 'Pessoa removida com sucesso.'
    return 'A pessoa que deseja remover, não se encontra no sistema.'
    
  # Questão 4
  def verificar_chave(self, chave):
    if chave in self.dicionario_pessoas.keys():
      return f'{chave} está presente no sistema.'
    return f'{chave} NÃO está no sistema.'
    
  # Questão 5
  def listar_pessoas(self):
    if len(self.dicionario_pessoas) == 0:
      return 'Ainda não tem nenhuma pessoa cadastrada no sistema.'
    
    lista_pessoas = ''
    for nome, idade in self.dicionario_pessoas.items():
      lista_pessoas += f'Nome: {nome} | Idade: {idade}\n'
    
    return lista_pessoas

gerenciador_pessoas = Gerenciador_Pessoas()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Adicionar pessoas\n[2] Acessar valor\n[3] Adicionar e remover pessoa\n[4] Verificar pessoa\n[5] Listar pessoas\n[0] Sair\n-> '))

  if opcao == 0:
    break
  elif opcao == 1:
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    print(gerenciador_pessoas.armazena_nomes(nome, idade))
  elif opcao == 2:
    nome = input('Informe o nome que deseja procurar: ')
    print(gerenciador_pessoas.acessa_valor(nome))
  elif opcao == 3:
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    pessoa_remover = input('Informe o nome da pessoa que deseja remover: ')
    print(gerenciador_pessoas.adiciona_e_remove(nome, idade, pessoa_remover))
  elif opcao == 4:
    nome = input('Informe o nome da pessoa que deseja verificar: ')
    print(gerenciador_pessoas.verificar_chave(nome))
  elif opcao == 5:
    print(gerenciador_pessoas.listar_pessoas())
  else:
    print('Opção inválida.')