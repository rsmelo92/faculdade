from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'talquei')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'Brasil acima de tudo')
        self.lexer.add('CLOSE_PAREN', r'Deus acima de todos')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'va')
        self.lexer.add('SUB', r'ga')
        self.lexer.add('MUL', r'bun')
        self.lexer.add('DIV', r'do')
        # Number
        self.lexer.add('NUMBER', r'1')
        # String
        self.lexer.add('STRING', r'\w+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
