import time

from data.filas import fila_criticos, fila_alertas, log_eventos
from analise_energetica import previsao_proximo_ciclo, analise_producao
from analise_modulos import analisar_dia, analisar_energia, verificar_modulos

#Enfeitando texto
def carregar(etapa):
    print(f"\n{etapa}")

    for i in range(0, 101, 10):
        print(f"\r[{'█'*(i//10)}{' '*(10-i//10)}] {i}%", end="")
        time.sleep(0.15)

    print()

def digitar(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.03)

    print()

# Alertas e Logs
def gerar_alertas():
    digitar("===== ALERTAS CRÍTICOS =====")

    while fila_criticos:
        digitar(fila_criticos.popleft())
        time.sleep(1)

    time.sleep(1)
    digitar("===== ALERTAS =====")

    while fila_alertas:
        digitar(fila_alertas.popleft())


def imprimir_logs():
    digitar("===== LOG DE EVENTOS =====")
    for evento in log_eventos:
        digitar(evento)


def gerar_recomendacoes(diagnostico, previsao):
    recomendacoes = []

    if diagnostico["suporte_vida_falhou"]:
        recomendacoes.append("Prioridade máxima: restaurar suporte à vida imediatamente.")

    if diagnostico["reserva_zerada"]:
        recomendacoes.append("Ativar modo economia e desligar módulos não essenciais.")

    if diagnostico["consumo_maior_geracao"] >= 3:
        recomendacoes.append("Reduzir consumo energético. O consumo superou a geração em vários horários.")

    if diagnostico["radiacao_alta"] >= 2:
        recomendacoes.append("Manter tripulação em áreas protegidas devido à radiação elevada.")

    if diagnostico["comunicacao_falhou"]:
        recomendacoes.append("Acionar canal de comunicação de emergência.")

    if previsao < 20:
        recomendacoes.append("Previsão energética baixa: priorizar suporte à vida e recarga das baterias.")

    for modulo in diagnostico["modulos_desligados"]:
        recomendacoes.append(f"Verificar módulo {modulo}, pois apresentou desligamento durante o ciclo.")

    if not recomendacoes:
        recomendacoes.append("Sistema estável. Manter monitoramento padrão.")

    return recomendacoes

def help_service():
    print("\n🤖 SENTINEL Help Service")
    print("Pergunte sobre: projeto, equipe, RM, email, SENTINEL ou Global Solution.")
    print("Digite 'sair' para voltar.\n")

    base_conhecimento = {
        "sentinel": "O SENTINEL é um sistema inteligente integrado de monitoramento da colônia marciana.",
        "global solution": "A Global Solution é um projeto integrador da FIAP focado em resolver desafios reais com tecnologia.",
        "projeto": "O projeto analisa telemetria, energia, módulos críticos, logs, alertas, previsão e recomendações.",
        "equipe": "Equipe: Vinicius Pelogia do Nascimento | RM: 572675 | Email: vinipelogia@gmail.com\nDavid de Sá Tomaz | RM: 570348 | Email: daviddesatomaz@gmail.com\nAntuny Marques de Menezes | RM: 572107 | Email: antunyyt@gmail.com\nEric Yuiti Ito Nissi | RM: 573495 | Email: ",
        "rm": "RMs: Vinicius Pelogia - 572675\nAntuny Menezes - 572107\nEric Yuiti - 573495\bDavid Tomaz - 570348",
        "email": "Emails: Vinicius Pelogia - vinipelogia@gmail.com\nDavid Tomaz - daviddesatomaz@gmail.com\nAntuny Menezes - antunyyt@gmail.com\n Eric Yuiti - "
    }

    while True:
        pergunta = input("Você: ").lower()

        if pergunta in ["sair", "voltar", "0"]:
            print("🤖 Retornando ao menu...")
            break

        respondeu = False

        for chave, resposta in base_conhecimento.items():
            if chave in pergunta:
                print(f"\n🤖 {resposta}\n")
                respondeu = True
                break

        if not respondeu:
            print("\n🤖 Não encontrei essa informação. Tente perguntar sobre SENTINEL, projeto, equipe, RM ou Global Solution.\n")

#Execução final
def executar_analise(dados):
    digitar("📡 Coletando dados da telemetria...")
    carregar("")

    digitar("⚡ Calculando consumo energético...")
    carregar("")

    digitar("🧠 Gerando diagnóstico da colônia...")
    carregar("")

    digitar("🚨 Verificando alertas críticos...")
    carregar("")

    digitar("✅ Análise concluída.")

    ##Analise
    verificar_modulos(dados)
    analisar_energia(dados)

    #Geração de gráfico
    digitar("📈 Gerando gráfico...")
    carregar("")
    analise_producao(dados)

    #Alertas e diagnósticos
    digitar("🚨 Imprimindo alertas...")
    gerar_alertas()
    diagnostico = analisar_dia(dados)

    #Análise próximo ciclo
    digitar("🔁 Calculando previsão do primeiro ciclo de amanhã...")
    carregar("")
    previsao = previsao_proximo_ciclo(dados)

    #Recomendações
    digitar("🚨 Imprimindo recomendações...")
    recomendacoes = gerar_recomendacoes(diagnostico, previsao)
    digitar("\n===== RECOMENDAÇÕES TÉCNICAS =====")
    for rec in recomendacoes:
        digitar(f"- {rec}")