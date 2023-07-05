frase = str(input())
vetor = []
comprimento = len(frase)
contador = 0
resposta = ""


for i in frase:
    vetor.append(i)

for i in vetor:
    if contador == 0 and ord(i)>89 and ord(i)<123 :
        resposta = resposta + i.upper()
        contador += 1
    else:
        resposta = resposta + i
    if i == "." or i == "!" or i == "?":
        contador = 0

print(resposta)
    
        
