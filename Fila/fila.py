from collections import deque

# Fila
fila: deque[int] = deque([])

print('Fila vazia:', fila)

fila.append(1)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
fila.append(2)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
fila.append(3)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
fila.append(4)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
fila.append(5)
print(f'Fila: {fila} -> Elemento inserido: {fila[-1]}')
print('')

print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print(f'Fila: {fila} -> Elemento removido: {fila[0]}')
fila.popleft()
print('Fila vazia:', fila)