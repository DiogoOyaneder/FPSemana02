frase1 = (input(""))
frase2 = (input(""))
a = frase1.split()
b = frase2.split()
intersecao = []
for palavra in a:
    if palavra in b and palavra not in intersecao:
        intersecao.append(palavra)
print (intersecao)