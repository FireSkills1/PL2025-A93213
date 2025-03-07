import ply.lex as lex

# Define reserved words
reserved_words = {
    'SELECT': 'SELECT',
    'WHERE': 'WHERE',
    'LIMIT': 'LIMIT'
}

# Token list
tokens = [
    'COMMENT', 'VARIABLE', 'INTEGER', 'URIREF', 'TEXT', 'LANGTAG',
    'A_KEYWORD', 'PERIOD', 'LBRACE', 'RBRACE', 'IDENTIFIER'
] + list(reserved_words.values())

# Regular expressions
t_ignore = ' \t'
t_PERIOD = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMENT = r'\#.*'
t_LANGTAG = r'@[a-z]{2,3}(-[a-z]{2,3})?'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value.upper(), 'IDENTIFIER')
    return t

def t_newline_or_text(t):
    r'("[^"]*")|\n+'
    if '\n' in t.value:
        t.lexer.lineno += len(t.value)
    else:
        t.type = 'TEXT'
    return t

def t_variable_or_uri(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z_][a-zA-Z0-9_-]*'
    if t.value.startswith('?'):
        t.type = 'VARIABLE'
    else:
        t.type = 'URIREF'
    return t

def t_A_or_integer(t):
    r'\ba\b|\d+'
    if t.value.isdigit():
        t.type = 'INTEGER'
        t.value = int(t.value)
    else:
        t.type = 'A_KEYWORD'
    return t

def t_error(t):
    print(f"Unexpected character: {t.value[0]}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Test input
sample_text = """
# DBPedia: Works by Chuck Berry
select ?name ?description where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?name.
    ?w dbo:abstract ?description
} LIMIT 1000
"""

lexer.input(sample_text)
for token in lexer:
    print(token.type, token.value)