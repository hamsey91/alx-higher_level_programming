#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = str(sys.argv[2])
    if operator == "+":
        print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, add(a, b)))
    elif operator == "-":
        print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
