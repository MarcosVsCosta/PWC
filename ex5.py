frase = str(input())
alinhada = sorted(frase)
impar = 0

#print(alinhada)

for i in alinhada:
    #print (alinhada.count(i))
    if (alinhada.count(i) % 2) == 1:
        impar += 1

if impar == 1 and (len(alinhada)%2)== 1:
    print ("true")
else:
    print("false")
