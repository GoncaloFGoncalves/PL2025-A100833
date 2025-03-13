# TPC5: Máquina De Vending

Autor: Gonçalo Faria Gonçalves (a100833)

## Executação
Para executar o programa:

```bash
    $ python3 vending.py stock.json
```

## Comandos Disponíveis

Os comandos disponiveis são:

- LISTAR: Lista os produtos disponíveis no stock.
- SELECIONAR (ID DO PRODUTO): Permite ao cliente selecionar um produto pelo seu ID.
- DEPOSITAR: Permite ao cliente depositar moedas na máquina. O programa aceita as seguintes moedas: 2€, 1€, 50c, 20c, 10c, 5c, 2c, 1c.
- SAIR: Encerra o programa.

## Resultados

Para o seguinte input:
```
   >> LISTAR
```

Devemos obter o output de:
```
    A23 Água Mineral 1L 12 1.5
    B13 Pacote de Salgadinhos 20 1.8
    C31 Barra de Cereal 8 1.2
    D05 Suco de Frutas 18 2.0
    E18 Sanduíche de Presunto 5 4.0
    F15 Salada de Frutas 3 3.8
    G02 Biscoitos Recheados 10 1.0
    H20 Balas de Goma 15 1.5
    I12 Banana 20 0.5
    J09 Pacote de Castanhas 2 2.5
```

Outro caso seria, por exemplo:

Para o seguinte input:
```
   >> DEPOSITAR
   >> 2e
```

Devemos obter o output de:
```
    Moedas aceitas: 2€, 1€, 50c, 20c, 10c, 5c, 2c, 1c
    Valor depositado: 2
```

E por ultimo:

Para o seguinte input:
```
    >> SELECIONAR J09
```

Devemos obter o output de:
```
    Produto selecionado: Pacote de Castanhas
    Saldo restante: 1.5
    Quantidade restante: 1
    Entregue 1e
    Entregue 50c
```