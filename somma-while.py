condizione = True
while condizione:
    print("ciao inserisci due numeri 0 se vui uscire")
    num1 = int(input())
    num2 = int(input())
    if num1==0 or num2==0: condizione = False
    print(f"ls somma di{num1} e {num2} é {num1+num2}")