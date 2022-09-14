from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens, symbol_table):
        self.tokens = tokens
        self.symbol_table = symbol_table
        self.token_index = -1
        self.advance()

    def advance(self, ):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        return self.current_token

    def parse(self):
        result = self.expression()

        if self.current_token.type != TokenType().EOF:
            raise Exception(f"\n\n#####################\n\nErro de sintaxe: Esperado '+', '-', '*', '/' ou '^'.\nLinha {self.current_token.start_position.line + 1}, coluna: {self.current_token.start_position.column + 1}\n\n#####################\n\n")
        return result

    def atom(self):
        token = self.current_token

        if token.type in (TokenType().NUMBER):
            self.advance()
            return NumberNode(token)

        elif token.type in (TokenType().IDENTIFIER):
            self.advance()
            return VariableAccessNode(token)

        elif token.type == TokenType().KEYWORD and token.value in ['sqrt', 'SQRT']:
            sqrt_expression = self.sqrt_expression()
            return sqrt_expression

        elif token.type == TokenType().LPAREN:
            self.advance()
            expression = self.expression()

            if self.current_token.type == TokenType().RPAREN:
                self.advance()
                return expression
            else:
                raise Exception(f"\n\n#####################\n\nErro de sintaxe: Esperado um ')'.\nLinha {self.current_token.start_position.line + 1}, coluna: {self.current_token.start_position.column + 1}\n\n#####################\n\n")

        raise Exception(f"\n\n#####################\n\nErro de sintaxe: Esperado número, '+' ou '-'.\nLinha {self.current_token.start_position.line + 1}, coluna: {self.current_token.start_position.column + 1}\n\n#####################\n\n")

    def sqrt_expression(self):
        self.advance()

        if self.current_token.type == TokenType().LPAREN:
            self.advance()
            expression = self.expression()

            if self.current_token.type == TokenType().RPAREN:
                self.advance()
                return SqrtNode(expression)
            else:
                raise Exception(f"\n\n#####################\n\nErro de sintaxe: Esperado um ')'.\nLinha {self.current_token.start_position.line + 1}, coluna: {self.current_token.start_position.column + 1}\n\n#####################\n\n")

    def power(self):
        return self.binary_operation(self.atom, (TokenType().POWER), self.factor)

    def factor(self):
        token = self.current_token

        if token.type in (TokenType().MINUS, TokenType().PLUS):
            self.advance()
            factor = self.factor()
            return UnaryOperationNode(token, factor)

        return self.power()

    def term(self):
        return self.binary_operation(self.factor, (TokenType().DIVIDE, TokenType().MULTIPLY))

    def expression(self):
        var_name = self.current_token
        var_name_value = self.symbol_table.get(var_name.value)
        if var_name_value == None and self.current_token.type == TokenType().IDENTIFIER:
            self.advance()

            if self.current_token.type != TokenType().EQUALS:
                raise Exception(f'Erro de sintaxe: Esperado um "=".\nLinha {self.current_token.start_position.line + 1}, coluna: {self.current_token.start_position.column + 1}')

            self.advance()
            expression = self.expression()

            return VariableAssignNode(var_name, expression)

        return self.binary_operation(self.term, (TokenType().PLUS, TokenType().MINUS))

    def binary_operation(self, function_a, operations, function_b=None):
        if function_b == None:
            function_b = function_a
        left_node = function_a()

        while self.current_token.type in operations:
            operation_token = self.current_token
            self.advance()
            right_node = function_b()
            left_node = BinaryOperationNode(left_node, operation_token, right_node)
        return left_node
