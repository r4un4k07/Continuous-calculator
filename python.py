def calc(f_digit, operator, s_digit):
    """Takes two digits and an operator as an input and returns the calculated value"""
  
    if operator == '+':
        return f_digit + s_digit
    elif operator == '-':
        return f_digit - s_digit
    elif operator == '*':
        return f_digit * s_digit
    elif operator == '/':
        return f_digit / s_digit
    else:
        print("Please provide a valid operator!")
        
a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))
op = input("Enter operand: ")
result = calc(a, op, b)
print(f'Your operation result: {result}')

while(1):
    question = input("Are there is more operation? yes / no: ")
    
    if question == 'yes':
        a = int(input("Enter the digit: "))
        op = input("Enter operand: ")
        result = calc(result, op, a)
        print(f'Your operation result: {result}')
        continue
    else:
        break
