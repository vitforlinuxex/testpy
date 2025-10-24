print("Inserire parola da invertire")
parola = input()
parola_invertita = ""

for i in range(-1, -len(parola)-1, -1): #ciclo
    #print(i)
    parola_invertita = parola_invertita + parola[i]

print(parola_invertita)