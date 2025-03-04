# TPC2 - Análise de um dataset de obras musicai

## Autor: 

#### Gonçalo Faria Gonçalves (a100833)


## Explicação:

O script é um conversor de Markdown para HTML que transforma documentos escritos em sintaxe Markdown em ficheiros HTML formatados. O programa recebe um ficheiro de entrada em Markdown, processa sequencialmente diferentes elementos de formatação, como cabeçalhos, texto em negrito, itálico, listas numeradas, links e imagens, aplicando as correspondentes tags HTML. O resultado é guardado num ficheiro de saída HTML, que preserva a estrutura e formatação do documento original, tornando o conteúdo renderizável em navegadores web.

## Lógica:

A função `processar_cabecalhos()` identifica cabeçalhos e os converte para as tags HTML `<h1>` a `<h6>`, preservando a estrutura hierárquica. Para formatação de texto, `processar_negrito()` transforma trechos entre `** **` em `<b>`, enquanto `processar_italico()` converte texto entre `* *` em `<i>`, garantindo a ênfase adequada. A formatação de listas ordenadas é realizada por `processar_listas_numeradas()`, que detecta itens numerados no Markdown, os encapsula em `<li>` e os agrupa dentro de `<ol>`, mantendo a estrutura correta. Hiperlinks no formato `[texto](URL)` são convertidos pela função `processar_links()`, que os substitui pela tag `<a href="URL">texto</a>`, tornando-os clicáveis. Da mesma forma, `processar_imagens()` converte imagens Markdown, no formato `![texto alternativo](URL)`, para `<img src="URL" alt="texto alternativo"/>`, permitindo a inclusão de imagens no HTML. O programa principal (`main()`) gerencia a leitura do ficheiro de entrada, executa a conversão e grava o resultado no ficheiro de saída. Caso ocorra algum erro na leitura ou escrita dos ficheiros, uma mensagem de erro é exibida.
