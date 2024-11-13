frase = (input(""))
dicionario = {}
for letra in frase:  
    if not letra.isalnum():    
        continue 
    letra = letra.lower()         
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
         dicionario[letra] +=1 
print (dicionario)