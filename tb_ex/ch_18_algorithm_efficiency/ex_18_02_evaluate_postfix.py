import Stack

def main():
    expression = input("Enter an expression: ").strip()
    try:
        print(expression, "=", evaluate_expression(expression))
    except:
        print("Wrong expression: ", expression)


def evaluate_expression(expression):
    
    # Create operandStack to store operands
    operandStack = Stack.Stack()
  
    # Insert blanks around +, -, /, and *
    expression = insert_blanks(expression)

    # Extract operands and operators
    tokens = expression.split()

    for token in tokens:
        if len(token) == 0: # Blank space
            continue # Back to the while loop to extract the next token
        elif token[0] == '+' or token[0] == '-' or token[0] == '*' or token[0] == '/':
            process_an_operator(token[0], operandStack)
        else: # An operand scanned
            # Push an operand to the stack
            operandStack.push(float(token))
    # Return the result
    return operandStack.pop()

# Process one operator
def process_an_operator(op, operandStack):
    op1 = operandStack.pop()
    op2 = operandStack.pop()
    if op == '+': 
        operandStack.push(op2 + op1)
    elif op == '-':
        operandStack.push(op2 - op1)
    elif op == '*': 
        operandStack.push(op2 * op1)
    elif op == '/':
        operandStack.push(op2 / op1)

def insert_blanks(s):
    result = ""

    for ch in s:
        if ch ==  '+' or ch == '-' or ch == '*' or ch == '/':
            result += " " + ch + " "
        else:
            result += ch
    
    return result

if __name__ == "__main__":
    main()
 
