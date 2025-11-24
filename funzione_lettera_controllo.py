def calcola_lettera_controllo(codice_fiscale_15):
    """
    Calcola la lettera di controllo del codice fiscale italiano a partire dai primi 15 caratteri.

    Args:
        codice_fiscale_15 (str): I primi 15 caratteri del codice fiscale (maiuscolo).

    Returns:
        str: La lettera di controllo.
    """

    if len(codice_fiscale_15) != 15:
        raise ValueError("Il codice fiscale deve contenere esattamente 15 caratteri")

    # Valori dispari (posizioni 1,3,5,...), indicizzati da 0 -> posizioni pari in Python
    valori_dispari = {
        '0': 1,  '1': 0,  '2': 5,  '3': 7,  '4': 9,  '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
        'A': 1,  'B': 0,  'C': 5,  'D': 7,  'E': 9,  'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
        'K': 2,  'L': 4,  'M': 18, 'N': 20, 'O': 11, 'P': 3,  'Q': 6,  'R': 8,  'S': 12, 'T': 14,
        'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
    }

    # Valori pari (posizioni 2,4,6,...), indicizzati da 0 -> posizioni dispari in Python
    valori_pari = {
        '0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,  '7': 7,  '8': 8,  '9': 9,
        'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,  'F': 5,  'G': 6,  'H': 7,  'I': 8,  'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

    # Lettere di controllo corrispondenti al valore modulo 26
    lettere_controllo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    codice_fiscale_15 = codice_fiscale_15.upper()

    totale = 0
    for i, char in enumerate(codice_fiscale_15):
        if i % 2 == 0:  # posizione dispari (indice 0-based)
            valore = valori_dispari.get(char)
        else:  # posizione pari
            valore = valori_pari.get(char)

        if valore is None:
            raise ValueError(f"Carattere '{char}' non valido nel codice fiscale")

        totale += valore

    indice_lettera = totale % 26
    return lettere_controllo[indice_lettera]
```

### Esempio d'uso:
```python
cf_15 = "RSSMRA85M01H501"  # primi 15 caratteri del codice fiscale
lettera_controllo = calcola_lettera_controllo(cf_15)
print(f"Lettera di controllo: {lettera_controllo}")  # Output previsto: T