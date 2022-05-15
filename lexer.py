from tokens import Token, TokenType

# Define whitespace values (space, line break, type)
WHITESPACE = ' \n\t'
# Define digits 
DIGITS = '1234567890'

class Lexer:
  def __init__(self, text):
    # store text and make iterable
    self.text = iter(text)
    # advance to first character
    self.advance()

  # Keep track of current character at any stage within the lexer
  def advance(self):
    try:
      self.current_char = next(self.text)
    except StopIteration:
      self.current_char = None
  
  # Generate all tokens from text
  def generate_tokens(self):
    # Iterate until end of string
    while self.current_char != None:

      # skip whitespace
      if self.current_char in WHITESPACE:
        self.advance()
      # NUMBER token
      elif self.current_char == '.' or self.current_char in DIGITS:
        # Need to get multiple tokens, want to use a generator/no return
        yield self.generate_number()
      # PLUS token
      elif self.current_char == '+':
        self.advance()
        yield Token(TokenType.PLUS)
      # MINUS token
      elif self.current_char == '-':
        self.advance()
        yield Token(TokenType.MINUS)
      # MULTIPLY token
      elif self.current_char == '*':
        self.advance()
        yield Token(TokenType.MULTIPLY)
      # DIVIDE token
      elif self.current_char == '/':
        self.advance()
        yield Token(TokenType.DIVIDE)
      # LPAREN token
      elif self.current_char == '(':
        self.advance()
        yield Token(TokenType.LPAREN)
      # RPAREN token
      elif self.current_char == ')':
        self.advance()
        yield Token(TokenType.RPAREN)
      else:
        raise Exception(f"Illegal Character '{self.current_char}'")


  def generate_number(self):
    decimal_point_count = 0
    number_str = self.current_char
    self.advance()

    while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
      if self.current_char == '.':
        decimal_point_count += 1
        if decimal_point_count > 1:
          break

      number_str += self.current_char
      self.advance()

    if number_str.startswith('.'):
      number_str = '0' + number_str
    if number_str.endswith('.'):
      number_str += '0'

    return Token(TokenType.NUMBER, float(number_str))