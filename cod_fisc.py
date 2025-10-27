while True:
    print("se hai un solo nome premi \"1\" se no \"2\"")
    scelta= input()
    if scelta == "1":
        nome_cognome = input()
        nome,cognome = nome_cognome.split()
        break
    elif scelta == "2":
        nome_multi = input("inserisci i nomi\n")
        cognome_multi = input("inserisci i cognomi\n")
        nome = nome_multi.replace(" ", "")
        cognome = cognome_multi.replace(" ", "")
        break
    else: print("Errore riprova")
        
#print(nome_cognome.split())
#nome,cognome = nome_cognome.split()[0],nome_cognome.split()[1]
    
anno = input("Inserisci anno in formato aaaa :")

nome_maiusc = nome.upper()
cognome_maiusc = cognome.upper()
print(nome_maiusc)
print(cognome_maiusc)

codice_ficale = ""
contatore = 0

for lettera in cognome_maiusc:
    if lettera not in "AEIOU":
        codice_ficale += lettera
        contatore +=1
        if contatore == 3: break
for lettera in cognome_maiusc:
    if lettera in "AEIOU" and len(codice_ficale)<3:
        codice_ficale += lettera
while len(codice_ficale) <3:
    codice_ficale += "X"
        
cons_nome = ""
indici_nome = [0,2,3]
        
for lettera in nome_maiusc:
    if lettera not in "AEIOU":
        cons_nome += lettera
        
if len(cons_nome) < 4:
    for i in range(len(cons_nome)):
        codice_ficale += cons_nome[i]
if len(cons_nome) >= 4:
    for i in [0,2,3]:
        codice_ficale += cons_nome[i]
    
for lettera in nome_maiusc:
    if lettera in "AEIOU" and len(codice_ficale)<6:
        codice_ficale += lettera

while len(codice_ficale) <6:
    codice_ficale += "X"
    

codice_ficale += anno[2:]

        
print(codice_ficale)