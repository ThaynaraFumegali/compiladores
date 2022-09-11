from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter, Value
from symbolTable import SymbolTable

symbol_table = SymbolTable()
symbol_table.set('null', Value(0))

while True:
    text = input('input > ')
    lexer = Lexer(text)
    tokens, error = lexer.generate_tokens()
    if error:
        print(error)
    else:
        parser = Parser(tokens, symbol_table)
        tree = parser.parse()
        interpreter = Interpreter()
        result = interpreter.callNodeMethod(tree, symbol_table)
        print(result)
