import sys
from typing import List
from ..data_structures.array_stack import Stack


# def _calculate(lhs: float, rhs: float, operator) -> float:
#
#
#
# def main():
#     values = Stack()
#     result = 0
#
#     # print('\nEnter one from the following:\n    \
#     #       - An integer value.                   \
#     #       - An operator                         \
#     #       - Q to Quit')
#
#     while True:
#         val = input('Enter:')
#
#         try:
#             operand = int(val)
#         except ValueError:
#             operation = str(val)
#
#             if operation == 'Q':
#                 break
#
#     return result


def postfix_calculate(tokens: List[str]):
    values = Stack()

    for token in tokens:
        try:
            # If the value is a float.
            operand = float(token)
            values.push(operand)
        except ValueError:
            try:
                # Otherwise evaluate the expression.
                rhs = float(values.pop())
                lhs = float(values.pop())

                # And push the value back to the stack.
                if token == '+':
                    values.push(lhs + rhs)
                elif token == '-':
                    values.push(lhs - rhs)
                elif token == '*':
                    values.push(lhs * rhs)
                elif token == '/':
                    values.push(lhs / rhs)
                elif token == '%':
                    values.push(lhs % rhs)
                else:
                    raise ValueError(f'Unrecognized token: {token}')
            except IndexError:
                raise IndexError('At least 2 operands should be present.')

    return values.pop()


if __name__ == '__main__':
    print(postfix_calculate((sys.argv[1:])))
    # args = [5.5, 7.5, 70, '*', '+', 53, '-', 'Q']
    # print(postfix_calculate(args))
