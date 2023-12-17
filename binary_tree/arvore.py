from typing import List, Union, Optional

class ArvoreBinaria:
    def __init__(self, valor: float) -> None:
        """Inicializa a árvore binária

        Args:
            valor (float): valor do nó raiz
        """
        self.valor = valor
        self.direita = None
        self.esquerda = None
    
    def heapify(self) -> None:
        """Performa o heapify, criando a estrutura heap. Nota-se que
        ele não garante que a árvore se torne um max-heap, esse seria papel do
        algoritmo Build Max Heap
        """
        largest = self.valor
        
        if self.esquerda is not None and self.esquerda.valor > largest:
            largest = self.esquerda.valor
        
        if self.direita is not None and self.direita.valor > largest:
            largest = self.direita.valor
        
        if largest != self.valor:
            """efetua a troca e chama recursivamente o heapify até que não haja
            necessidade de troca (esteja em heap)"""
            self.valor, largest = largest = self.valor
            self.heapify()
    
    def to_array(self) -> List[float]:
        lista = []
        if self is not None:
            lista.append(self.valor)
            if self.esquerda is not None:
                lista.extend(self.esquerda.to_array())
            if self.direita is not None:
                lista.extend(self.direita.to_array())
        return lista
    
    def print_tree(self) -> None:
        pass
    
    
def construir_recursiva(i, arr):
    if i >= len(arr):
        return None
    arvore = ArvoreBinaria(arr[i])
    arvore.esquerda = construir_recursiva(2*i+1, arr)
    arvore.direita = construir_recursiva(2*i+2, arr)
    return arvore

def construir_arvore(arr):
    return construir_recursiva(0, arr)