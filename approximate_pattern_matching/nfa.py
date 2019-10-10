import sys, getopt

class State:
    def __init__(self, state_number, error_num, acc_char = None):
       self.state_number = state_number
       self.error_num = error_num
       self.accepted_char = acc_char

    def accepts(self, char):
        return self.accepted_char == char
    
    def is_accepting(self):
        return self.accepted_char == None

class NFA:
    def __init__(self, pattern, max_error):
        self.max_error = max_error
        self.pattern = pattern
        self.states = { }
        self.max_size = (len(pattern) + 1) * ( max_error + 1 )
        i = 0
        while i <= max_error:
            self.initialize_state_error(pattern, i, 1 + i*len(pattern) + i)
            i += 1
    
    def initialize_state_error(self, pattern, error_number, start):
        i = start
        for char in pattern:
            self.states[str(i)] = State(i, error_number, char)
            i += 1
        self.states[str(i)] = State(i, error_number)

    def print(self):
        for state_no in self.states:
            print("State number: " + str(self.states[state_no].state_number) + " with error_num: " + str(self.states[state_no].error_num) + " accepting char " + str(self.states[state_no].accepted_char))

    def process(self, word):
        state_no = 1
        queue_state_numbers = [ state_no ]
        # process strings in word
        for char in word:
            i = len(queue_state_numbers)
            while i > 0:
                state_no = queue_state_numbers.pop(0)
                if self.states[str(state_no)].accepts(char):
                    state_no += 1
                    self.inc_queue(queue_state_numbers, state_no)
                else:
                    state_no += 1 + len(self.pattern)
                    self.inc_queue(queue_state_numbers, state_no)
                    state_no += 1
                    self.inc_queue(queue_state_numbers, state_no)
                i -= 1
        self.deal_with_empty_states(word, queue_state_numbers)
        return self.verify_approximate_matching(queue_state_numbers)
    
    def inc_queue(self, queue_state_numbers, state_no):
        if state_no <= self.max_size:
            queue_state_numbers.append(state_no)
    
    def deal_with_empty_states(self, word, queue_state_numbers):
        dif = len(self.pattern) -  len(word) 
        if dif > 0:
            i = len(queue_state_numbers)
            while i > 0:
                state_no = queue_state_numbers.pop(0)
                state_no += min(dif, self.max_error) *(2 + len(self.pattern))
                self.inc_queue(queue_state_numbers, state_no)
                i -= 1

    def verify_approximate_matching(self, queue):
        for state_no in queue:
            if self.states[str(state_no)].is_accepting():
                return True
        return False
            
pattern = getopt.getopt(sys.argv[1:],"")[1][0]
word = getopt.getopt(sys.argv[1:],"")[1][1]
error = getopt.getopt(sys.argv[1:],"")[1][2]

nfa = NFA(pattern,int(error))
if nfa.process(word):
    print("True")
else:
    print("False")