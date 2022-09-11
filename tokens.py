# Classe responsável por definir os tipos de tokens, seja operador, número, identificador e etc
class TokenType:
    NUMBER = 'NUMBER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    POWER = 'POWER'
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    EQUALS = 'EQUALS'
    EOF = 'EOF'

    KEYWORDS = [
        'SQRT',
        'sqrt'
    ]


# Classe responsável pelo tipo do token e seu valor. Exemplo [value: 6, type: NUMBER]
class Token:
    def __init__(self, type, value=None, start_position=None, end_position=None):
        self.type = type
        self.value = value

        if start_position:
            self.start_position = start_position.position_copy()
            self.end_position = start_position.position_copy()
            self.end_position.advance()

        if end_position:
            self.end_position = end_position

    def __repr__(self):
        return self.type + (f":{self.value}" if self.value != None else "")
