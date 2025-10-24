#GNAAAA!!!
#SBAGLIATO
print("Inserire parole, quando voi smettere premi 0.")
lista_parole=[]

for x in range(100):
    parola = input()
    if parola == "0": break
    lista_parole.append(parola)
    
print(lista_parole)
lista_parole2 = lista_parole

lista_parole_ordinate = []
parola_corta = ""

for i in range(len(lista_parole)):
    for j in range(len(lista_parole)):
        if j > i:
            if len(lista_parole[i]) > len(lista_parole[j]):
                lista_parole2.remove(lista_parole[i])
                break
            else:
                lista_parole2.remove(lista_parole[j])
                break 
         
print("fine", lista_parole2)
            #print (i,j)
    #if len(lista_parole[i]) < len(lista_parole[i+1]):
     #   lista_parole_ordinate.append(lista_parole[i])