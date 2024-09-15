#o arquivo palavras.txt contém o texto integral do conto "A Cartomante" de Machado de Assis
#disponível em http://www.dominiopublico.gov.br/download/texto/bv000257.pdf
#

#3i
lista = list()

with open('palavras.txt','r',encoding='utf8') as arq:
    for linha in arq:
        linha = linha.strip()
        linha = linha.upper() 
        #3c
        palavras = linha.split()
        #3d
        for p in palavras:
            lista.append(p)

#Sort Nativo
res = lista.sort()

#criação do arquivo com as palavras ordenadas
arq = open('palavrasordenadas.txt','w',encoding='utf8')
for l in lista:
    arq.write(l+'\n')
arq.close()