class NumberNode:                     # Classe responsável pelos números da árvore binária
    def __init__(self, token):
        self.token = token

        self.start_position = self.token.start_position
        self.end_position = self.token.end_position

    def __repr__(self):
        return f'{self.token}'


class VariableAccessNode:
    def __init__(self, variable_name_token):
        self.variable_name_token = variable_name_token

        self.start_position = self.variable_name_token.start_position
        self.end_position = self.variable_name_token.end_position


class VariableAssignNode:
    def __init__(self, variable_name_token, node_value):
        self.variable_name_token = variable_name_token
        self.node_value = node_value

        self.start_position = self.variable_name_token.start_position
        self.end_position = self.node_value.end_position


class BinaryOperationNode:            # Classe responsável pelas operações que envolvem mais de um operando. Exemplo: 1 + 2
    def __init__(self, left_node, operation_token, right_node):
        self.left_node = left_node
        self.operation_token = operation_token
        self.right_node = right_node

        self.start_position = self.left_node.start_position
        self.end_position = self.right_node.end_position

    def __repr__(self):
        return f'({self.left_node}, {self.operation_token}, {self.right_node})'


class UnaryOperationNode:
    def __init__(self, operation_token, node):
        self.operation_token = operation_token
        self.node = node

        self.start_position = self.operation_token.start_position
        self.end_position = self.node.end_position

    def __repr__(self):
        return f'({self.operation_token}, {self.node})'

    def __repr__(self):
        return f'({self.node})'


class SqrtNode:
    def __init__(self, node):
        self.node = node

        self.start_position = self.node.start_position
        self.end_position = self.node.end_position
