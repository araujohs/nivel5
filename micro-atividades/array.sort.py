#5.a até 5.e
n = [218,303,232,198,998,451,346,668,190,694,601,629,834,565,39]
n.sort()
#print(n)

n.sort(key=None,reverse=True)
#print(n)

#5.f
pessoa = ['nome','dataNascimento','cpf','rg',
          'endereco','telefone','email','cidade',
          'estado','cep','pais','bairro','numero',
          'complemento','profissao']
pessoa.sort()
print(pessoa)

pessoa.sort(key=None,reverse=True)
print(pessoa)
