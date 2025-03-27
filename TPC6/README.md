# TPC6 - Recursivo Descendente para expressões aritméticas

Autor: Gonçalo Faria Gonçalves (a100833)


## Introdução

O presente relatório descreve a implementação de uma calculadora interativa utilizando as bibliotecas PLY (Python Lex-Yacc) para análise léxica e sintática de expressões matemáticas. O sistema permite a realização de cálculos aritméticos básicos com suporte a operações fundamentais e parênteses.

## Componentes do Sistema

### Análise Léxica (Lexer)

Os tokens reconhecidos pelo sistema incluem:
- `NUMBER`: Números inteiros
- `PLUS`: Operador de adição (+)
- `MINUS`: Operador de subtração (-)
- `TIMES`: Operador de multiplicação (*)
- `DIVIDE`: Operador de divisão (/)
- `LPAREN`: Parêntese esquerdo
- `RPAREN`: Parêntese direito

### Análise Sintática (Parser)

O parser implementa as seguintes regras gramaticais:
- Expressões podem ser compostas por adição e subtração
- Termos podem ser multiplicados e divididos
- Suporte a agrupamento de expressões com parênteses
- Tratamento de precedência de operadores

## Funcionalidades Principais

- Cálculo de expressões matemáticas
- Tratamento de erros de sintaxe
- Prevenção de divisão por zero
- Interface interativa de linha de comando
- Opção de saída a qualquer momento

## Exemplo de Uso

```python
Expressão: 2+3
Resultado: 5

Expressão: 67-(2+3*4)
Resultado: 55

Expressão: (9-2)*(13-4)
Resultado: 63
```

## Tratamento de Erros

O sistema possui mecanismos de tratamento de erros para:
- Caracteres ilegais
- Erros de sintaxe
- Divisão por zero
