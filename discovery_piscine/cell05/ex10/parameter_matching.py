#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    parameter = sys.argv[1]
    answer = input("What was the parameter? ")

    if answer == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
