from data.filas import fila_criticos, fila_alertas, log_eventos

def verificar_modulos(dados):
    colunas = [
        'suporte_vida',
        'energia',
        'comunicacao',
        'habitat',
        'laboratorio',
        'armazenamento'
    ]
    modulos_criticos = [
        'suporte_vida',
        'energia',
        'comunicacao',
        'habitat'
    ]

    for _, valor in dados.iterrows() :
        for coluna in colunas:
            #verifica valores inconsistentes
            if valor[coluna] not in [0, 1]:
                fila_criticos.append(
                    f"{valor['horario']} - ALERTA CRÍTICO: módulo {coluna} contém valor inconsistente"
                )
                log_eventos.append(f"{valor['horario']} - Valor inconsistente encontrado")

            #encontra modulos desligados
            if valor[coluna] == 0:
                if valor[coluna] in modulos_criticos:
                    fila_criticos.append(
                        f"{valor['horario']} - ALERTA CRÍTICO: módulo {coluna} desligado"
                    )
                else:
                    fila_alertas.append(f"{valor['horario']} - ALERTA: módulo {coluna} desligado")
                    log_eventos.append(f"{valor['horario']} - Modulo de {coluna} desligado")

def analisar_dia(dados):
    diagnostico = {
        "consumo_maior_geracao": 0,
        "radiacao_alta": 0,
        "comunicacao_falhou": False,
        "suporte_vida_falhou": False,
        "reserva_zerada": False,
        "modulos_desligados": []
    }

    for _, linha in dados.iterrows():
        if linha["consumo_kwh"] > linha["geracao_kwh"]:
            diagnostico["consumo_maior_geracao"] += 1

        if linha["radiacao"] == "alta":
            diagnostico["radiacao_alta"] += 1

        if linha["comunicacao"] == 0:
            diagnostico["comunicacao_falhou"] = True

        if linha["suporte_vida"] == 0:
            diagnostico["suporte_vida_falhou"] = True

        if linha["reserva_kwh"] <= 0:
            diagnostico["reserva_zerada"] = True

        for modulo in ["laboratorio", "armazenamento", "habitat"]:
            if linha[modulo] == 0 and modulo not in diagnostico["modulos_desligados"]:
                diagnostico["modulos_desligados"].append(modulo)

    return diagnostico

def analisar_energia(dados):
    #Calculo da reserva e energia
    reserva_total = 0
    hora = ''
    for _, e in dados.iterrows():
        hora = e['horario']
        if e["consumo_kwh"] > e["geracao_kwh"]:
            fila_alertas.append(f"{hora} - ALERTA: consumo maior que geração")
            log_eventos.append(f"{hora} - Consumo maior que geração detectado")

        if e["reserva_kwh"] <= 0:
            fila_criticos.append(f"{hora} - ALERTA CRÍTICO: reserva zerada")
            log_eventos.append(f"{hora} - Reserva energética chegou a 0 kWh")
