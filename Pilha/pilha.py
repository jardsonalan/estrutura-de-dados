# Pilha
pilha: list[int] = []

print('Pilha vazia:', pilha)

pilha.append(1)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
pilha.append(2)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
pilha.append(3)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
pilha.append(4)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
pilha.append(5)
print(f'Pilha: {pilha} -> Elemento inserido: {pilha[-1]}')
print('')

print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print(f'Pilha: {pilha} -> Elemento removido: {pilha[-1]}')
pilha.pop()
print('Pilha vazia:', pilha)