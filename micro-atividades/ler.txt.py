'''
#3a
texto = open('loremipsum.txt','r').read()

#3b
print(texto)

#3c
primeira_linha = texto.split('\n')[0]
print(primeira_linha)

#3d
print(texto[:3])
'''

#3e
with open('loremipsum.txt') as arq:
    texto = arq.read()
    print(texto)
