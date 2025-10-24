def find_shortest_word(word_list):
    return min(word_list, key=len)

# Esempio di utilizzo:
print("Inserire parole, quando voi smettere premi 0.")
lista_parole=[]
for x in range(100):
    parola = input()
    if parola == "0": break
    lista_parole.append(parola)
piu_corto = find_shortest_word(lista_parole)
print(f"La parola più corta è: {piu_corto}")