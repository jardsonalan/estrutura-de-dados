## Fila
Fila é uma estrutura de dados do tipo **FIFO** (*First In, First Out*), ou seja, o **primeiro elemento** inserido é o **primeiro a ser removido**.

### Exemplo de fila:
**Observação:** Para implementar uma fila em python, usamos a classe `collections.deque` que foi projetada para permitir appends e pops eficientes nas duas extremidades;

```py
from collections import deque

# Fila
fila: deque[int] = deque([])

# Inserindo elementos na fila
fila.append(1)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
fila.append(2)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
fila.append(3)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')

# Removendo elementos da fila
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()

print(f'Fila: {fila}')
```

#### Resultado:
```bash
Fila: deque([1]) -> Elemento inserido: 1
Fila: deque([1, 2]) -> Elemento inserido: 2
Fila: deque([1, 2, 3]) -> Elemento inserido: 3

Fila: deque([1, 2, 3]) -> Elemento removido: 1
Fila: deque([2, 3]) -> Elemento removido: 2
Fila: deque([3]) -> Elemento removido: 3

Fila: deque([])
```