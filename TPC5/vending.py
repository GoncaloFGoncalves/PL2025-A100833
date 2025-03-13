import ply.lex as lex 
import json
import sys
from datetime import datetime

chicoCoins = [("2e",2), ("1e",1), ("50c",0.50), ("20c",0.20), ("10c",0.10), ("5c",0.05), ("2c",0.02), ("1c",0.01)]

def loadJson(file):
    with open(file, 'r') as jf:
        return json.load(jf)['stock']
    
tokens = (
    'SELECIONAR',
    'DEPOSITAR',
    'LISTAR',
    'SAIR',
    'VIRGULA',
    'COIN',
    'ID'
)
    
t_LISTAR = r'LISTAR'
t_DEPOSITAR = r'DEPOSITAR'
t_SELECIONAR =  r'SELECIONAR'
t_SAIR = r'SAIR'
t_VIRGULA = r','
t_COIN = r'\d+(e|c)'
t_ID = r'[A-Z]\d{2}'
    
t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    jsonFile = sys.argv[1]
    stock = loadJson(jsonFile)
    
    saldo = 0
    
    print(f"{datetime.now().date()}, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.")
    
    sair = False

    while not sair:
        data = input(">> ")
        lexer.input(data)
        tok = lexer.token()

        if tok:
            if tok.type == 'LISTAR':
                print ("""cod | nome | quantidade | preço
    ---------------------------------""")
                for p in stock:
                    print(f"{p['cod']} {p['nome']} {p['quant']} {p['preco']}")
            
            elif tok.type == 'SELECIONAR':
                tok = lexer.token()
                if tok and tok.type == 'ID':
                    produto_selecionado = None
                    for p in stock:
                        if p['cod'] == tok.value:
                            produto_selecionado = p
                            break
                    
                    if produto_selecionado:
                        if saldo >= produto_selecionado['preco']:
                            print(f"Produto selecionado: {produto_selecionado['nome']}")

                            # Atualizar saldo
                            saldo -= produto_selecionado['preco']
                            print(f"Saldo restante: {saldo}")

                            # Atualizar quantidade no estoque
                            produto_selecionado['quant'] -= 1
                            print(f"Quantidade restante: {produto_selecionado['quant']}")

                            # Calcular troco
                            troco = saldo
                            for coin, value in chicoCoins:
                                while troco >= value:
                                    print(f"Entregue {coin}")
                                    troco -= value
                            saldo = 0  # Zerar saldo após a compra
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Produto não encontrado.")
                else:
                    print("Utilize: \"SELECIONAR (ID DO PRODUTO)\" ")
            
            elif tok.type == 'DEPOSITAR':
                valor_depositado = 0
                while True:
                    print("Moedas aceitas: 2€, 1€, 50c, 20c, 10c, 5c, 2c, 1c")
                    moeda = input("Insira a moeda (ou 'cancelar' para interromper): ").lower()
                    if moeda == 'cancelar':
                        break
                    for coin, value in chicoCoins:
                        if moeda == coin.lower():
                            valor_depositado += value
                            saldo += value
                            print(f"Valor depositado: {valor_depositado}")
                            break
                    else:
                        print("Moeda inválida.")
                
                print(f"Saldo total: {saldo}")

            elif tok.type == 'SAIR':
                sair = True
        else:
            print("Entrada inválida.")
