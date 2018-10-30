# FUNC : Scan input file and return list of tokens
def scan(file) :
  input_file = open(file, 'r')
  tokens = []

  import string
  if_index = []
  for line in input_file :
    temp = line.strip().split()

    index = 0
    while index < len(temp) :
      # number
      if temp[index].isdigit() :
        if int(temp[index]) < 0 :
          tokens.append(['ERROR', int(temp[index])])
        elif int(temp[index]) <= 100 :
          tokens.append(['number<=100', int(temp[index])])
        elif int(temp[index]) <= 1000 :
          tokens.append(['number<=1000', int(temp[index])])
        else :
          tokens.append(['ERROR', int(temp[index])])
      # id
      elif temp[index] in string.ascii_uppercase and len(temp[index]) == 1 :
        tokens.append(['id', ord(temp[index]) - ord('A') + 1])
      # IF
      elif temp[index] == 'IF' :
        tokens.append(['IF', 0])
        if_index.append(len(tokens)-1)
      # GOTO
      elif temp[index] == 'GOTO' :
        if temp[index+1].isdigit() and 0 < int(temp[index+1]) <= 1000 :
          index += 1
          tokens.append(['GOTO', int(temp[index])])
        else :
          tokens.append(['ERROR', 0])
      # PRINT
      elif temp[index] == 'PRINT' :
        tokens.append(['PRINT', 0])
      # STOP
      elif temp[index] == 'STOP' :
        tokens.append(['STOP', 0])
      # +
      elif temp[index] == '+' :
        tokens.append(['+', 1])
      # -
      elif temp[index] == '-' :
        tokens.append(['-', 2])
      # <
      elif temp[index] == '<' :
        tokens.append(['<', 3])
      # =
      elif temp[index] == '=' :
        tokens.append(['=', 4])
      else :
        tokens.append(['ERROR', 0])
      index += 1
  input_file.close()
  for index in if_index :
    tokens[index+4][0] = 'GOTO'
  
  return tokens

      
