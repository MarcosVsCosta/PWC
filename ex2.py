frase = str(input())
vetor = []
comprimento = len(frase)
contador = 0
resposta = ""

for i in frase:
    vetor.append(i)
    
while contador < comprimento:
    auxiliar = contador + 1
    while auxiliar < comprimento :
        #print (vetor[contador], vetor[auxiliar], contador, auxiliar)
        if vetor[contador] == vetor[auxiliar] :
            vetor.pop(auxiliar)
            comprimento = len(vetor)
            auxiliar -= 1
        auxiliar += 1
    contador += 1

for i in vetor:
    resposta = resposta + i

print (resposta)
