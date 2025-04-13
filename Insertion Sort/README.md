## Inserção Ordenada
Pega um elemento do final e insere em uma sequência que já está ordenada, exceto pelo último elemento.

- Lista Desordenada, antes da inserção ordenada: [1, 7, **3**]

- Lista Ordenada, depois da inserção ordenada: [1, **3**, 7]

## Insertion Sort
- O Insertion Sort nada mais é do que a execução do algoritmo de inserção ordenada repetidas vezes;
- O Insertion Sort é in-place, estável e *O* (n²);
- O pior caso da execução deste algoritmo manifesta-se quando a entrada está ordenada em ordem decrescente;
    - No melhor caso, o Insertion Sort é *O* (n). Isso ocorre quando o array já está ordenado.
- Na teoria, Insertion Sort, Selection Sort e Bubble Sort estão na mesma classe de complexidade, qual seja *O* (n²). Na prática, o Insertion Sort apresenta o melhor desempenho entre esses 3 algoritmos.