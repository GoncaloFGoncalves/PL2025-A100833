# TPC4 - Analisador Léxico

## Autor: 

#### Gonçalo Faria Gonçalves (a100833)

Este projeto implementa um analisador léxico para uma linguagem de consulta semelhante a SPARQL, usada para consultar bases de conhecimento como a DBPedia.

## Visão Geral

O analisador léxico (ou scanner) é a primeira fase de um compilador ou interpretador. Ele é responsável por quebrar o código fonte em tokens - os elementos básicos da linguagem, como palavras-chave, identificadores, operadores, etc.

## Funcionamento do Analisador

### Processo de Análise Léxica

1. **Entrada**: Um arquivo de texto contendo a query
2. **Processamento**: O texto é lido caractere por caractere e convertido em tokens
3. **Saída**: Uma sequência de tokens formatados como tuplas ('TIPO', 'valor')

### Tipos de Tokens Reconhecidos

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| COMMENT | Comentários iniciados com # | # DBPedia: obras de Chuck Berry |
| KEYWORD | Palavras reservadas da linguagem | select, where, LIMIT |
| VARIABLE | Variáveis iniciadas com ? | ?nome, ?desc |
| STRING | Literais de string entre aspas | "Chuck Berry" |
| LANGUAGE | Tags de idioma | @en |
| OPERATOR | Operadores da linguagem | . , ; = |
| DELIMITER | Delimitadores | { } ( ) |
| PREFIX | Prefixos de namespace | dbo:, foaf: |
| URI | Identificadores e URIs | MusicalArtist, artist |
| NUMBER | Valores numéricos | 1000 |
| UNKNOWN | Tokens não reconhecidos | |

## Uso do Programa

Para executar o analisador léxico:

```bash
python main.py caminho/para/ficheiro.txt
```

### Exemplo de Entrada

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

### Exemplo de Saída

```
('COMMENT', '# DBPedia: obras de Chuck Berry')
('KEYWORD', 'select')
('VARIABLE', '?nome')
('VARIABLE', '?desc')
('KEYWORD', 'where')
('DELIMITER', '{')
('VARIABLE', '?s')
('KEYWORD', 'a')
('PREFIX', 'dbo:')
('URI', 'MusicalArtist')
('OPERATOR', '.')
...
('KEYWORD', 'LIMIT')
('NUMBER', '1000')
```

## Implementação

O código do analisador léxico está estruturado da seguinte forma:

- **Classe TipoToken**: Enumeração com os tipos de tokens reconhecidos
- **Classe Token**: Representa um token com seu tipo, valor, linha e coluna
- **Classe AnalisadorLexico**: Contém a lógica de análise
- **Função main()**: Ponto de entrada que lê o arquivo e executa a análise
