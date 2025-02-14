import sys

def process_command(text, index):
    """Verifica se existe um comando ON/OFF no texto começando no índice dado"""
    if text[index] == 'o':
        if index + 2 < len(text) and text[index:index+2] == "on":
            return "ON", 2
        if index + 3 < len(text) and text[index:index+3] == "off":
            return "OFF", 3
    return None, 0

def process_input(input_source):
    total_sum = 0
    current_number = ""
    is_summing = True
    
    for line in input_source:
        if line.strip() == "":  # Stop on empty line
            break
        i = 0
        while i < len(line):
            # Se estamos no modo de soma, procuramos dígitos
            if is_summing:
                if line[i].isdigit():
                    current_number += line[i]
                    i += 1
                    continue
                
                # Se não é dígito, processamos o número acumulado
                if current_number:
                    total_sum += int(current_number)
                    current_number = ""
            
            # Verificamos comandos independente do estado
            command, skip = process_command(line.lower(), i)
            if command:
                is_summing = (command == "ON")
                i += skip
                continue
            
            # Verificamos se é para mostrar a soma
            if line[i] == '=':
                print(f"Soma = {total_sum}\n")
                is_summing = not is_summing
            
            i += 1
    
    # Processa o último número acumulado
    if current_number:
        total_sum += int(current_number)
    
    print(f"Soma final = {total_sum}\n")

def main():
    escolha = input("Digite '1' para inserir o texto ou '2' para ler de um arquivo: ")
    
    if escolha == '1':
        print("Digite o texto (linha vazia para finalizar):")
        process_input(sys.stdin)
    elif escolha == '2':
        caminho_arquivo = input("Digite o caminho do arquivo: ")
        with open(caminho_arquivo, 'r') as arquivo:
            process_input(arquivo)
    else:
        print("Escolha inválida.")

if __name__ == '__main__':
    main()