"""
Oppgave:
Lag et program som gjetter brukerens fødselsdag (dag i måneden, 1-31) ved å presentere 5 tabeller med tall.
Brukeren svarer om hans/hennes dag finnes i hver tabell, og programmet regner ut dagen basert på svarene.
Tema: lister, for-løkke, logikk
"""
def get_y_n():
    while True:
        svar = input("Er din fødselsdag i denne tabellen? (j/n): ").strip().lower()
        if svar in ('j', 'n'):
            return svar
        print("Ugyldig svar. Vennligst svar med 'j' eller 'n'.")


print("Gjett din fødselsdag!")
print("Svar med 'ja' eller 'nei' på om din dag finnes i tabellen.")

tabell1 = [n for n in range(1, 32) if n & 1]
tabell2 = [n for n in range(1, 32) if n & 2]
tabell3 = [n for n in range(1, 32) if n & 4]
tabell4 = [n for n in range(1, 32) if n & 8]
tabell5 = [n for n in range(1, 32) if n & 16]

dag = 0
print("\nTabell 1:", tabell1)
if get_y_n() == 'j':
    dag += 1
print("\nTabell 2:", tabell2)
if get_y_n() == 'j':
    dag += 2
print("\nTabell 3:", tabell3)
if get_y_n() == 'j':
    dag += 4
print("\nTabell 4:", tabell4)
if get_y_n() == 'j':
    dag += 8
print("\nTabell 5:", tabell5)
if get_y_n() == 'j':
    dag += 16

print(f"\nDu er født den {dag} i måneden!")