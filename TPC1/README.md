# TPC1: Somador on/off

## Autor: 

#### Gonçalo Faria Gonçalves (a100833)


## Explicação: 
Este script recebe continuamente linhas de texto e, segundo um booleano, vai adicionando ou não todos os números que vai encontrando a um resultado final. Este resultado é depois consultado sempre que aparece o caracter **=**. Para além disso, sempre que aparecem as palavras-chave **on** e **off**, o booleano liga ou desliga, retomando ou parando a soma dos números encontrados no texto, respetivamente. Este processo termina quando o utilizador insere uma linha vazia.

## Lógica:

O primeiro passo passa por escolher como o utilizador vai querer inserir o texto a ser lido, se por um ficheiro se manualmente. Se for a primeira opção, o utilizador insere o texto no terminal e ele é processado, já se for a segunda opção, o texto dentro do ficheiro especificado será lido e processado.

Após a inserção ou leitura do input, este texto será utilizado como argumento pela função responsável pelo processamento.

Agora sim começa o processamento do texto. 
Primeiramente, são criadas 3 variáveis:

- `total_sum`, que armazena o valor do resultado até à data, começando em **0** ;

- `current_number`, que guarda a string do valor que está a ser lido;

- `is_summing`, que representa o estado **on** ou **off**, sendo inicializado a `True`;

Em seguida, são percorridas todas as linhas do texto, uma a uma. Cada linha é percorrida caractér a caractér, onde primeiramente, é verificado o estado do **booleano** está a `True`. Se sim, então, faz-se a verificação de se o caractér a ser inspecionado é um dígito e em caso verdadeiro, este é concatenado à string `current_number`. Caso este não seja dígito, significa que o último número não contém mais dígitos, sendo o número guardado no `current_number` adicionado ao `total_sum`, tornando o `current_number` numa string vazia, preparada para receber o próximo número. 

Em seguida, é feita a confirmação se estamos perante um comando **on** ou **off**. Esta confirmação é feita, chamando a função auxiliar `process_command` que recebe a linha atual e o índice do caractér que está a ser verificada. Nesta função axuliar, primeiramente, verifica-se se o caractér atual é igual a `o`, e caso seja, verifica-se se os caractéres logo a seguir compõem as palavras-chave **on** ou **off**. É retornada a palavra-chave correspondente e o número de "casas" a avançar, 2 no caso de **on** e 3 no caso de **off**. Ao retornar o valor, o valor do `is_summing` é passado para o inverso, caso o seu valor atual seja diferente do valor recebiido.

Por último, é feita a verificação se o caractér atual equivale ao `=`, e caso seja, apresenta no terminal o valor somado até agora. Já no final do processamento do texto por completo, é imprimido no terminal o valor total da soma.


### Testar o programa a funcionar:

1. No terminal, insira: 
<pre>$ python <a href="somadorOnOff.py">somadorOnOff.py</a>
</pre>

2. Selecione a opção pretendida, 1 para texto manual, 2 para leitura de ficheiro

3. Caso tenha escolhido a opção de inserir manualmente:
    
    3.1. Insira o texto com números e as palavras-chave **on** e **off**.
    
    3.2. Os números serão adicionados enquando o estado for **on** e deixarão de o ser aquando da mudança de estado.

    3.3. Insira **=** para imprimir o resultado.

    3.4. Para terminar, basta inserir uma linha vazia, sendo apresentado o resultado final.

4. Caso tenha escolido a opção de inserir um ficheiro de texto:

    4.1. Insira o caminho para o ficheiro de texto.

    4.2. Será apresentado no terminal o resultado.



## **Exemplo prático**:

Entrada:

`123 abc 12 off 5 on 6 =`

Saída:

`Soma = 141`

`Soma final = 141`

A soma para na palavra-chave **off**, ignorando o 5, retomando no **on**, onde depois é adicionado o 5.