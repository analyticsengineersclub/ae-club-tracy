# calc.py 

import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator")

subparsers = parser.add_subparsers(help="sub-command help", dest="command")
# sum subparser
add = subparsers.add_parser("add", help="add integers")
add.add_argument("ints_to_sum", nargs=2, type=int)

# difference subparser
sub = subparsers.add_parser("sub", help="subtract integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

args = parser.parse_args()

if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"the sum of values is {our_sum}")

if args.command == "sub":
    our_sub = args.ints_to_sub[0] - args.ints_to_sub[1]
    print(f"the difference of values is {our_sub}")
