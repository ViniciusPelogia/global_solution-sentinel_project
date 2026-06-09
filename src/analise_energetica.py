import matplotlib.pyplot as plt

def regressao_linear(x, y):
    media_x = sum(x) / len(x)
    media_y = sum(y) / len(y)

    numerador = 0
    denominador = 0

    for xi, yi in zip(x, y):
        numerador += (xi - media_x) * (yi - media_y)
        denominador += (xi - media_x) ** 2

    a = numerador / denominador
    b = media_y - a * media_x

    return a, b

def analise_producao(dados):
    x = [0, 4, 8, 12, 16, 20, 24]

    geracao = dados["geracao_kwh"].tolist()
    consumo = dados["consumo_kwh"].tolist()

    r = input(
        "📊 Gráfico de geração e consumo - PRONTO\n"
        "Deseja visualizar? (s/n)\n"
    ).lower()

    if r in ["s", "sim"]:

        plt.figure(figsize=(12, 6))

        plt.suptitle(
            "Análise Energética da Colônia Espacial",
            fontsize=16,
            fontweight="bold",
            x=0.125,
            ha="left"
        )
        plt.title(
            "Comparação entre geração e consumo de energia em intervalos de 4 horas",
            fontsize=10,
            loc="left"
        )
        plt.plot(
            x,
            geracao,
            marker="o",
            linewidth=2,
            label="Geração de Energia"
        )
        plt.plot(
            x,
            consumo,
            marker="s",
            linewidth=2,
            label="Consumo de Energia"
        )

        plt.grid(
            linestyle="--",
            alpha=0.5
        )
        plt.xticks(x)
        plt.xlabel("Horário Operacional (h)")
        plt.ylabel("Energia (kWh)")
        plt.legend()
        plt.tight_layout()
        for hora, energia in zip(x, geracao):
            plt.annotate(
                f"{energia}",
                (hora, energia),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center"
            )
        for hora, energia in zip(x, consumo):
            plt.annotate(
                f"{energia}",
                (hora, energia),
                textcoords="offset points",
                xytext=(0, -15),
                ha="center"
            )
            plt.figtext(
                0.99,
                0.01,
                "Sentinel - Monitoramento Energético Diário",
                ha="right",
                fontsize=8
            )
        plt.show()

def previsao_proximo_ciclo(dados):
    y = dados["geracao_kwh"].tolist()

    intervalo = 4
    x = [i * intervalo for i in range(len(y))]

    a, b = regressao_linear(x, y)

    proximo_ciclo = x[-1] + intervalo
    previsao = a * proximo_ciclo + b

    print(f"Previsão para {proximo_ciclo}h: {previsao:.2f} kWh")

    r = input('Deseja obter a visualização em gráfico? (s/n)\n').lower()

    if r == 's' or r == 'sim':
        x_reta = x + [proximo_ciclo]

        y_reta = [
            a * xi + b
            for xi in x_reta
        ]

        plt.suptitle(
            "Previsão Energética do Próximo Ciclo",
            fontsize=16,
            fontweight="bold",
            x=0.125,
            ha="left"
        )
        plt.title(
            "Cálculo de Previsão da Produção de Energia do Ciclo de Amanhã",
            fontsize=10,
            loc="left"
        )
        plt.plot(
            x_reta,
            y_reta,
            linewidth=2.5,
            linestyle="--",
            label="Tendência de geração"
        )
        plt.scatter(x,
                    y,
                    label="Dados reais",
                    s=70)
        plt.scatter(
            proximo_ciclo,
            previsao,
            s=120,
            c="red",
            marker="*",
            label="Próximo ciclo"
        )
        plt.grid(
            linestyle="--",
            alpha=0.5
        )
        for hora, energia in zip(x, y):
            plt.annotate(
                f"{energia}",
                (hora, energia),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center"
            )
        plt.annotate(
            f"{previsao:.1f} kWh",
            (proximo_ciclo, previsao),
            textcoords="offset points",
            xytext=(0, 12),
            ha="center",
            fontweight="bold"
        )
        plt.figtext(
            0.99,
            0.01,
            "Sentinel - Sistema Inteligente de Monitoramento",
            ha="right",
            fontsize=8
        )
        plt.xlabel("Horário Operacional (h)")
        plt.ylabel("Geração de Energia (kWh)")
        plt.xticks(x_reta)
        plt.legend()
        plt.show()

    return previsao
