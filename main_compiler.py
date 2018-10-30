# Scan source file for tokens
from scanner import scan
tokens = scan('input.txt')

# Stack for parsing
class Stack :
  data = []
  def push(self, item) : self.data.append(item)
  def pop(self) : return self.data.pop()
  def empty(self) : return len(self.data) == 0
  def top(self) : return self.data[-1]
stack = Stack()
stack.push('pgm')

# Pointer for tokens iterating
pointer = 0

# Import grammar
from grammar import Grammar
grammar = Grammar()

# List for output
output = []
current_line = 10
error = False
error_message = ''

# Parsing loop
while not stack.empty() and pointer < len(tokens) :
  top = stack.pop() 
  # check if terminal symbol matched
  if grammar.is_terminal(top) and grammar.match(top, tokens[pointer][0]) :
    if top == tokens[pointer][0] == 'GOTO' : stack.pop()
    if top == 'line_num' and tokens[pointer][0] == 'GOTO' : top = 'GOTO'
    b_code = grammar.get_b_code(top, tokens[pointer][1])
    output += b_code
    # Save current line for error message
    if b_code[0] == 10 : current_line = b_code[1]
    pointer += 1
  else :
    # Check if it is in correct grammar
    # If yes, push next production(s) to stack
    prod_number = grammar.check_grammar(top, tokens[pointer][0])
    if prod_number != 0 :
      prod = grammar.get_next_production(prod_number) 
      for i in range (len(prod)-1, -1, -1) :
        stack.push(prod[i] )
    else :
      error_message = grammar.get_error_message(top, current_line)
      error = True
      break

output_file = open('./output.txt', 'w')
if not error :
  for i in output :
    output_file.write(str(i))
    output_file.write(' ')
else :
  output_file.write(error_message)
output_file.close()
    
