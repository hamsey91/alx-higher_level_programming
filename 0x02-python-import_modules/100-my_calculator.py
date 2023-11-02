#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <a> <operator> <b>')
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif operator == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif operator == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif operator == "/":
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
