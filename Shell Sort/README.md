## Shell Sort
- Às vezes chamado de "ordenação por incrementos diminutos";
- Melhora a ordenação por inserção ao quebrar a lista original em um número menor de sublistas, as quais são ordenadas usando a ordenação por inserção;
- Em vez de quebrar a lista em sublistas de itens contíguos, o shell short usa um incremento **i**, às vezes chamado de **gap**, para criar uma sublista escolhendo todos os itens que estão afastados **i** itens um dos outros.

### Passo a passo do Shell Sort:
1. Lista desordenada:
    ```py
    [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
    ```

2. Sublistas que serão geradas da lista original:
    ```py
    # 1° Sublista
    [5, 12, 9, 7]

    # 2° Sublista
    [16, 3, 17]

    # 3° Sublista
    [20, 8, 19]
    ```

3. Ordenação das sublistas:
    ```py
    # 1° Sublista
    [5, 7, 9, 12]

    # 2° Sublista
    [3, 16, 17]

    # 3° Sublista
    [8, 19, 20]
    ```

4. Resultado da lista, depois das trocas com gap de 3:
    ```py
    [5, 3, 8, 7, 16, 19, 9, 17, 20, 12]
    ```

5. Lista ordenada, após a ordenação por inserção com incremento de um:
    ```py
    [3, 5, 7, 8, 9, 12, 16, 17, 19, 20]
    ```