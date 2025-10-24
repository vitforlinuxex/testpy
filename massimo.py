print("Inserire quanti numeri")
num = int(input())
lista_numeri = []
print("Inserire i numeri")
for pippo in range(num): #ciclo
    print(pippo)
    numero = int(input())
    lista_numeri.append(numero)
    
#print(lista_numeri)
    
massimo = lista_numeri[0]

for numer in lista_numeri:
    if numero > massimo:
        massimo = numero
        
print("in mumero più grande è", massimo)