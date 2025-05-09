## Recursividade
- É a definição de uma sub-rotina (função ou método) que pode invocar a si mesma;
- A grande vantagem da recursão está na possibilidade de usar um programa de computador finito para definir, analisar ou produzir um estoque potencialmente infinito de sentenças, designs ou outros dados;
- Em geral, uma definição recursiva é definida por casos: um número limitado de casos base e um caso recursivo. Os casos base são geralmente situações triviais e não envolvem recursão.

### Exemplo de recursividade:
- Um exemplo comum usando recursão é a função para calcular o fatorial de um natural (N);
- Nesse caso, no caso base o valor de 0! é 1. No caso recursivo, dado um N > 0, o valor de N! é calculado multiplicando por N o valor de (N-1)!, e assim por diante, de tal forma que N! tem como valor N * (N-1) * (N-2) * ... * (N-N)!, onde (N-N)! representa obviamente o caso base.

```py
# Fatorial
def fatorial(numero: int) -> int:
  if numero == 0:
    return 1
  return numero * fatorial(numero-1)
```