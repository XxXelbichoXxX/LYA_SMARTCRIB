import ply.lex as lex
import os
from Codigo_Fuente import variables as v

# Seccion de analisis lexico

resv = ['BGN', 'END', 'IF', 'ELSE', 'WHL', 'DO', 'PCD',
        'CALL', 'INT', 'FLT', 'CHR', 'STR','ENDL', 'AND','OR','NOT','CAMARA', 'MUSICA']

tokens = resv + ['ADD', 'SUBST', 'MULT', 'DIV', 'EQL', 'EQL_SUM',
                 'EQL_SUB', 'EQL_MULT', 'EQL_DIV', 'DIF', 'SML',
                 'GRT', 'SMLE', 'GRTE', 'OPRT', 'CPRT', 'OKEY', 'CKEY',
                 'OBRT', 'CBRT', 'CM', 'ENDST', 'IDF', 'COMMENT']
t_ADD = r'\+'
t_SUBST = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_EQL = r'='
t_OR= r'\|{2}'
t_AND=r'\&\&'
t_EQL_SUM = r'\+='
t_EQL_SUB = r'\-='
t_EQL_MULT = r'\*='
t_EQL_DIV = r'/='
t_DIF = r'!='
t_SML = r'<'
t_GRT = r'>'
t_SMLE = r'<='
t_GRTE = r'>='
t_OPRT = r'\('
t_CPRT = r'\)'
t_OKEY = r'\{'
t_CKEY = r'\}'
t_OBRT = r'\['
t_CBRT = r'\]'
t_CM = r','
t_ENDST = r';'

def t_error(t):
    os.system("C:\\LYA_SMARTCRIB-master\\codigo_fuente\\Audio\\error.mp3")
    t.lexer.skip(1)
    v.cError += 1
    return t

def t_END(t):
	r'endl'
	return t

def t_IDF(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value.upper() in resv:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_STRING(t):
    r'\"[a-zA-Z][a-zA-Z]*\"'
    if t.value.upper() in resv:
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NONSPACE(t):
    r'\s'
    pass

def t_COMMENT(t):
    r'\$.*'
    pass

def t_FLT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHR(t):
    r'\"[a-zA-Z]\"'
    t.value = t.value[1:-1]  # NOS AYUDA A ELIMINAR LAS COMILLAS
    return t

def obtenerLexico(cad):
    toxic = lex.lex()
    toxic.input(cad)
    while True:
        tokens = toxic.token()
        if not tokens: break
        v.arreglo = v.arreglo + 'Renglon ' + str(tokens.lineno) + ': ' + str(tokens.value) + ' Forma parte de: ' + str(tokens.type)+'\n'
        if v.cError == 1:
            v.arreglo = 'Analizador lexico\n'+'¡¡¡ ERROR: Renglon ' + str(tokens.lineno) + ': El siguiente token no es valido:' + \
                        str(tokens.value[0]) + '\n' +'NO SE PUEDE CONTINUAR'
            return v.arreglo,1
    return v.arreglo,0

