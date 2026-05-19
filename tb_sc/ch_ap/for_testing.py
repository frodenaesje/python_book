# Diverse oppgaver list / dict / set: loops eller comprehensions

# Lag en ny liste odde_tall som inneholder alle odde tall fra matrisen
# - som en flat liste, ikke en matrise.
# Tips: du trenger to for-klausuler i comprehension.
# Forventet resultat: [1, 3, 5, 7, 9, 11]

matrise = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]
odde_tall = []
for rad in  matrise:
    for tall in rad:
        if tall % 2 != 0:
            odde_tall.append(tall)
print(odde_tall)

odde_tall = [tall for rad in matrise for tall in rad if tall % 2 != 0]
print(odde_tall)

# Lag en dictionary tilgjengelig der nøkkelen er produkt-ID og verdien er produktnavnet - men kun for produkter
# som er på lager (lager > 0) og koster under 1000 kr.

produkter = [
    {"id": "A101", "navn": "Tastatur", "pris": 899, "lager": 12},
    {"id": "B205", "navn": "Skjerm", "pris": 4990, "lager": 0},
    {"id": "C310", "navn": "Mus", "pris": 449, "lager": 34},
    {"id": "D412", "navn": "Headset", "pris": 1299, "lager": 0},
    {"id": "E517", "navn": "Webkamera", "pris": 699, "lager": 7},
]

tilgjengelig = {}
for dict in produkter:
    for key, value in dict.items():
        if key == "lager" and value > 0 and dict["pris"] < 1000:
            tilgjengelig[dict["id"]] = dict["navn"]
print(tilgjengelig)

tilgjengelig = {key:value for key, value in dict.items() if key == "lager" and value > 0 and dict["pris"] < 1000}
print(tilgjengelig)

tilgjengelig = {produkt["id"]: produkt["navn"] for produkt in produkter if produkt["lager"] > 0 and produkt["pris"] < 1000}
print(tilgjengelig)

