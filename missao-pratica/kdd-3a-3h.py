import time

#aproveitei os códigos criados nas microatividades 2 e 3 e os coloquei no arquivo 
#metodosordenacao.py
from metodosordenacao import bubbleSort, selectionSort

#o arquivo palavras.txt contém o texto integral do conto "A Cartomante" de Machado de Assis
#disponível em http://www.dominiopublico.gov.br/download/texto/bv000257.pdf
#

#3a
lista = list()
#3b
with open('palavras.txt','r',encoding='utf8') as arq:
    for linha in arq:
        linha = linha.strip()
        linha = linha.upper() 
        #3c
        palavras = linha.split()
        #3d
        for p in palavras:
            lista.append(p)

#lista original
print('='*10,' LISTA ORIGINAL ','='*10)
print(f'Contém {len(lista)} palavras')
print()

#Bubble Sort
inicio = time.time()
res = bubbleSort(lista)
fim = time.time()
tempo_bubblesort = fim - inicio
print('='*10,' TEMPO BUBBLE SORT ','='*10)
print(tempo_bubblesort)
#Selection Sort
inicio = time.time()
res = selectionSort(lista)
fim = time.time()
tempo_selectionsort = fim - inicio
print('='*10,' TEMPO SELECTION SORT ','='*10)
print(tempo_selectionsort)
#Sort Interno
inicio = time.time()
res = lista.sort()
fim = time.time()
tempo_sortnativo = fim - inicio
print('='*10,' TEMPO SORT NATIVO ','='*10)
print(tempo_sortnativo)
