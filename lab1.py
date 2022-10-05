from decimal import *


def prec(o): #приоритет оператора
    if o == '*':
        return 3
    elif o == '/':
        return 2
    elif o == '+':
        return 1
    elif o == '-':
        return 1


def get_postfix(expr):
    final_list = []
    stack_of_operators = []
    token_list = expr.split() #разделение выражения
    for token in token_list:
        if token not in ('-', '+', '*', '/', '(', ')'):
            final_list.append(token)
        elif token in ('-', '+', '*', '/'):
            if len(stack_of_operators) > 0:
                temp_token = stack_of_operators[len(stack_of_operators) - 1] # вершина стека операторов 
                while len(stack_of_operators) > 0 and temp_token != '(':
                    if prec(token) <= prec(temp_token): # сравнивание приоритет операции 
                        final_list.append(stack_of_operators.pop())
                    else:
                        break
            stack_of_operators.append(token)
        elif token == '(':
            stack_of_operators.append(token)
        elif token == ')':
            temp_token = stack_of_operators[len(stack_of_operators) - 1] 
            while temp_token != '(':
                final_list.append(stack_of_operators.pop())
                temp_token = stack_of_operators[len(stack_of_operators) - 1]
                if temp_token == '(':
                    stack_of_operators.pop()

    while len(stack_of_operators) > 0:
        final_list.append(stack_of_operators.pop())
    return final_list


def calculate_postfix(postfix_exp):
    stack = []
    for x in postfix_exp:
        if x in ('+', '-', '*', '/'):
            b = stack.pop()
            a = stack.pop()
            if x == "+":
                result = a + b
            elif x == "-":
                result = a - b
            elif x == "*":
                result = a * b
            else:
                result = a / b
            stack.append(result)
        else:
            stack.append(Decimal(x))
    if len(stack) == 1:
        return stack.pop()


def calculate():
    exp = input('>>>')
    postfix = get_postfix(exp)
    print(calculate_postfix(postfix))


while True:
    try:
        calculate()
    except DivisionByZero:
        print('На ноль делить нельзя!')
    except IndexError: 
        print('Неверное выражение.')
