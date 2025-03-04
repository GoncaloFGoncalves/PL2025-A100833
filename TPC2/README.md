# TPC2 - Análise de um dataset de obras musicai

## Autor: 

#### Gonçalo Faria Gonçalves (a100833)


## Explicação: 
O script é um processador de dados musicais que foi projetado para ser flexível, eficiente e fácil de usar. A ideia principal é criar um sistema que possa ler um arquivo de dados musicais e permitir diferentes tipos de análise de forma simples e rápida.

Este processo passa por, numa primeira fase, ler o ficheiro recebido como argumento, usando expressões regulares para separar os campos, lidando com campos que podem conter vírgulas, aspas ou quebras de linha. Para além disso, converte cada linha em um dicionário com chaves correspondentes ao cabeçalho presente na 1ª linha do ficheiro **.csv**. Desta primeira leitura, resulta um dicionário com os dados lidos, sendo criado uma classe de nome `ProcessadorMusical` onde é guardado o dicionário, assim como o resultado das funcionalidades requeridas quando chamadas, não sendo necessário processar os dados mais do que uma vez, no caso de se querer visualizar o resultado de uma funcionalidade já realizada.

## Lógica:

O primeiro passo passa por inicializar a classe `ProcessadorMusical` onde será guardado o dicionário depois da leitura do ficheiro, assim como as respetivas soluções aos problemas a resolver, num primeiro momento, inicializadas como `None`.

Logo depois deste passo **0**, é-nos apresentado o menu principal com as seguintes opções:

1. Listar Compositores Por Ordem Alfabética

2. Distribuição de Obras por Período

3. Listar as obras correspondentes a cada período de forma ordenada

4. Sair

Caso tenha escolhido a primeira opção, ser-lhe-á apresentada um `Set` de compositores, ordenados alfabeticamente. Quando o método é chamado, é primeiro verificado se o valor de `_compositores_cache` é `None` e caso seja, é feito o processamento e é guardado o resultado na variável `_compositores_cache`. Caso o valor não seja `None`, então isso significa que o processamento já foi feito, sendo apenas necessário apresentar o resultado guardado previamente.

Caso tenha escolhido a segunda opção, semelhante ao processo descrito em cima, tmabém será verificado se já existe um resultado guardado ou não e caso não exista, são contadas quantas obras existem em cada período histórico, resultando daí um dicionário com o período como chave e o número de obras como valor.

Por último, a mesma ideia se aplica e caso ainda não exista resultado, são agrupadas as obras por período histórico, criando um dicionário onde cada chave é um período e o valor de cada chave é uma lista de títulos de obras.


