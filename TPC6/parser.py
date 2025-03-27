import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    if p[3] == 0:
        raise ValueError("Divisão por zero")
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print(f"Erro de sintaxe: {p}")

# Criação do parser
parser = yacc.yacc()

def calcular_expressao(expressao):
    try:
        return parser.parse(expressao)
    except Exception as e:
        return f"Erro: {e}"

def main():
    print("Calculadora Interativa")
    print("Digite uma expressão matemática ou 'quit' para sair.")
    
    while True:
        try:
            entrada = input("Expressão: ").strip()
            
            # Verificar se o usuário quer sair
            if entrada.lower() == 'quit' or entrada.lower() == 'sair':
                print("Saindo...")
                break
            
            # Calcular e mostrar o resultado
            resultado = calcular_expressao(entrada)
            print(f"Resultado: {resultado}")
        
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Executar o programa principal
if __name__ == "__main__":
    main()