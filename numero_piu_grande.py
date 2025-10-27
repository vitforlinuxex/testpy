lista_numeri = []
while True:
        num = int(input("inserisci un numero positivo negativo per uscire\n"))
        if num<0: break
        lista_numeri.append(num)
        
print ("il numero più grande è", max(lista_numeri))