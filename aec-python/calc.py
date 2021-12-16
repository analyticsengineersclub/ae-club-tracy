# calc.py
import argparse

parser = argparse.ArgumentParser(description="CLI Calculator")
subparsers = parser.add_subparsers(help="sub-command help", dest="command")

# sum subparser
add = subparsers.add_parser("add", help="add integers")
add.add_argument("integers_to_sum", nargs="*", type=int)

# difference subparser
subtract = subparsers.add_parser("subtract", help="subtract integers")
subtract.add_argument("integers_to_subtract", nargs="*", type=int)

# quotient subparser
divide = subparsers.add_parser("divide", help="divide integers")
divide.add_argument("integers_to_divide", nargs="*", type=int)

# product subparser
multiply = subparsers.add_parser("multiply", help="multiply integers")
multiply.add_argument("integers_to_multiply", nargs="*", type=int)


def aec_subtract(integers_to_subtract):
    for number in integers_to_subtract:
        if not isinstance(number, int):
            raise TypeError("Only integers, please!")
    else:
        difference = integers_to_subtract[0]
        if len(integers_to_subtract) == 1:
            print(f"Only one integer was passed; the value is {difference}")
        else:
            for i in range(1, len(integers_to_subtract)):
                difference -= integers_to_subtract[i]
        if difference < 0:
            difference = 0
        print(f"The difference of these values is {difference}")
        return difference


def aec_divide(integers_to_divide):
    for number in integers_to_divide:
        if not isinstance(number, int):
            raise TypeError("Only integers, please!")
    quotient = integers_to_divide[0]
    if len(integers_to_divide) == 1:
        print(f"Only one integer was passed; the value is {quotient}")
    elif 0 in integers_to_divide[1:]:
        print("Whoops! Cannot divide by 0! Returning 0 as quotient.")
        quotient = 0
    else:
        for i in range(1, len(integers_to_divide)):
            quotient /= integers_to_divide[i]
        print(f"The quotient of these values is {quotient}")
    return quotient


def aec_add(integers_to_sum):
    summed = sum(integers_to_sum)
    if len(integers_to_sum) == 1:
        print(f"Only one integer was passed; the value is {sum}")
    else:
        print(f"The sum of these values is {sum}")
    return summed


def aec_multiply(integers_to_multiply):
    product = integers_to_multiply[0]
    if len(integers_to_multiply) == 1:
        print(f"Only one integer was passed; the value is {product}")
    else:
        for i in range(1, len(args.integers_to_multiply)):
            product *= args.integers_to_multiply[i]
        print(f"The product of these values is {product}")
    return product


if __name__ == "__main__":

    args = parser.parse_args()

    if args.command == "add":
        aec_add(args.integers_to_sum)

    if args.command == "subtract":
        aec_subtract(args.integers_to_subtract)

    if args.command == "multiply":
        aec_multiply(args.integers_to_multiply)

    if args.command == "divide":
        aec_divide(args.integers_to_divide)
