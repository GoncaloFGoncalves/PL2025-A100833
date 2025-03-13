import re
import sys
from enum import Enum

class TipoToken(Enum):
    COMENTARIO = 'COMMENT'
    PALAVRA_CHAVE = 'KEYWORD'
    VARIAVEL = 'VARIABLE'
    LITERAL_STRING = 'STRING'
    LITERAL_IDIOMA = 'LANGUAGE'
    OPERADOR = 'OPERATOR'
    DELIMITADOR = 'DELIMITER'
    PREFIXO = 'PREFIX'
    URI = 'URI'
    NUMERO = 'NUMBER'
    DESCONHECIDO = 'UNKNOWN'

class Token:
    def __init__(self, tipo, valor, linha, coluna):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
        self.coluna = coluna
    
    def __str__(self):
        # Formatação como solicitado: ('TIPO', 'valor')
        return f"('{self.tipo.value}', '{self.valor}')"

class AnalisadorLexico:
    def __init__(self):
        self.palavras_chave = [
            'select', 'where', 'filter', 'optional', 'union', 'minus',
            'graph', 'service', 'bind', 'as', 'group', 'by', 'having',
            'order', 'limit', 'offset', 'values', 'a'
        ]
        
        self.operadores = [
            '.', ',', ';', '=', '!=', '<', '>', '<=', '>=', '+', '-', '*', '/', '&&', '||', '!'
        ]
        
        self.delimitadores = ['{', '}', '(', ')', '[', ']']
        
    def analisar(self, texto):
        tokens = []
        linhas = texto.split('\n')
        
        for num_linha, linha in enumerate(linhas, 1):
            index = 0
            tamanho = len(linha)
            
            while index < tamanho:
                char = linha[index]
                
                # Ignorar espaços em branco
                if char.isspace():
                    index += 1
                    continue
                
                # Comentários
                if char == '#':
                    comentario = linha[index:]
                    tokens.append(Token(TipoToken.COMENTARIO, comentario.strip(), num_linha, index + 1))
                    break  # O comentário vai até o final da linha
                
                # Variáveis - começam com ?
                if char == '?':
                    inicio = index
                    index += 1
                    while index < tamanho and (linha[index].isalnum() or linha[index] == '_'):
                        index += 1
                    nome_var = linha[inicio:index]
                    tokens.append(Token(TipoToken.VARIAVEL, nome_var, num_linha, inicio + 1))
                    continue
                
                # Strings entre aspas
                if char == '"':
                    inicio = index
                    index += 1
                    # Buscar o fechamento das aspas
                    while index < tamanho and linha[index] != '"':
                        if linha[index] == '\\' and index + 1 < tamanho:  # Escape character
                            index += 2
                        else:
                            index += 1
                    
                    if index < tamanho:  # Se encontrou as aspas de fechamento
                        index += 1
                        string_valor = linha[inicio:index]
                        tokens.append(Token(TipoToken.LITERAL_STRING, string_valor, num_linha, inicio + 1))
                        
                        # Verificar se há tag de idioma (@en, @pt, etc)
                        if index < tamanho and linha[index] == '@':
                            inicio_idioma = index
                            index += 1
                            while index < tamanho and (linha[index].isalnum() or linha[index] == '-'):
                                index += 1
                            idioma = linha[inicio_idioma:index]
                            tokens.append(Token(TipoToken.LITERAL_IDIOMA, idioma, num_linha, inicio_idioma + 1))
                    else:
                        # String não fechada - erro
                        tokens.append(Token(TipoToken.DESCONHECIDO, linha[inicio:], num_linha, inicio + 1))
                        index = tamanho
                    continue
                
                # Prefixos (dbo:, foaf:, etc)
                prefixo_match = re.match(r'([a-z]+):', linha[index:])
                if prefixo_match:
                    prefixo = prefixo_match.group(0)
                    tokens.append(Token(TipoToken.PREFIXO, prefixo, num_linha, index + 1))
                    index += len(prefixo)
                    continue
                
                # Operadores compostos (>=, <=, !=, &&, ||)
                if index + 1 < tamanho and linha[index:index+2] in self.operadores:
                    tokens.append(Token(TipoToken.OPERADOR, linha[index:index+2], num_linha, index + 1))
                    index += 2
                    continue
                
                # Operadores simples e delimitadores
                if char in self.operadores:
                    tokens.append(Token(TipoToken.OPERADOR, char, num_linha, index + 1))
                    index += 1
                    continue
                
                if char in self.delimitadores:
                    tokens.append(Token(TipoToken.DELIMITADOR, char, num_linha, index + 1))
                    index += 1
                    continue
                
                # Números
                num_match = re.match(r'\d+(\.\d+)?', linha[index:])
                if num_match:
                    numero = num_match.group(0)
                    tokens.append(Token(TipoToken.NUMERO, numero, num_linha, index + 1))
                    index += len(numero)
                    continue
                
                # Palavras (identificadores, palavras-chave)
                if char.isalpha() or char == '_':
                    inicio = index
                    index += 1
                    while index < tamanho and (linha[index].isalnum() or linha[index] == '_'):
                        index += 1
                    palavra = linha[inicio:index].lower()
                    
                    if palavra in self.palavras_chave:
                        # Para palavras-chave, mantemos o valor original (pode estar em maiúsculas ou minúsculas)
                        original_palavra = linha[inicio:index]
                        tokens.append(Token(TipoToken.PALAVRA_CHAVE, original_palavra, num_linha, inicio + 1))
                    else:
                        # URIs ou identificadores normais
                        original_palavra = linha[inicio:index]
                        tokens.append(Token(TipoToken.URI, original_palavra, num_linha, inicio + 1))
                    continue
                
                # Caracteres desconhecidos
                tokens.append(Token(TipoToken.DESCONHECIDO, char, num_linha, index + 1))
                index += 1
        
        return tokens


def main():
    # Verificar se o nome do arquivo foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Uso: python analisador_lexico.py <nome_do_arquivo>")
        sys.exit(1)
    
    nome_arquivo = sys.argv[1]
    
    try:
        # Abrir e ler o arquivo
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        # Executar a análise léxica
        analisador = AnalisadorLexico()
        tokens = analisador.analisar(conteudo)
        
        # Imprimir os tokens identificados no formato solicitado
        for token in tokens:
            print(token)
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()