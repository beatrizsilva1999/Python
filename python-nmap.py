# Importa o módulo nmap para realizar varreduras de rede
import nmap

# Cria uma instância do scanner de portas do nmap
nm = nmap.PortScanner()

# Define o alvo da varredura (IP ou hostname)
target = "45.33.32.156"  # Nota: corrigido para um IP válido; o original estava com um erro

# Define as opções para a varredura
# -sV: Detecta as versões dos serviços em execução
# -sC: Executa os scripts padrão de varredura do nmap
# scan_results: Nome do arquivo para salvar os resultados
options = "-sv -sC -oN scan_results"

# Realiza a varredura no alvo com as opções especificadas
nm.scan(target, arguments=options)

# Itera sobre todos os hosts detectados na varredura
for host in nm.all_hosts():
    # Imprime o endereço IP do host e seu nome de host, se disponível
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    # Imprime o estado do host (ativo ou inativo)
    print("State: %s" % nm[host].state())
    
    # Itera sobre todos os protocolos encontrados no host
    for protocol in nm[host].all_protocols():
        # Imprime o protocolo (por exemplo, 'tcp' ou 'udp')
        print("Protocol: %s" % protocol)
        # Obtém as informações das portas para o protocolo atual
        port_info = nm[host][protocol]
        # Itera sobre as portas e seus estados
        for port, state in port_info.items():
            # Imprime a porta e seu estado (aberta, fechada, etc.)
            print("Port: %s\tState: %s" % (port, state))
