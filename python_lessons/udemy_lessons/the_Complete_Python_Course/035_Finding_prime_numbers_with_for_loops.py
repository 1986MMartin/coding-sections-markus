for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")

# Funktionsweise des Programms,
# Zeile 1 : n bekommt ab 3 bis 9 die Zahlen zugewiesen pro Durchlauf
# Zeile 2 : x bekommt die Anzahl der durchläufe von 2 bis n zugewiesen
# Zeile 3 : Wenn Abfrage ob der Modolu % Wert von n und x == 0 ist
# Zeile 4 : Wenn Modolu Wert == 0 ist, dann wird String ausgegeben der besagt, dass n keine Primzahl ist, da sie durch x getielt werden kann
# Zeile 6 : else: bezieht sich auf die for x in range(2, n) Schleife
# Zeile 7 : wenn else greift, dann wird ausgegeben das es sich um eine Primzahl handelt.
