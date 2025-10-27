#riparato

print("Inserire parole, quando voi smettere premi 0.")
lista_parole=[]

for x in range(100):
    parola = input()
    if parola == "0": break
    lista_parole.append(parola)
    
print(lista_parole)


for i in range(len(lista_parole)):
    for j in range(len(lista_parole)):
        if j > i:
            if len(lista_parole[i]) > len(lista_parole[j]):
                lista_parole[i],lista_parole[j] = lista_parole[j],lista_parole[i]

         
print("fine", lista_parole)
