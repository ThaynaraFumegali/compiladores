from lib2to3.pgen2 import token
import string
from tokens import Token, TokenType
from errors import Error
from position import Position

DIGITS = '0123456789'
LETTERS = string.ascii_letters

LETTERS_DIGITS = LETTERS + DIGITS

# Classe responsável por realizar a leitura e a análise léxica do texto


class Lexer:
    def __init__(self, text):
        self.text = text                            # Atributo: texto lido, ou seja, o código
        self.position = Position(-1, 0, -1)         # Atributo: posição no texto
        self.current_char = None                    # Atributo: caracter atual no texto
        self.advance()                              # Método: chama o método responsável por avançar para o próximo caractere

    def advance(self):                            # Método: responsável por avançar para o próximo caracter do texto
        self.position.advance(self.current_char)                            # Aumenta o contador
        if self.position.index < len(self.text):            # Se o contador for menor que o tamanho total do texto
            self.current_char = self.text[self.position.index]       # Então o caracter atual recebe o caracter da posição no texto
        else:                                         # Se não
            self.current_char = None                      # O caracter atual lido recebe valor nulo

    def generate_tokens(self):                     # Método: gera uma lista de tokens adicionando-os de acordo com as regras
        tokens = []

        while self.current_char != None:              # Enquanto ainda tem texto para ler
            if self.current_char in ' \t\r':                # Se o caracter lido for espaço ou tab, ele apenas avança para o próximo
                self.advance()
            elif self.current_char in LETTERS:             # Se o caracter lido for um dígito (0123456789), ele chama um método responsável por verificar o número, se possui ponto decimal, mais de um caracter e etc
                identifier = self.generate_identifier()
                tokens.append(identifier)
            elif self.current_char in DIGITS:             # Se o caracter lido for um dígito (0123456789), ele chama um método responsável por verificar o número, se possui ponto decimal, mais de um caracter e etc
                number = self.generate_number()
                tokens.append(number)
            elif self.current_char == '+':                # Se o caracter lido for um "+" adiciona na lista de tokens o token do tipo PLUS (mais) e avança para o próximo caractere
                tokens.append(Token(TokenType.PLUS, start_position=self.position))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TokenType.MINUS, start_position=self.position))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TokenType.DIVIDE, start_position=self.position))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TokenType.MULTIPLY, start_position=self.position))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TokenType.LPAREN, start_position=self.position))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TokenType.RPAREN, start_position=self.position))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TokenType.POWER, start_position=self.position))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(TokenType.EQUALS, start_position=self.position))
                self.advance()
            else:
                start_position = self.position.position_copy()
                char = self.current_char
                self.advance()
                return [], Error(start_position, self.position, "Caracter inválido", f"'{char}'")

        tokens.append(Token(TokenType().EOF, start_position=self.position))
        return tokens, None

    def generate_number(self):                      # Método: responsável por verificar os números e gerar o token de número
        number_string = ''                            # inicialmente o número ainda em texto é vazio
        decimal_dot_count = 0                         # inclui um contador de pontos decimais
        start_position = self.position.position_copy()

        while self.current_char != None and self.current_char in DIGITS + '.':  # Enquanto o caracter atual ainda não é nulo e é um dígito
            if self.current_char == '.':          # Se o caracter atual for um ponto decimal
                if decimal_dot_count == 1:            # Se a quantidade de pontos decimais já for igual a 1, então há mais de um ponto seguido e deve gerar um erro
                    return
                decimal_dot_count += 1                # adiciona 1 ao contador de ponto
                number_string += '.'                  # e inclui no número ainda texto o ponto decimal
            else:
                number_string += self.current_char    # Se não, apenas adiciona ao número em texto o caracter do número lido
            self.advance()
        return Token(TokenType.NUMBER, float(number_string), start_position, self.position)  # Retorna um token do tipo NUMBER com seu respectivo valor já convertido para float

    def generate_identifier(self):
        identifier_string = ''
        start_position = self.position.position_copy()

        while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
            identifier_string += self.current_char
            self.advance()

        token_type = TokenType().KEYWORD if identifier_string in TokenType().KEYWORDS else TokenType().IDENTIFIER

        return Token(token_type, identifier_string, start_position, self.position)
