# file: ch_20_02_postfix_notation.py
"""
Oppgave:
Postfix notasjon er en måte å skrive aritmetiske uttrykk på uten parenteser.
Eksempel: (4 + 5) * 3 blir i postfix 4 5 + 3 *

Implementer en funksjon eval_postfix(postfix_expression) som evaluerer postfix uttrykk
ved hjelp av en stack (deque).

Tema: deque, stack, operatorer
"""

from collections import deque


def eval_postfix(postfix_expression):
    """
    Evaluerer et aritmetisk uttrykk skrevet i postfix notasjon.
    
    Algoritme:
    1. Opprett en tom stack kalt evaluation_stack
    2. For hvert tegn i postfix_expression:
       - Hvis token er et tall, legg det til evaluation_stack
       - Hvis token er en operator, pop to operander, utfør operasjonen, 
         og legg resultatet tilbake på evaluation_stack
    3. Når alle tokens er behandlet, skal evaluation_stack inneholde ett element
    
    Args:
        postfix_expression: En streng med tall og operatorer separert med mellomrom.
                           Operatorene er: +, -, *, /, %, ^
    
    Returns:
        Resultatet av beregningen (int)
    
    Eksempler:
        eval_postfix("4 5 +") -> 9        # 4 + 5
        eval_postfix("4 5 + 3 *") -> 27   # (4 + 5) * 3
        eval_postfix("10 2 /") -> 5       # 10 / 2 (heltallsdivisjon)
        eval_postfix("2 3 ^") -> 8        # 2 ^ 3 = 2 ** 3
    """
    evaluation_stack = deque()
    tokens = postfix_expression.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/', '%', '^']:
            # Token er en operator - pop to operander
            operand2 = evaluation_stack.pop()
            operand1 = evaluation_stack.pop()
            
            # Utfør operasjonen
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 // operand2  # Heltallsdivisjon
            elif token == '%':
                result = operand1 % operand2
            elif token == '^':
                result = operand1 ** operand2
            
            # Legg resultatet tilbake på stacken
            evaluation_stack.append(result)
        else:
            # Token er et tall - legg det på stacken
            evaluation_stack.append(int(token))
    
    # Resultatet skal være det eneste elementet igjen på stacken
    return evaluation_stack.pop()


if __name__ == "__main__":
    # Testeksempler
    print("Testing eval_postfix():")
    print(f"4 5 + = {eval_postfix('4 5 +')}")  # 9
    print(f"4 5 + 3 * = {eval_postfix('4 5 + 3 *')}")  # 27
    print(f"10 2 / = {eval_postfix('10 2 /')}")  # 5
    print(f"15 7 % = {eval_postfix('15 7 %')}")  # 1
    print(f"2 3 ^ = {eval_postfix('2 3 ^')}")  # 8
    print(f"3 4 + 5 * 2 - = {eval_postfix('3 4 + 5 * 2 -')}")  # (3 + 4) * 5 - 2 = 33
