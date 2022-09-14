import math
from nodes import *
from tokens import TokenType


class Interpreter:
    def callNodeMethod(self, node, symbol_table):

        if type(node) == NumberNode:
            number = Value(node.token.value)
            number.set_position_value(node.start_position, node.end_position)
            return number
        elif type(node) == VariableAccessNode:
            variable_name = node.variable_name_token.value
            value = symbol_table.get(variable_name)

            if not value:
                raise Exception(f"\n\n#####################\n\nErro de tempo de execução: Variável {variable_name} não definida.\nLinha {node.start_position.line + 1}, coluna: {node.start_position.column + 1}\n\n#####################\n\n")

            return value
        elif type(node) == VariableAssignNode:
            variable_name = node.variable_name_token.value
            value = self.callNodeMethod(node.node_value, symbol_table)
            symbol_table.set(variable_name, value)

            return value
        elif type(node) == BinaryOperationNode:
            left_node = self.callNodeMethod(node.left_node, symbol_table)
            right_node = self.callNodeMethod(node.right_node, symbol_table)

            if node.operation_token.type == TokenType().PLUS:
                result = left_node.add(right_node)
            elif node.operation_token.type == TokenType().MINUS:
                result = left_node.sub(right_node)
            elif node.operation_token.type == TokenType().MULTIPLY:
                result = left_node.mul(right_node)
            elif node.operation_token.type == TokenType().DIVIDE:
                result = left_node.div(right_node)
            elif node.operation_token.type == TokenType().POWER:
                result = left_node.power(right_node)
            result.set_position_value(node.start_position, node.end_position)
            return result
        elif type(node) == UnaryOperationNode:
            number = self.callNodeMethod(node.node, symbol_table)

            if node.operation_token.type == TokenType().MINUS:
                number = number.mul(Value(-1))

            number.set_position_value(node.start_position, node.end_position)
            return number
        elif type(node) == SqrtNode:
            number = self.callNodeMethod(node.node, symbol_table)
            result = number.sqrt(number)
            result.set_position_value(node.start_position, node.end_position)
            return result


class Value:
    def __init__(self, value):
        self.value = value
        self.set_position_value()

    def set_position_value(self, start_position=None, end_position=None):
        self.start_position = start_position
        self.end_position = end_position

    def add(self, number):
        if isinstance(number, Value):
            return Value(self.value + number.value)

    def sub(self, number):
        if isinstance(number, Value):
            return Value(self.value - number.value)

    def mul(self, number):
        if isinstance(number, Value):
            return Value(self.value * number.value)

    def div(self, number):
        if isinstance(number, Value):
            if number.value == 0:
                raise Exception(f"\n\n#####################\n\nErro de tempo de execução: Divisão por zero.\nLinha {number.start_position.line + 1}, coluna: {number.start_position.column + 1}\n\n#####################\n\n")
            return Value(self.value / number.value)

    def power(self, number):
        if isinstance(number, Value):
            return Value(self.value ** number.value)

    def sqrt(self, number):
        if isinstance(number, Value):
            return Value(math.sqrt(number.value))

    def __repr__(self):
        return str(self.value)
