while True:
    print("ciao inserisci due numeri 0 se vui uscire")
    num1 = input()
    num2 = input()
    if num1=="0" or num2=="0": break
    if num1.isdigit() and num2.isdigit():
        print(f"ls somma di{int(num1)} e {int(num2)} é {int(num1)+int(num2)}")
    else: print("Errore")