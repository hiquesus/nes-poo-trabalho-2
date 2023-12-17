from typing import List, Union, Optional
from collections import deque

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
        
        if self.esquerda != None and self.esquerda.valor > largest:
            largest = self.esquerda.valor
        
        if self.direita != None and self.direita.valor > largest:
            largest = self.direita.valor
        
        if largest != self.valor:
            """efetua a troca e chama recursivamente o heapify até que não haja
            necessidade de troca (esteja em heap)"""
            self.valor, largest = largest, self.valor
            self.heapify()

    """def build_max_heap(self) -> None:
        for i in range(len(self.to_array() // 2 - 1), -1, -1):
            self.heapify(i)"""
    
    def to_array(self) -> List[float]:
        """Transforma o objeto árvore binária em forma de lista

        Returns:
            List[float]: lista com os valores da árvore
        """
        lista = []
        fila = deque([self])
        while fila:
            no_atual = fila.popleft()
            if no_atual:
                lista.append(no_atual.valor)
                fila.append(no_atual.esquerda)
                fila.append(no_atual.direita)
            else:
                lista.append(None)
        while lista and lista[-1] == None:
            lista.pop()
        return lista
        

    def print_tree(self, space=0) -> None:
        """Método recursivo que imprime toda a árvore

        Args:
            space (int, optional): Espaço para cada 'andar' da árvore.
        """
        if self:
            space += 1
            if self.direita:
                self.direita.print_tree(space)
            print(" " * 5 * space + str(self.valor))
            if self.esquerda:
                self.esquerda.print_tree(space)

    
def construir_recursiva(i, arr):
    if i >= len(arr):
        return None
    # inicia a árvore
    arvore = ArvoreBinaria(arr[i])
    # caso exista, cria as subarvores esq e dir (caso existam na lista)
    if arvore.valor:
        if 2*i+1 <= len(arr):
            arvore.esquerda = construir_recursiva(2*i+1, arr)
        if 2*i+2 <= len(arr):
            arvore.direita = construir_recursiva(2*i+2, arr)
    # retorna a árvore criada
    return arvore

def construir_arvore(arr):
    # função que inicia a construção da árvore, chamando recursivamente
    # construir_recursiva com i = 0.
    return construir_recursiva(0, arr)