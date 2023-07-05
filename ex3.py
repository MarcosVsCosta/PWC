frase = str(input())
comparacao = ""
comprimento = len(frase)
contador = 0
resposta = ""

def palindromo (teste):
    teste = teste.lower().replace(' ','')
    teste_invertido = teste[::-1]

    if teste == teste_invertido and len(teste) > 1:
        return(teste)
    else:
        return ("")
    

while contador < comprimento:
    auxiliar = contador
    teste = ""
    while auxiliar < comprimento:
        teste = teste + frase[auxiliar]
        auxiliar += 1
        comparacao = palindromo(teste)
        if len(comparacao) > len(resposta):
            resposta = comparacao
    contador = contador + 1

 
print (resposta)
