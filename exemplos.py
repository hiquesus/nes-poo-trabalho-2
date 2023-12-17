import binary_tree as bt

# EXEMPLO COM UM ARRAY SIMPLES
print("EXEMPLO 1: \n")
arr_simples = [1, 2, 3, 4, 1, 9, 7]
arvore_simples = bt.construir_arvore(arr_simples)
print(f"Array da árvore: {arvore_simples.to_array()} \n Representação Gráfica:")
arvore_simples.print_tree()
arvore_simples.heapify()
print(f"Array da árvore (pós heapify): {arvore_simples.to_array()} \n Representação Gráfica:")
arvore_simples.print_tree()
print(f"Lista ordenada: {sorted(arvore_simples.to_array())}\n")

#EXEMPLO COM UM ARRAY MAIS COMPLEXO
print("EXEMPLO 2: \n")
arr_maior = [5, 150, None, 100, 1, None, None, None, 10]
arvore_maior = bt.construir_arvore(arr_maior)
print(f"Array da árvore: {arvore_maior.to_array()}")
arvore_maior.heapify()
print(f"Array da árvore (pós heapify): {arvore_maior.to_array()} \n Representação Gráfica:")
arvore_maior.print_tree()