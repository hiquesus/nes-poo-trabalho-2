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
        """Performa o heapify, criando uma estrutura heap. Nota-se que
        ele não garante que a árvore se torne um max-heap, esse seria papel do
        algoritmo Build Max Heap
        """
        if self.valor != None:
            largest_val = self.valor
            lar = self

            if self.esquerda and self.esquerda.valor:
                if self.esquerda.valor > largest_val:
                    largest_val = self.esquerda.valor
                    lar = self.esquerda
            
            if self.esquerda and self.direita.valor:
                if self.direita.valor > largest_val:
                    largest_val = self.direita.valor
                    lar = self.direita
            
            if largest_val != self.valor:
                """efetua a troca e chama recursivamente o heapify até que não haja
                necessidade de troca (o nó esteja em heap)"""
                self.valor, lar.valor = lar.valor, self.valor
                lar.heapify()
    
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
        # remove os "None's" do final da array,
        # deixando somente os necessários; e.g.: [1, 2, 3, None, 4]
        while lista and lista[-1] == None:
            lista.pop()
        return lista
        

    def print_tree(self, space: int = 0) -> None:
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
    

def construir_recursiva(i: int, arr: List[float]) -> ArvoreBinaria:
    """chama recursivamente até a árvore ser construida

    Args:
        i (int): posição do atual i da árvore
        arr (List[float]): array em formato de árvore binária

    Returns:
        ArvoreBinaria: Retorna o objeto da árvore
    """
    if i >= len(arr):
        return None
    # inicia a árvore
    arvore = ArvoreBinaria(arr[i])
    # caso exista, cria as subarvores esq e dir (caso existam na lista)
    if arvore.valor:
        if 2*i+1 < len(arr):
            arvore.esquerda = construir_recursiva(2*i+1, arr)
        if 2*i+2 < len(arr):
            arvore.direita = construir_recursiva(2*i+2, arr)
    # retorna a árvore criada
    return arvore

def construir_arvore(arr: List[float]) -> ArvoreBinaria:
    """função que inicia a construção da árvore, 
    chamando construir_recursiva com i = 0.

    Args:
        arr (List[float]): array inicial em formato de árvore binária

    Returns:
        ArvoreBinaria: o objeto final da árvore completa
    """
    return construir_recursiva(0, arr)
