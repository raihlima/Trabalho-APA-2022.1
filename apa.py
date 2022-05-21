# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import pandas as pd

quantidadeVertices = 100
quantidadeMaxLigacao = 3

"""
1 – Gerar randomicamente um grafo não orientado com 100 vértices , com um número baixo
de ligações ( de uma a dez vezes o número de vértices ).
2 – Implementar um algoritmo que gere a representação matricial ( matriz adjacência binária )
"""
def grafo():
    global matriz
    matriz = []
    linha = []
    for x in range (quantidadeVertices):
        linha.append(0)
    for x in range (quantidadeVertices):
        matriz.append(linha.copy())
        
    
    
    for x in range (quantidadeVertices):
        quantidadeLigacao = random.randint(1, quantidadeMaxLigacao)
        for y in range (quantidadeLigacao):
            k = random.randint(0, quantidadeVertices-1)
            if k != x:
                matriz[x][k] = 1
                matriz[k][x] = 1
            
def verificaNumeroLigacoes():
    
    for x in range (quantidadeVertices):
        numeroLigacao = 0
        for y in range (quantidadeVertices):
            if matriz[x][y] == 1:
                numeroLigacao = numeroLigacao +1
        if numeroLigacao>10:
            removeLigacao(x, numeroLigacao)
            
def verificaNumeroLigacoesAux(y):
    numeroLigacao = 0
    for x in range (quantidadeVertices):
        if matriz[x][y] == 1:
            numeroLigacao = numeroLigacao +1
    if numeroLigacao > 1:
        return bool(True)
    else:
        return bool(False)



def removeLigacao(x, numeroLigacao):
    for y in range (quantidadeVertices):
        if matriz[x][y] == 1:
            if verificaNumeroLigacoesAux(y):
                matriz[x][y] = 0
                matriz[y][x] = 0
                numeroLigacao = numeroLigacao - 1
                if numeroLigacao <=10:
                    break
    if numeroLigacao > 10:
        grafo()
        
"""
3 – Implementar um algoritmo que, a partir da matriz, gere a representação vetorial ( vetor
binário )de sua parte triangular superior.
"""
def gerarRepresentacaoVetorial():
    vetor = []
    for x in range(1,quantidadeVertices):
        for y in range(x, quantidadeVertices):
            vetor.append(matriz[x][y])
    return vetor

def main():
    grafo()
    verificaNumeroLigacoes()

if __name__ == "__main__":
    main()
