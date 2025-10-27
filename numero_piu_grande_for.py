lista_numeri = []
for i in range(1000):
        num = int(input("inserisci un numero positivo negativo per uscire\n"))
        if num<0: break
        lista_numeri.append(num)
        
print ("il numero più grande è", max(lista_numeri))