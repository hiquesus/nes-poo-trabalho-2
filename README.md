# Trabalho 02 de OOP no NES

Pacote que implementa a classe árvore binária e uma função para construi-la com base em um array.

## Instalação

Para instalar execute:

```
python setup.py install
```

## Uso

Exemplo de uso do módulo `binary_tree` com uma árvore binária simples:

```py
import binary_tree as bt

arr_simples = [1, 2, 3, 4, 5, 6, 7]
arvore_simples = bt.construir_arvore(arr_simples)
print(f"Array da árvore: {arvore_simples.to_array()} \n Representação Gráfica:")
arvore_simples.print_tree()
arvore_simples.heapify()
print(f"Array da árvore (pós heapify): {arvore_simples.to_array()} \n Representação Gráfica:")
arvore_simples.print_tree()
```