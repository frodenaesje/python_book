# file: sc_07_11_comprehensions_examples.py

# ── Oppgave 1 - List comprehension ───────────────────────────────────────────

# Gitt denne listen med ansatte
ansatte = [
    {"navn": "Kari",  "avdeling": "IT",  "lønn": 620000},
    {"navn": "Ola",   "avdeling": "HR",  "lønn": 540000},
    {"navn": "Lise",  "avdeling": "IT",  "lønn": 710000},
    {"navn": "Per",   "avdeling": "HR",  "lønn": 490000},
    {"navn": "Anne",  "avdeling": "IT",  "lønn": 580000},
]

# Oppgave:
# Lag en liste it_navn som inneholder navnene på alle ansatte i IT-avdelingen,
# men kun de som tjener over 600 000. Navnene skal være med store bokstaver.
# Forventet resultat: ["KARI", "LISE"]

# Forslag til løsning
it_navn = [a["navn"].upper() for a in ansatte
           if a["avdeling"] == "IT" and a["lønn"] > 600000]
print(it_navn)


# ── Oppgave 2 - List comprehension, to dimensjoner ───────────────────────────

# Gitt denne matrisen
matrise = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
]

# Oppgave:
# Lag en ny liste odde_tall som inneholder alle odde tall fra matrisen
# - som en flat liste, ikke en matrise.
# Tips: du trenger to for-klausuler i comprehension.
# Forventet resultat: [1, 3, 5, 7, 9, 11]

# Forslag til løsning
odde_tall = [tall for rad in matrise for tall in rad if tall % 2 != 0]
print(odde_tall)


# ── Oppgave 3 - Set comprehension ────────────────────────────────────────────

# Gitt denne listen med logglinjer fra en server
logger = [
    "ERROR   192.168.1.1  disk full",
    "WARNING 192.168.1.2  high load",
    "ERROR   192.168.1.1  disk full",
    "INFO    192.168.1.3  backup ok",
    "ERROR   192.168.1.4  timeout",
    "WARNING 192.168.1.2  high load",
    "ERROR   192.168.1.1  disk full",
]

# Oppgave:
# Lag et set feil_ip som inneholder IP-adressene til alle linjer som starter
# med "ERROR". Duplikater skal fjernes automatisk.
# Tips: linje.split() deler linjen på mellomrom.
# Forventet resultat: {"192.168.1.1", "192.168.1.4"}

# Forslag til løsning
feil_ip = {linje.split()[1] for linje in logger if linje.startswith("ERROR")}
print(feil_ip)


# ── Oppgave 4 - Dict comprehension ───────────────────────────────────────────

# Gitt denne listen med produkter
produkter = [
    {"id": "A101", "navn": "Tastatur",  "pris": 899,  "lager": 12},
    {"id": "B205", "navn": "Skjerm",    "pris": 4990, "lager": 0},
    {"id": "C310", "navn": "Mus",       "pris": 449,  "lager": 34},
    {"id": "D412", "navn": "Headset",   "pris": 1299, "lager": 0},
    {"id": "E517", "navn": "Webkamera", "pris": 699,  "lager": 7},
]

# Oppgave:
# Lag en dictionary tilgjengelig der nøkkelen er produkt-ID og verdien er
# produktnavnet - men kun for produkter som er på lager (lager > 0)
# og koster under 1000 kr.
# Forventet resultat: {"A101": "Tastatur", "C310": "Mus", "E517": "Webkamera"}

# Forslag til løsning
tilgjengelig = {item["id"]: item["navn"] for item in produkter
                if item["lager"] > 0 and item["pris"] < 1000}
print(tilgjengelig)
