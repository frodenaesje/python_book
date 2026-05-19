# File: sc_07_01_tuple_from_file.py
# Demonstrasjon av å opprette tupler fra fil

# Eksempel 1: Lese tall fra fil og konvertere til tuple
def read_numbers_from_file(filnavn):
    """Leser tall fra fil (ett tall per linje) og returnerer som tuple"""
    with open(filnavn, 'r') as f:
        numbers = tuple(int(line.strip()) for line in f if line.strip())
    return numbers

# Eksempel 2: Lese linjer som tuple (strenger)
def read_lines_as_tuple(filnavn):
    """Leser alle linjer fra fil og returnerer som tuple av strenger"""
    with open(filnavn, 'r') as f:
        lines = tuple(line.rstrip('\n') for line in f)
    return lines

# Eksempel 3: Lese CSV-data og opprette tuple av tupler
def read_csv_as_tuples(filnavn):
    """Leser CSV-fil og returnerer tuple av tupler (hver rad)"""
    with open(filnavn, 'r') as f:
        rows = tuple(tuple(value.strip() for value in line.split(',')) 
                     for line in f if line.strip())
    return rows

# Eksempel 4: Lese og dele data i kolumner
def read_columns_as_tuple(filnavn, delimiter=','):
    """Leser fil og returnerer tuple der hver element er en kolonne"""
    with open(filnavn, 'r') as f:
        rows = [tuple(value.strip() for value in line.split(delimiter)) 
                for line in f if line.strip()]
    
    if not rows:
        return ()
    
    # Transponerer for å få kolonner
    columns = tuple(zip(*rows))
    return columns

# Eksempel 5: Enkel way - bruk tuple() direkte på fil
def read_file_simple(filnavn):
    """Enkleste måte - lese hele filen som tuple av linjer"""
    with open(filnavn, 'r') as f:
        return tuple(f)

# TEST-EKSEMPLER
if __name__ == "__main__":
    # Opprett en testfil
    test_file = "test_data.txt"
    with open(test_file, 'w') as f:
        f.write("10\n20\n30\n40\n50\n")
    
    # Les tall fra fil
    tall = read_numbers_from_file(test_file)
    print("Tall fra fil:", tall)
    print("Type:", type(tall))
    print("Første tall:", tall[0])
    print()
    
    # Opprett en CSV-testfil
    csv_file = "test_data.csv"
    with open(csv_file, 'w') as f:
        f.write("Navn,Alder,By\n")
        f.write("Alice,25,Oslo\n")
        f.write("Bob,30,Bergen\n")
        f.write("Charlie,28,Stavanger\n")
    
    # Les CSV som tupler
    data = read_csv_as_tuples(csv_file)
    print("CSV data som tupler:")
    for rad in data:
        print(rad)
    print()
    
    # Les kolonner
    columns = read_columns_as_tuple(csv_file)
    print("Kolonner fra CSV:")
    for i, col in enumerate(columns):
        print(f"Kolonne {i}:", col)
