frase = str(input())
resposta = ""
comprimento = len(frase)-1

while comprimento >= 0:
    auxiliar = comprimento
    if frase[comprimento] == " ":
        auxiliar += 1
        while (auxiliar < len(frase)) and (frase[auxiliar] != " " ) :
            resposta = resposta + frase[auxiliar]
            auxiliar += 1
        resposta = resposta + " " 
    comprimento -= 1

comprimento = 0
while frase[comprimento] != " ":
    resposta = resposta + frase[comprimento]
    comprimento += 1

print (resposta)
