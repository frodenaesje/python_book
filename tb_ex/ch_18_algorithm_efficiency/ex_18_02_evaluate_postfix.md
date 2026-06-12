# Oppgave: Evaluering av postfiks-uttrykk

## Beskrivelse

Postfiks-notasjon (også kjent som "Reverse Polish Notation") er en måte å skrive matematiske uttrykk på hvor operatoren kommer **etter** operandene, i stedet for mellom dem som i vanlig infiksnotasjon.

### Eksempler:
- **Infiksnotasjon**: `3 + 5` → **Postfiksnotasjon**: `3 5 +`
- **Infiksnotasjon**: `(2 + 3) * 4` → **Postfiksnotasjon**: `2 3 + 4 *`
- **Infiksnotasjon**: `10 - 5 + 2` → **Postfiksnotasjon**: `10 5 - 2 +`

## Oppgave

Implementer en funksjon som evaluerer postfiks-uttrykk ved hjelp av en **stakk** (stack).

### Algoritme:
1. Opprett en tom stakk for operander
2. For hvert symbol i uttrykket:
   - Hvis det er en operand (tall): legg det på stakken
   - Hvis det er en operator (+, -, *, /): 
     - Hent de to øverste operandene fra stakken
     - Utfør operasjonen
     - Legg resultatet tilbake på stakken
3. Returner det siste elementet i stakken (resultatet)

### Pseudokode:

```
function evaluateExpression(expression):
    stack = new Stack()
    tokens = expression.split()
    
    for each token in tokens:
        if token is operator:
            pop two operands, apply operator, push result
        else:
            push number to stack
    
    return stack.pop()
```

### Eksempel-kjøring:
```
Enter an expression: 15 7 1 1 + - / 3 * 2 1 1 + + -
15 7 1 1 + - / 3 * 2 1 1 + + - = 5.0
```

### Instruksjoner:
- Bruk `Stack`-klassen til å implementere stakkfunksjonalitet
- Funksjonen `insertBlanks()` skal legge inn mellomrom rundt operatorer
- Implementer `processAnOperator()` for å håndtere operasjoner
- Håndter feil (f.eks. ugyldige uttrykk)

## Løsningshint

Programmet skal:
1. Lese et matematisk uttrykk fra bruker
2. Konvertere infiksnotasjon til postfiksnotasjon (eller ta inn postfiks direkte)
3. Evaluere postfiks-uttrykket
4. Skrive ut resultatet

### Hint: `insert_blanks()` funksjon

For å gjøre parsing enklere, bruk denne hjelpefunksjonen som legger inn mellomrom omkring operatorene:

```python
def insert_blanks(s):
    """Insert blanks around operators (+, -, *, /) for easier parsing"""
    result = ""
    
    for ch in s:
        if ch == '+' or ch == '-' or ch == '*' or ch == '/':
            result += " " + ch + " "
        else:
            result += ch
    
    return result
```

**Eksempel på bruk:**
- Input: `"355/7+3"`
- Output: `"355 / 7 + 3"`

Deretter kan du bruke `.split()` for å få en liste med tokens som er enkle å prosessere.

Se løsningsfilen `ex_18_02_evaluate_postfix.py` for fullstendig implementasjon.
