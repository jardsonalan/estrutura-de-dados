## Pilha
Pilha é uma estrutura de dados do tipo **LIFO** (*Last In, First Out*), ou seja, o **último elemento** inserido é o **primeiro a ser removido**.

### Exemplo de pilha:
```py
# Pilha
pilha: list[int] = []

# Inserindo elementos na pilha
pilha.append(1)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
pilha.append(2)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
pilha.append(3)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')

# Removendo elementos da pilha
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()

print('Pilha:', pilha)
```

#### Resultado:
```bash
Pilha: [1] -> Elemento inserido: 1
Pilha: [1, 2] -> Elemento inserido: 2
Pilha: [1, 2, 3] -> Elemento inserido: 3

Pilha: [1, 2, 3] -> Elemento removido: 3
Pilha: [1, 2] -> Elemento removido: 2
Pilha: [1] -> Elemento removido: 1

Pilha: []
```