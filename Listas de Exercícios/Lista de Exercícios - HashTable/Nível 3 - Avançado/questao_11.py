class Hashtable_Simples:
  def __init__(self):
    self.hashtable = []
    self.hash_key = []
    self.hash_value = []

  # Insere valores em listas separadas (hash_key e hash_value)
  # e processa os valores das listas em uma única lista
  def inserir(self, nome, valor):
    # Adiciona os nomes em uma lista de chaves
    self.hash_key.append(nome)
    # Adiciona os valores em uma lista de valores
    self.hash_value.append(valor)
    # Executa o processador
    self.processador(self.hash_key, self.hash_value)
  
  # Busca valores no hashtable principal
  def buscar_valor(self, nome):
    # Verifica se a hashtable está vazia
    if len(self.hashtable) == 0:
      return 'Hash vazio.'
    
    # Percorre os valores da hashtable
    for i in self.hashtable:
      # Verifica se o nome está em algum valor armazenado na hashtable
      if nome in i:
        return i
    
    return 'Valor não encontrado.'

  # Processa os valores informados em uma única lista
  def processador(self, lista_nome, lista_valor):
    # Percorre a hash_key
    for key in lista_nome:
      # Percorre a hash_value
      for value in lista_valor:
        # Adiciona os valores correspondentes na hashtable
        # dentro de uma tupla
        self.hashtable.append((key, value))
        # Limpa a lista de hash_key e hash_value
        self.hash_key.pop()
        self.hash_value.pop()
    return

hashtable_simples = Hashtable_Simples()

while True:
  print(' Menu '.center(20, '-'))
  opcao = int(input('[1] Inserir valor\n[2] Buscar valor\n[0] Sair\n-> '))

  if opcao == 0:
    break

  elif opcao == 1:
    nome = input('Informe um nome: ')
    valor = input('Informe um valor: ')
    hashtable_simples.inserir(nome, valor)

  elif opcao == 2:
    nome = input('Informe o nome que deseja buscar: ')
    print(hashtable_simples.buscar_valor(nome))

  else:
    print('Opção inválida.')