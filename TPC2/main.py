import sys
import re

class ProcessadorMusical:
    def __init__(self, caminho_arquivo):
        """
        Inicializa o processador musical com o caminho do arquivo.
        """
        self.caminho_arquivo = caminho_arquivo
        self.obras = None
        
        # Caches para resultados processados
        self._compositores_cache = None
        self._distribuicao_periodos_cache = None
        self._obras_por_periodo_cache = None

    def ler_dataset(self):
        """
        Lê dataset com suporte a campos com aspas e quebras de linha.
        Carrega os dados apenas uma vez.
        """
        if self.obras is None:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                # Lê o cabeçalho
                cabecalho = arquivo.readline().strip().split(';')
               
                linhas = []
                linha_atual = ""
                dentro_de_aspas = False
               
                for linha in arquivo:
                    linha = linha.strip()
                   
                    if linha:
                        # Adiciona a linha atual se já existir, senão usa a nova linha
                        linha_atual = linha_atual + " " + linha if linha_atual else linha
                       
                        # Alterna o estado de dentro_de_aspas se o número de aspas for ímpar
                        dentro_de_aspas ^= linha.count('"') % 2 == 1
                       
                        # Processa a linha quando não estiver dentro de aspas
                        if not dentro_de_aspas:
                            # Usa regex para separar corretamente os campos
                            valores = re.findall(r'(?:^|;)("(?:[^"]|"")*"|[^;]*)', linha_atual)
                           
                            # Remove aspas extras e substitui aspas duplicadas
                            valores = [v.strip('"').replace('""', '"') for v in valores]
                           
                            # Formata o nome do compositor se existir no cabeçalho
                            if 'compositor' in cabecalho:
                                index_compositor = cabecalho.index('compositor')
                                valores[index_compositor] = valores[index_compositor].strip()
                           
                            # Cria um dicionário associando cabeçalho aos valores
                            linhas.append(dict(zip(cabecalho, valores)))
                           
                            # Reseta a linha atual
                            linha_atual = ""
               
                self.obras = linhas
        
        return self.obras

    def obter_compositores(self):
        """
        Obtém lista de compositores em ordem alfabética.
        Usa cache para evitar reprocessamento.
        """
        if self._compositores_cache is None:
            # Carrega os dados se ainda não carregados
            if self.obras is None:
                self.ler_dataset()
            
            # Processa compositores
            self._compositores_cache = sorted(set(obra['compositor'] for obra in self.obras))
        
        return self._compositores_cache

    def obter_distribuicao_periodos(self):
        """
        Obtém distribuição de obras por período.
        Usa cache para evitar reprocessamento.
        """
        if self._distribuicao_periodos_cache is None:
            # Carrega os dados se ainda não carregados
            if self.obras is None:
                self.ler_dataset()
            
            # Processa distribuição
            distribuicao_periodos = {}
            for obra in self.obras:
                periodo = obra['periodo']
                distribuicao_periodos[periodo] = distribuicao_periodos.get(periodo, 0) + 1
            
            self._distribuicao_periodos_cache = distribuicao_periodos
        
        return self._distribuicao_periodos_cache

    def obter_obras_por_periodo(self):
        """
        Obtém dicionário de obras por período, 
        com títulos em ordem alfabética.
        Usa cache para evitar reprocessamento.
        """
        if self._obras_por_periodo_cache is None:
            # Carrega os dados se ainda não carregados
            if self.obras is None:
                self.ler_dataset()
            
            # Processa obras por período
            obras_por_periodo = {}
            for obra in self.obras:
                periodo = obra['periodo']
                if periodo not in obras_por_periodo:
                    obras_por_periodo[periodo] = []
                obras_por_periodo[periodo].append(obra['nome'])
            
            # Ordenar títulos alfabeticamente em cada período
            for periodo in obras_por_periodo:
                obras_por_periodo[periodo] = sorted(obras_por_periodo[periodo])
            
            self._obras_por_periodo_cache = obras_por_periodo
        
        return self._obras_por_periodo_cache

    def exibir_compositores(self):
        """
        Exibe a lista de compositores em ordem alfabética.
        """
        compositores = self.obter_compositores()
        print("\n1. Compositores (ordem alfabética):")
        for compositor in compositores:
            print(f"  - {compositor}")

    def exibir_distribuicao_periodos(self):
        """
        Exibe a distribuição de obras por período.
        """
        distribuicao = self.obter_distribuicao_periodos()
        print("\n2. Distribuição de Obras por Período:")
        for periodo, quantidade in distribuicao.items():
            print(f"  {periodo}: {quantidade} obra(s)")

    def exibir_obras_por_periodo(self):
        """
        Exibe as obras organizadas por período.
        """
        obras_periodicas = self.obter_obras_por_periodo()
        print("\n3. Obras por Período (ordem alfabética):")
        for periodo, titulos in obras_periodicas.items():
            print(f"\n{periodo}:")
            for titulo in titulos:
                print(f"  - {titulo}")

    def menu_principal(self):
        """
        Menu interativo para processamento de dados musicais.
        """
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Listar Compositores Por Ordem Alfabética")
            print("2. Distribuição de Obras por Período")
            print("3. Listar as obras correspondentes a cada período de forma ordenada")
            print("4. Sair")
            
            try:
                opcao = input("Escolha uma opção: ")
                
                if opcao == '1':
                    self.exibir_compositores()
                elif opcao == '2':
                    self.exibir_distribuicao_periodos()
                elif opcao == '3':
                    self.exibir_obras_por_periodo()
                elif opcao == '4':
                    print("Encerrando o programa...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            
            except Exception as e:
                print(f"Erro: {e}")

def main():
    """
    Função principal para processamento dos dados.
    """
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_do_arquivo>")
        sys.exit(1)
    
    caminho_arquivo = sys.argv[1]
    
    try:
        # Criar processador musical
        processador = ProcessadorMusical(caminho_arquivo)
        
        # Chamar menu principal
        processador.menu_principal()
    
    except FileNotFoundError:
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Uso: python script.py caminho_do_arquivo.txt
if __name__ == "__main__":
    main()