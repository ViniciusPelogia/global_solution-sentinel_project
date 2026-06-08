import pandas as pd
import time


from respostas import imprimir_logs, executar_analise, help_service
from src.analise_modulos import analisar_energia, verificar_modulos, analisar_dia


def carregar_dados():
    dados = pd.read_csv("../data/dados.csv")
    return dados


def mostrar_menu():
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗        ║
║   ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║        ║
║   ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║        ║
║   ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║        ║
║   ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗   ║
║   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝   ║
║                                                                      ║
║      Sistema Inteligente Integrado da Colônia Marciana               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)

    time.sleep(1)
    print("""

                 🚀 GLOBAL SOLUTION - FIAP 🚀

Desenvolvido por:
• Vinicius Pelogia
• David Tomaz
• Eric Yuiti
• Antuny Menezes
    """)
    time.sleep(2)
    print("""
──────────────────────────────────────────────────────────────────────
╔══════════════════════════════════════════════════════════════════════╗
║ STATUS: ONLINE                                                       ║
║ TELEMETRIA: CONECTADA                                                ║
║ ALERTAS: MONITORADOS                                                 ║
║ PREVISÕES: DISPONÍVEIS                                               ║
╚══════════════════════════════════════════════════════════════════════╝


[1] 📊 Análise diária da colônia
[2] 📜 Logs do dia
[3] 🤖 Help Service com IA
[0] ❌ Encerrar sistema

    """)

def main():
    while True:

        dados = carregar_dados()
        mostrar_menu()
        opcao = input("▶ Escolha uma opção: ")
        if opcao == "1":
            executar_analise(dados)
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "2":
            verificar_modulos(dados)
            analisar_dia(dados)
            analisar_energia(dados)
            imprimir_logs()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "3":
            help_service()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "0":
            print("\n🛰️ Encerrando SENTINEL...")
            print("Até o próximo ciclo operacional.\n")
            break

        else:
            print("\n⚠️ Opção inválida!\n")



if __name__ == "__main__":
    main()