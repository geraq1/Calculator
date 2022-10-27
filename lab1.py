from decimal import *


def priority_of(o):
    if o == '*' or o == '/':
        return 2
    elif o == '+' or o == '-':
        return 1


def handle_operator(final_list, stack_of_operators, token):
    if len(stack_of_operators) > 0:
        temp_token = stack_of_operators[len(stack_of_operators) - 1]
        while len(stack_of_operators) > 0 and temp_token != '(':
            if priority_of(token) <= priority_of(temp_token):
                final_list.append(stack_of_operators.pop())
            else:
                break

    stack_of_operators.append(token)


def handle_right_parenthesis(final_list, stack_of_operators):
    temp_token = stack_of_operators[len(stack_of_operators) - 1]

    while temp_token != '(':
        final_list.append(stack_of_operators.pop())
        temp_token = stack_of_operators[len(stack_of_operators) - 1]
        if temp_token == '(':
            stack_of_operators.pop()


def get_postfix(expr):
    final_list = []
    stack_of_operators = []
    token_list = expr.split()

    for token in token_list:
        if token not in ('-', '+', '*', '/', '(', ')'):
            final_list.append(token)
        elif token in ('-', '+', '*', '/'):
            handle_operator(final_list, stack_of_operators, token)
        elif token == '(':
            stack_of_operators.append(token)
        elif token == ')':
            handle_right_parenthesis(final_list, stack_of_operators)

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
                stack.append(a + b)
            elif x == "-":
                stack.append(a - b)
            elif x == "*":
                stack.append(a * b)
            else:
                stack.append(a / b)
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
