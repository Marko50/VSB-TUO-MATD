import sys, getopt, time

class State:
    def __init__(self, is_ending, accepted_input = None, next_state = None):
        self.is_ending = is_ending
        self.accepted_input = accepted_input
        self.next_state = next_state
    
    def process_input(self, input):
        if input == self.accepted_input:
            return self.next_state
        else:
            return self.initial_state

    def print(self):
        print("My input: " + str(self.accepted_input))
        if self.next_state != None:
            self.next_state.print()

    def set_initial_state(self, state):
        self.initial_state = state
        if self.next_state:
            self.next_state.set_initial_state(state)
        

def preprocess(pattern):
    initial_state = None  
    last_state = State(True)
    for i in reversed(range(len(pattern))):
        initial_state = State(False, pattern[i], last_state)
        last_state = initial_state
    initial_state.set_initial_state(initial_state)
    return initial_state

def process(text, initial_state, pattern):
    i = 0
    state = initial_state
    while i < len(text):
        state = state.process_input(text[i])
        i += 1
        if state.is_ending:            
            print("Match found at " + str(i - len(pattern)))
            state = initial_state
        

pattern = getopt.getopt(sys.argv[1:],"")[1][0]
file = getopt.getopt(sys.argv[1:],"")[1][1]

with open(file, encoding="utf8", errors='ignore') as f:
    file_text = f.read()
    start = time.time()
    initial_state = preprocess(pattern)
    process(file_text, initial_state, pattern)
    end = time.time()
    print("Elapsed time was: " + str(end - start) + " seconds")
    f.close()