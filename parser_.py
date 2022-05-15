'''
Transforms tokens into nodes
At this point, our lexer takes the input and generates a list of tokens, so we're not working on a character level, and work on a token level

The parser builds up a tree of what's going to happen:

ex. 1 + 2 * 3

      ADD OPERATION
     /              \
   NUMBER      MULTIPLY OPERATION
   value: 1        /       \
              NUMBER     NUMBER
              value: 2   value: 3

ex. (1 + 2) * 3

            MULTIPLY OPERATION
            /                  \
      ADD OPERATION           NUMBER
       /           \          value: 3
    NUMBER       NUMBER
    value:1      value: 2


Grammar rules:

Factor - Numbers
  v
Term - Multiply & divide operations (Number * Number or Number / Number)
  v
Expression - Plus and Minus operations (Term + Term or Term - Term)

Each expression or term can have 0 or more operators
'''

from tokens import TokenType
from nodes import *

class Parser:
  def __init__(self, tokens):
    self.tokens = iter(tokens)
    self.advance()

  def raise_error(self):
    raise Exception("Invalid Syntax")

  def advance(self):
    try:
      self.current_token = next(self.tokens)
    except StopIteration:
      self.current_token = None
  
  def parse(self):
    if self.current_token == None:
      return None

    result = self.expr()

    if self.current_token != None:
      self.raise_error()

    return result

  def expr(self):
    result = self.term()

    while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
      if self.current_token.type == TokenType.PLUS:
        self.advance()
        result = AddNode(result, self.term())
      elif self.current_token.type == TokenType.MINUS:
        self.advance()
        result = SubtractNode(result, self.term())

    return result

  def term(self):
    result = self.factor()

    while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.term())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.term())

    return result

  def factor(self):
    token = self.current_token

    if token.type == TokenType.NUMBER:
      self.advance()
      return NumberNode(token.value)

    self.raise_error()