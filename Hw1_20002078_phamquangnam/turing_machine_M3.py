class TuringMachine:
    def __init__(self, states, symbol, initial_state, transitions):
        self.states = states
        self.symbols = symbols
        self.current_state = initial_state
        self.transitions = transitions

    def run(self, input_str):
        temp_str = list('>' + input_str +  '_')
        temp_idx = 0
        
        while self.current_state != 'h':
            current_symbol = temp_str[temp_idx] 
            if (self.current_state, current_symbol) in self.transitions:
                transition = self.transitions[(self.current_state, current_symbol)]
                temp_str[temp_idx] = transition[1]
                if transition[2] == 'R':
                    temp_idx += 1
                elif transition[2] == 'L':
                    temp_idx -= 1
                self.current_state = transition[0]
            else:
                print("No transition found for state {} and symbol {}".format(self.current_state, current_symbol))
                break

        result = ''.join(temp_str)
        return result

# Define the states, symbols, and transitions for the Turing machine
states = {'s', 'q', 'h'}
symbols = {'0', '1', '>', '_'}
initial_state = 's'

transitions = {
    ('s', '0'): ('s', '1', 'R'),
    ('s', '1'): ('s', '0', 'R'),
    ('s', '>'): ('s', '>', 'R'),
    ('s', '_'): ('h', '_', '-'),
}

# Create a Turing machine instance
tm = TuringMachine(states, symbols, initial_state, transitions)

# Test the Turing machine with a binary input
binary_input = "10101"
result = tm.run(binary_input)
print("Input:  {} (binary)".format(binary_input))
print("Output: {} (binary)".format(result[1:-1]))
