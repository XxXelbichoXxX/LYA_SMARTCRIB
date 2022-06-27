from analizadorLexico import tokens

import os

import ply.yacc as yacc

import Codigo_Fuente.variables as v
from Codigo_Fuente.Funciones.camara import encenderCamara
from Codigo_Fuente.Funciones.musica import musica

# para errores que tengamos en nuestro analizador
# de tipo reduce
precedencias = (
    ('right','ID','CALL','BGN','IF','WHL','CAMARA'),
    ('left', 'OPRT','CPRT'),
    ('left', 'OKEY','CKEY'),
    ('right', 'EQL'),
    ('left', 'DIF'),
    ('left', 'SML'),
    ('left', 'GTR'),
    ('left', 'SMLE'),
    ('left', 'GRTE'),
    ('left', 'ADD'),
    ('left', 'SUBST'),
    ('left', 'MULT'),
    ('left', 'DIV'),

)


# Terminales son aquellos tokens que definimos
def p_program(p):
	'''program : block'''
	v.resultado = v.resultado + "[program]---> block" + '\n'
	#p[0] = program(p[1],"program")

def p_block(p):
	'''block : constDecl statement'''
	v.resultado = v.resultado + "[block]---> declaracion" + '\n'

def p_constDecl(p):
	'''constDecl : constAssignmentList ENDST'''
	#p[0] = constDecl(p[2])
	#resultado.append("constDecl")

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	#p[0] = Null()
	#resultado.append("nulo")

def p_constAssignmentList1(p):
	'''constAssignmentList : IDF EQL expression'''
	v.resultado = v.resultado + "Asignacion ..." + '\n'

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList ENDST IDF EQL expression'''
	v.resultado = v.resultado + "Asignacion 2..." + '\n'

def p_identList1(p):
	'''identList : IDF'''
	v.resultado = v.resultado + "variable ..." + '\n'

def p_identList2(p):
	'''identList : identList CM IDF'''
	#resultado.append("identList 2")

def p_statement1(p):
	'''statement : CALL CAMARA'''
	v.resultado = v.resultado + "Declaracion: Funcion CAMARA" + '\n'
	os.system("start C:\\LYA_SMARTCRIB-master\\codigo_fuente\\Audio\\Camara.mp3")
	encenderCamara()


def p_statement2(p):
	'''statement : BGN OKEY statementList CKEY'''
	v.resultado = v.resultado + "Declaracion transaccion --->" + '\n'

def p_statement3(p):
	'''statement : IF OPRT condition CPRT OKEY constDecl statement CKEY'''
	v.resultado = v.resultado + "Declaracion Bloque IF ---> condicional" + '\n'
	v.resultado = v.resultado + "BloqueDeclaracion --> declaracion" + '\n'

def p_statement4(p):
	'''statement : WHL OPRT condition CPRT  OKEY statement CKEY'''
	v.resultado = v.resultado + "Declaracion Bloque WHILE ---> condicional" + '\n'
	v.resultado = v.resultado + "BloqueDeclaracion --> declaracion" + '\n'

def p_statement5(p):
	'''statement : DO OKEY constDecl statement CKEY WHL OPRT condition CPRT'''
	v.resultado = v.resultado + "Declaracion Bloque DO WHILE ---> condicional" + '\n'
	v.resultado = v.resultado + "BloqueDeclaracion --> declaracion" + '\n'

def p_statement6(p):
	'''statement : CALL MUSICA'''
	v.resultado = v.resultado + "Declaracion: Funcion Musica" + '\n'
	os.system("start C:\\LYA_SMARTCRIB-master\\codigo_fuente\\Audio\\Musica.mp3")
	musica()
def p_statementEmpty(p):
	'''statement : empty'''
	#resultado.append("nulo")

def p_statementList1(p):
	'''statementList : statement'''
	#resultado.append("statementList 1")

def p_statementList2(p):
	'''statementList : statementList ENDST statement'''
	#resultado.append("statementList 2")

def p_condition1(p):
	'''condition : expression relation expression'''
	v.resultado = v.resultado + "condicional ---> relacional" + '\n'

def p_relation1(p):
	'''relation : EQL'''
	v.resultado = v.resultado + "igual a ..." + '\n'

def p_relation2(p):
	'''relation : DIF'''
	v.resultado = v.resultado + "diferente a ..." '\n'

def p_relation3(p):
	'''relation : SML'''
	v.resultado = v.resultado+ "menor que ..." + '\n'

def p_relation4(p):
	'''relation : GRT'''
	v.resultado = v.resultado + "mayor que ..." + '\n'

def p_relation5(p):
	'''relation : SMLE'''
	v.resultado = v.resultado + "menor igual que ..." + '\n'

def p_relation6(p):
	'''relation : GRTE'''
	v.resultado = v.resultado + "mayor igual que ..." + '\n'

def p_expression1(p):
	'''expression : term'''
	#resultado.append("expresion 1")

def p_expression2(p):
	'''expression : addingOperator term'''
	#resultado.append("expresion 2")

def p_expression3(p):
	'''expression : expression addingOperator term'''
	#resultado.append("expresion 3")

def p_addingOperator1(p):
	'''addingOperator : ADD'''
	v.resultado = v.resultado + "suma ..." + '\n'

def p_addingOperator2(p):
	'''addingOperator : SUBST'''
	v.resultado = v.resultado + "resta ..." + '\n'

def p_term1(p):
	'''term : factor'''
	#resultado.append("term 1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	#resultado.append("term 1")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : DIV'''
	v.resultado = v.resultado + "Division ..." + '\n'

def p_factor1(p):
	'''factor : IDF'''
	v.resultado = v.resultado + "variable ..." + '\n'

def p_factor2(p):
	'''factor : INT'''
	v.resultado = v.resultado + "entero ..." + '\n'

def p_factor3(p):
	'''factor : OPRT expression CPRT'''
	#resultado.append("condicional")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
    v.resultado = v.resultado + '¡¡¡ ERROR: Expresion: ' + str(p.value) + ' !!!\n'

def archivo(cadena):
    cadena = cadena.upper()
    parser = yacc.yacc()
    # ya no es necesario esta variable puesto que se guarda todo en resultado
    result = parser.parse(cadena)
    #print(result)
    return v.resultado