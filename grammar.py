class Grammar :
  
  productions = dict()
  parsing_table = dict()
  terminal = ['line_num', 'id', 'const', '+', '-', '=', '<',
              'IF', 'PRINT', 'GOTO', 'STOP']
  

  # FUNC : Init function
  def __init__(self) :
    # Insert productions
    production_list_file = open('production_list.txt', 'r')
    prod_no = 1
    for line in production_list_file :
      temp = line.strip().split()
      if temp[3] == 'empty' : temp = temp[:3]
      self.productions[prod_no] = ( (temp[1], temp[3:]) )
      prod_no += 1
    production_list_file.close()

    # Initialize parsing table
    parsing_table_file = open('parsing_table.txt', 'r')
    for line in parsing_table_file :
      temp = line.strip().split()
      if temp[0] not in self.parsing_table :
        self.parsing_table[temp[0]] = [ (temp[1], int(temp[2])) ]
      else :
        self.parsing_table[temp[0]].append( (temp[1], int(temp[2])) )
    parsing_table_file.close()

  # FUNC : Check if inputted symbol is terminal symbol
  def is_terminal(self, symbol) :
    return symbol in self.terminal

  # FUNC : Check if current character's type matched top of stack
  def match(self, top, c_type) :
    if top == c_type  :
      return True
    if top == 'line_num' and c_type in 'number<=1000' :
      return True
    if top == 'const' and c_type in 'number<=100' :
      return True
    if top == 'id' and c_type == 'id' :
      return True
    if top == 'GOTO' and c_type in 'number<=1000' :
      return True
    if top == 'line_num' and c_type == 'GOTO' :
      return True
    return False

  # FUNC : Return B-code
  def get_b_code(self, top, value) :
    if top == 'line_num' : return [10, value]
    if top == 'id' : return [11, value]
    if top == 'const' : return [12, value]
    if top == 'IF' : return [13, 0]
    if top == 'GOTO' : return [14, value]
    if top == 'PRINT' : return [15, 0]
    if top == 'STOP' : return [16, 0]
    if top in '+-<=' : return [17, value]
    
  # FUNC : Check if current character's type is available in parsing table
  #        If available, return next production number
  #        Else, return 0
  def check_grammar(self, top, c_type) :
    if c_type == 'number<=1000' : c_type = 'line_num'
    if c_type == 'number<=100' : c_type = 'const|line_num'
    if top in self.parsing_table :
      for route in self.parsing_table[top] :
        if route[0] in c_type : return route[1]
    return 0

  # FUNC : Return production that matched input number
  def get_next_production(self, number) :
    return self.productions[number][1]

  # FUNC : Return error message
  def get_error_message(self, top, line) :
    message = 'Invalid syntax at line ' + str(line) + '.'
    return message
