import binary_tree as bt

# EXEMPLO COM UM ARRAY SIMPLES
print("EXEMPLO 1:")
arr_simples = [1, 2, 3, 4, 5, 6, 7]
arvore_simples = bt.construir_arvore(arr_simples)
print(f"Array da árvore: {arvore_simples.to_array()} \n Representação Gráfica:")
arvore_simples.print_tree()
arvore_simples.heapify()
print(f"Array da árvore (pós heapify): {arvore_simples.to_array()} \n Representação Gráfica:")
arvore_simples.print_tree()

#EXEMPLO COM UM ARRAY MAIS COMPLEXO
print("EXEMPLO 2:")
arr_maior = [5, 15, None, 10, 1, None, None, None, 100]
arvore_maior = bt.construir_arvore(arr_maior)
print(f"Array da árvore: {arvore_maior.to_array()} \n Representação Gráfica:")
arvore_maior.print_tree()
arvore_maior.heapify()
print(f"Array da árvore (pós heapify): {arvore_maior.to_array()} \n Representação Gráfica:")
arvore_maior.print_tree()