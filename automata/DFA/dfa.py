# Prepare DFA over binary alphabet accepting odd number of 1s.
import sys, getopt

class S0:
    def __init__(self):
        self.accepting_state = False

    def next_state(self, char):
        if char == '0':
            return self
        elif char == '1':
            return S1()
        else:
            raise ValueError("String alfabet must only contain 0 or 1")


class S1:
    def __init__(self):
        self.accepting_state = True

    def next_state(self, char):
        if char == '0':
            return self
        elif char == '1':
            return S0()
        else:
            raise ValueError("String alfabet must only contain 0 or 1")

def process(sequence):
    state = S0()
    for c in sequence:
        state = state.next_state(c)
    return state    

arg = getopt.getopt(sys.argv[1:],"")[1][0]

state = process(arg)

if state.accepting_state:
    print("String has odd number of 1's")
else:
    print("String has even number of 1's")


