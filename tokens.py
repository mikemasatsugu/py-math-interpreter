'''
Lexer - groups input characters into tokens and determines type of each token

E.g.: 1 + 2.2 * 3 => Token 1: { type: NUMBER, value: 1 }
                     Token 2: { type: PLUS, value: None } 
                     Token 3: { type: NUMBER, value: 2.2 } 
                     Token 4: { type: MULTIPLY, value: None } 
                     Token 5: { type: NUMBER, value: 3 } 
'''

from enum import Enum
from dataclass import dataclass

class TokenType(Enum):
  NUMBER   = 0
  PLUS     = 1
  MINUS    = 2
  MULTIPLY = 3
  DIVIDE   = 4
  LPAREN   = 5
  RPAREN   = 6

@dataclass
class Token:
  type: TokenType
  value: any = None

  # debugging representation method to print tokens
  def __repr__(self):
    return self.type.name + (f":{self.value}" if self.value != None else "")