import re
import sys

def converter_markdown_para_html(markdown_texto):
    """
    Converte texto Markdown para HTML suportando:
    - Cabeçalhos
    - Negrito
    - Itálico
    - Listas numeradas
    - Links
    - Imagens
    """
    def processar_cabecalhos(texto):
        padrao_cabecalhos = r'^(#{1,6})\s+(.+)$'
        def substituir_cabecalho(match):
            nivel = len(match.group(1))
            return f'<h{nivel}>{match.group(2)}</h{nivel}>'
        return re.sub(padrao_cabecalhos, substituir_cabecalho, texto, flags=re.MULTILINE)
    
    def processar_negrito(texto):
        return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', texto)
    
    def processar_italico(texto):
        return re.sub(r'\*(.*?)\*', r'<i>\1</i>', texto)
    
    def processar_listas_numeradas(texto):
        linhas = texto.split('\n')
        lista_atual = []
        resultado = []
        
        for linha in linhas:
            match = re.match(r'^(\d+)\.\s+(.+)$', linha)
            if match:
                lista_atual.append(f'<li>{match.group(2)}</li>')
            else:
                if lista_atual:
                    resultado.append('<ol>')
                    resultado.extend(lista_atual)
                    resultado.append('</ol>')
                    lista_atual = []
                resultado.append(linha)
        
        if lista_atual:
            resultado.append('<ol>')
            resultado.extend(lista_atual)
            resultado.append('</ol>')
        
        return '\n'.join(resultado)
    
    def processar_links(texto):
        return re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', texto)
    
    def processar_imagens(texto):
        return re.sub(r'!\[([^\]]+)\]\(([^\)]+)\)', r'<img src="\2" alt="\1"/>', texto)
    
    texto_processado = markdown_texto
    texto_processado = processar_imagens(texto_processado)
    texto_processado = processar_links(texto_processado)
    texto_processado = processar_cabecalhos(texto_processado)
    texto_processado = processar_listas_numeradas(texto_processado)
    texto_processado = processar_negrito(texto_processado)
    texto_processado = processar_italico(texto_processado)
    
    return texto_processado

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <arquivo_entrada.md> <arquivo_saida.html>")
        sys.exit(1)
    
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            markdown_texto = f.read()
        
        html_texto = converter_markdown_para_html(markdown_texto)
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(html_texto)
        
        print(f"Conversão concluída. HTML salvo em {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao processar arquivos: {e}")

if __name__ == "__main__":
    main()
