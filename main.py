from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter, Value
from symbolTable import SymbolTable
import os

symbol_table = SymbolTable()
symbol_table.set('null', Value(0))

expressions = [
    ("1 + 1", 1 + 1),
    ("2 * 3", 2 * 3),
    ("5 / 4", 5 / 4),
    ("2 * 3 + 1", 2 * 3 + 1),
    ("1 + 2 * 3", 1 + 2 * 3),
    ("(2 * 3) + 1", (2 * 3) + 1),
    ("2 * (3 + 1)", 2 * (3 + 1)),
    ("(2 + 1) * 3", (2 + 1) * 3),
    ("-2 + 3", -2 + 3),
    ("5 + (-2)", 5 + (-2)),
    ("5 * -2", 5 * -2),
    ("-1 - -2", -1 - -2),
    ("-1 - 2", -1 - 2),
    ("4 - 5", 4 - 5),
    ("1 - 2", 1 - 2),
    ("3 - ((8 + 3) * -2)", 3 - ((8 + 3) * -2)),
    ("2*3*4", 2 * 3 * 4),
    ("2 + 3 + 4 * 3 * 2 * 2", 2 + 3 + 4 * 3 * 2 * 2),
    ("10 + 11", 10 + 11),
]

while (True):
    print('Deseja inserir manualmente ou utilizar a lista de expressões pré-selecionadas?\n\n[1] pré-seleção\n[2] input manual\n[0] sair\n\n')
    opcao = input('\nOpção: ')

    if opcao == '1':
        os.system('CLS')
        print("Pré-seleção de expressões:\n\n")
        for expression, expected in expressions:
            lexer = Lexer(str(expression))
            tokens, error = lexer.generate_tokens()
            if error:
                print(error)
            else:
                parser = Parser(tokens, symbol_table)
                tree = parser.parse()
                interpreter = Interpreter()
                result = interpreter.callNodeMethod(tree, symbol_table)
                pass_result = "PASS" if result.value == float(expected) else "FAIL"
                print(f"Expression: {expression} - {pass_result} - {type(result.value)}: {result.value} - {type(float(expected))}: {float(expected)}")
        exit()
    elif opcao == '2':
        os.system('CLS')
        print("Input manual de expressões:\n\n")
        while (True):
            expression = input('input > ')
            lexer = Lexer(str(expression))
            tokens, error = lexer.generate_tokens()
            if error:
                print(error)
            else:
                parser = Parser(tokens, symbol_table)
                tree = parser.parse()
                interpreter = Interpreter()
                result = interpreter.callNodeMethod(tree, symbol_table)
                print(f"Expressão: {expression} - Resultado: {result}")
    elif opcao == '0':
        exit()
    else:
        os.system('CLS')
        print('Opção inválida, tente de novo.')
