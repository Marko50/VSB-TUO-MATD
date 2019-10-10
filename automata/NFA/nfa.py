# Prepare NFA over binary alphabet accepting strings ending with 01.

import sys, getopt

class S0:
    def __init__(self):
        self.accepting_state = False

    def next_state(self, char, index):
        queue = []
        if char == '0':
            queue.append( (S1(), index) )
            queue.append( (S0(), index ) )
        elif char == '1':
            queue.append( (S0(), index) )
        return queue 
           

class S1:
    def __init__(self):
        self.accepting_state = False
    def next_state(self, char, index):
        queue = []
        if char == '1':
            queue.append((S2(), index))
        else:
            queue.append((S1(), index))
        return queue

class S2:
    def __init__(self):
        self.accepting_state = True
    def next_state(self, _char, _index):
        return []

def process(sequence):
    queue = []
    index = 0
    queue.append((S0(), index))
    for c in sequence:
        index += 1
        aux_queue = []
        for tup in queue:
            tup = queue.pop()
            state = tup[0]
            aux_queue = state.next_state(c, index)
        for aux_tup in aux_queue:
            queue.append(aux_tup)
    return queue

def verify_validness(queue, length):
    for tup in queue:
        if (tup[1] == length) and tup[0].accepting_state:
            print("Give string ends in 01.")
            return True
    print("Given string does not end in 01.")
    return False
        

arg = getopt.getopt(sys.argv[1:],"")[1][0]

queue = process(arg)
verify_validness(queue, len(arg))



