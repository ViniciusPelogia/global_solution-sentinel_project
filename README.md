# 🛰️ SENTINEL — Sistema Inteligente Integrado da Colônia Marciana

> **Monitoramento • Diagnóstico • Alertas • Previsão • Recomendações**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Leitura%20CSV-purple?style=for-the-badge\&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Gr%C3%A1ficos-orange?style=for-the-badge)
![FIAP](https://img.shields.io/badge/Global%20Solution-FIAP-red?style=for-the-badge)

---

## 🌌 Visão geral

O **SENTINEL** é um sistema inteligente de monitoramento operacional desenvolvido para a **Global Solution FIAP**, com o objetivo de simular o controle básico de uma colônia marciana experimental.

Em uma missão espacial, pequenas falhas podem gerar consequências críticas. Um módulo de comunicação desligado, uma reserva energética zerada, radiação elevada ou consumo maior que a geração podem comprometer a segurança da tripulação e a continuidade da operação.

Pensando nisso, o SENTINEL foi criado como uma central de suporte à decisão capaz de:

* 📡 Ler dados simulados de telemetria;
* ⚡ Analisar geração, consumo e reserva energética;
* 🧠 Identificar falhas operacionais e inconsistências;
* 🚨 Gerar alertas normais e alertas críticos;
* 📜 Registrar logs de eventos do dia;
* 📈 Criar gráficos de análise energética;
* 🔮 Prever a geração de energia do próximo ciclo operacional;
* 🛠️ Gerar recomendações técnicas automáticas;
* 🤖 Disponibilizar um Help Service com IA baseada em regras.

O sistema não apenas mostra dados: ele interpreta, classifica, prioriza e recomenda ações.

---

# 📊 Dados simulados da missão

O arquivo `data/dados.csv` representa um ciclo operacional da colônia ao longo de um dia, com leituras registradas em intervalos de 4 horas.

Cada linha representa uma “fotografia” da situação da missão em determinado horário.

## Exemplo de estrutura do CSV

| horario | geracao_kwh | consumo_kwh | reserva_kwh | temp_interna | radiacao | qualidade_comunicacao | suporte_vida | energia | comunicacao | habitat | laboratorio | armazenamento |
| ------- | ----------: | ----------: | ----------: | -----------: | -------- | --------------------: | -----------: | ------: | ----------: | ------: | ----------: | ------------: |
| 00:00   |          82 |          60 |          78 |           22 | baixa    |                    96 |            1 |       1 |           1 |       1 |           1 |             1 |
| 04:00   |          70 |          64 |         100 |           21 | baixa    |                    92 |            1 |       1 |           1 |       1 |           1 |             1 |
| 08:00   |          58 |          72 |         106 |           23 | media    |                    85 |            1 |       1 |           1 |       1 |           1 |             1 |
| 12:00   |          45 |          86 |          92 |           25 | alta     |                    62 |            1 |       1 |           1 |       1 |           1 |             1 |
| 16:00   |          34 |          91 |          51 |           26 | alta     |                    41 |            1 |       1 |           0 |       1 |           1 |             1 |
| 20:00   |          25 |          98 |           0 |           28 | alta     |                    28 |            1 |       1 |           0 |       1 |           0 |             1 |
| 24:00   |          18 |          82 |           0 |           27 | media    |                    55 |            1 |       1 |           1 |       1 |           0 |             1 |

---

## 🧾 Explicação das colunas

| Coluna                  | Significado                                   |
| ----------------------- | --------------------------------------------- |
| `horario`               | Horário operacional da leitura                |
| `geracao_kwh`           | Energia gerada no ciclo, em kWh               |
| `consumo_kwh`           | Energia consumida no ciclo, em kWh            |
| `reserva_kwh`           | Energia armazenada/reserva disponível, em kWh |
| `temp_interna`          | Temperatura interna da colônia                |
| `radiacao`              | Nível de radiação detectado                   |
| `qualidade_comunicacao` | Qualidade do sinal de comunicação             |
| `suporte_vida`          | Estado do módulo de suporte à vida            |
| `energia`               | Estado do módulo energético                   |
| `comunicacao`           | Estado do módulo de comunicação               |
| `habitat`               | Estado do habitat                             |
| `laboratorio`           | Estado do laboratório                         |
| `armazenamento`         | Estado do armazenamento                       |

---

## 🔢 Estados binários dos módulos

Os módulos críticos são representados por valores binários:

| Valor | Significado                          |
| ----: | ------------------------------------ |
|   `1` | Módulo ligado / funcionando          |
|   `0` | Módulo desligado / falha operacional |

Caso algum módulo apresente valor diferente de `0` ou `1`, o SENTINEL interpreta isso como **inconsistência nos dados**, pois o sensor deveria retornar apenas estados binários válidos.

Exemplo:

```csv
energia = 3
```

Esse valor seria considerado inválido, pois o módulo energético só deveria estar ligado (`1`) ou desligado (`0`).

---

# 🚀 Proposta do sistema

O SENTINEL foi projetado como uma central inteligente para apoiar decisões em uma colônia marciana.

A ideia é simular uma situação em que a equipe da missão coleta dados de telemetria durante o dia e, ao final do ciclo operacional, executa o sistema para responder perguntas essenciais:

* A colônia está segura?
* Houve falha em algum módulo crítico?
* O consumo superou a geração?
* A reserva energética chegou a níveis perigosos?
* A radiação ficou elevada?
* Existe risco para o próximo ciclo?
* Quais ações devem ser tomadas?

A resposta do sistema é entregue por meio de:

* Alertas;
* Logs;
* Gráficos;
* Previsões;
* Recomendações técnicas.

---

# 🧠 Como o SENTINEL funciona

Fluxo geral do sistema:

```text
CSV de telemetria
        ↓
Leitura dos dados
        ↓
Verificação de módulos
        ↓
Análise energética
        ↓
Geração de alertas
        ↓
Registro de logs
        ↓
Previsão do próximo ciclo
        ↓
Recomendações técnicas
        ↓
Apoio à decisão da missão
```

---

# 📁 Estrutura do projeto

```text
GlobalSolution/
│
├── data/
│   ├── dados.csv
│   └── filas.py
│
├── docs/
│   ├── relatorio.pdf
│   ├── link_video.txt
│   └── uso_ia.md
│
├── src/
│   ├── sistema.py
│   ├── analise_modulos.py
│   ├── analise_energetica.py
│   └── respostas.py
│
├── README.md
└── requirements.txt
```

---

## 📌 Função de cada arquivo

| Arquivo                     | Responsabilidade                                                                 |
| --------------------------- | -------------------------------------------------------------------------------- |
| `src/sistema.py`            | Arquivo principal. Exibe o menu, carrega os dados e controla o fluxo do programa |
| `src/analise_modulos.py`    | Verifica módulos, falhas, inconsistências e cria diagnóstico do dia              |
| `src/analise_energetica.py` | Analisa geração/consumo, cria gráficos e calcula previsão por regressão linear   |
| `src/respostas.py`          | Gera alertas, logs, recomendações, animações de terminal e Help Service          |
| `data/filas.py`             | Armazena filas de alertas, alertas críticos e logs                               |
| `data/dados.csv`            | Base simulada de telemetria da missão                                            |
| `docs/relatorio.pdf`        | Relatório explicativo do projeto                                                 |
| `docs/link_video.txt`       | Link do vídeo de apresentação                                                    |
| `docs/uso_ia.md`            | Registro opcional do uso de IA no desenvolvimento                                |

---

# 🖥️ Menu principal

Ao executar o sistema, o usuário acessa um menu interativo em terminal:

```text
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
```

Menu:

```text
[1] 📊 Análise diária da colônia
[2] 📜 Logs do dia
[3] 🤖 Help Service com IA
[0] ❌ Encerrar sistema
```

---

# ⚙️ Funcionalidades principais

## 1. 📊 Análise diária da colônia

Executa a rotina principal do SENTINEL.

Nesta opção, o sistema:

* Coleta os dados da telemetria;
* Analisa os módulos críticos;
* Verifica inconsistências;
* Analisa geração e consumo energético;
* Gera gráficos;
* Mostra alertas;
* Calcula previsão do próximo ciclo;
* Gera recomendações técnicas.

---

## 2. 📜 Logs do dia

Exibe os eventos registrados durante a análise.

Exemplos de logs:

```text
08:00 - Consumo maior que geração detectado
16:00 - Módulo de comunicação desligado
20:00 - Reserva energética chegou a 0 kWh
20:00 - Módulo de laboratório desligado
```

Os logs funcionam como um diário de bordo da missão.

---

## 3. 🤖 Help Service com IA

O SENTINEL possui um assistente simples baseado em regras e palavras-chave.

Ele responde perguntas como:

```text
O que é o SENTINEL?
Quem são os participantes?
O que é Global Solution?
Qual o RM da equipe?
O que o projeto faz?
```

Essa funcionalidade simula um assistente inteligente de suporte operacional, usando uma pequena base de conhecimento interna.

---

## 0. ❌ Encerrar sistema

Finaliza a execução:

```text
🛰️ Encerrando SENTINEL.
Até o próximo ciclo operacional.
```

---

# 🧱 Estruturas de dados utilizadas

## Listas

Usadas para armazenar séries temporais, como:

```python
geracao = dados["geracao_kwh"].tolist()
consumo = dados["consumo_kwh"].tolist()
```

Também são utilizadas para:

* Recomendações;
* Módulos críticos;
* Módulos desligados;
* Valores de regressão linear;
* Dados do eixo X dos gráficos.

---

## Dicionários

Utilizados no diagnóstico do dia:

```python
diagnostico = {
    "consumo_maior_geracao": 0,
    "radiacao_alta": 0,
    "comunicacao_falhou": False,
    "suporte_vida_falhou": False,
    "reserva_zerada": False,
    "modulos_desligados": []
}
```

Esse dicionário funciona como um resumo inteligente do estado da missão.

---

## Filas

O projeto utiliza `deque`, da biblioteca `collections`, para organizar alertas.

```python
fila_criticos = deque()
fila_alertas = deque()
```

As filas permitem armazenar alertas em ordem de chegada e depois exibi-los de forma organizada.

O sistema separa:

* Alertas críticos;
* Alertas normais.

Isso permite priorizar problemas mais graves primeiro.

---

## Logs

Os logs são armazenados em uma lista:

```python
log_eventos = []
```

Eles registram eventos importantes ocorridos durante o dia, como falhas, consumo elevado ou reserva energética zerada.

---

# 🚨 Classificação dos alertas

O SENTINEL trabalha com dois níveis principais de alerta:

## ALERTA

Indica uma situação que exige atenção, mas não compromete imediatamente a sobrevivência da missão.

Exemplos:

* Consumo maior que geração;
* Laboratório desligado;
* Armazenamento desligado;
* Queda de desempenho energético.

---

## ALERTA CRÍTICO

Indica uma condição perigosa ou potencialmente fatal para a missão.

Exemplos:

* Suporte à vida desligado;
* Comunicação inoperante;
* Habitat desligado;
* Reserva energética zerada;
* Valor inconsistente em módulo binário;
* Falha em módulo essencial.

---

# 🧠 Regras lógicas principais

O sistema utiliza regras com `if`, `elif`, `else` e operadores lógicos para interpretar a missão.

## Regra 1 — Consumo maior que geração

```python
if consumo_kwh > geracao_kwh:
    gerar_alerta("Consumo maior que geração")
```

Interpretação:

Se a colônia está consumindo mais energia do que produz, há risco de esgotamento da reserva energética.

---

## Regra 2 — Reserva zerada

```python
if reserva_kwh <= 0:
    gerar_alerta_critico("Reserva energética zerada")
```

Interpretação:

Se a reserva chega a zero, o sistema entra em condição crítica, pois a colônia passa a depender apenas da geração imediata.

---

## Regra 3 — Módulo binário inválido

```python
if valor not in [0, 1]:
    gerar_alerta_critico("Valor inconsistente detectado")
```

Interpretação:

Módulos binários só podem assumir `0` ou `1`. Qualquer valor diferente indica possível falha de sensor, erro de leitura ou dado corrompido.

---

## Regra 4 — Módulo crítico desligado

```python
if modulo in modulos_criticos and valor == 0:
    gerar_alerta_critico("Módulo crítico desligado")
```

Interpretação:

Suporte à vida, energia, comunicação e habitat são essenciais. Se algum deles falhar, a missão pode entrar em risco imediato.

---

## Regra 5 — Radiação elevada

```python
if radiacao == "alta":
    diagnostico["radiacao_alta"] += 1
```

Interpretação:

Quando a radiação permanece alta em vários horários, o sistema recomenda manter a tripulação em áreas protegidas.

---

# 🧮 Expressão booleana principal do diagnóstico

A lógica central do SENTINEL pode ser resumida pela seguinte expressão:

```python
situacao_critica = (
    suporte_vida == 0
    or energia == 0
    or comunicacao == 0
    or habitat == 0
    or reserva_kwh <= 0
    or radiacao == "alta"
)
```

Em linguagem simples:

> A missão entra em estado crítico se um módulo essencial falhar, se a reserva energética zerar ou se a radiação atingir nível elevado.

---

# ⚡ Análise energética

O sistema compara a geração e o consumo de energia em cada horário operacional.

Exemplo:

```text
16:00
Geração: 34 kWh
Consumo: 91 kWh
```

Como o consumo é maior que a geração, o sistema registra:

```text
16:00 - ALERTA: consumo maior que geração
```

Essa análise permite identificar horários de sobrecarga e risco energético.

---

# 📈 Gráfico de geração x consumo

O SENTINEL gera um gráfico comparando a produção e o consumo da colônia ao longo do dia.

O gráfico apresenta:

* Linha de geração energética;
* Linha de consumo energético;
* Pontos destacados;
* Valores anotados;
* Eixo X ajustado em intervalos de 4 horas;
* Título e subtítulo explicativos.

Objetivo:

> Permitir uma visualização rápida dos momentos em que o consumo ultrapassa a geração.

---

# 🔮 Previsão do próximo ciclo operacional

O SENTINEL aplica uma regressão linear simples para prever a geração energética do próximo ciclo.

A previsão é calculada manualmente, sem uso de bibliotecas avançadas de machine learning.

## Fórmula utilizada

A reta da regressão é dada por:

```text
y = ax + b
```

Onde:

| Símbolo | Significado         |
| ------- | ------------------- |
| `x`     | Horário operacional |
| `y`     | Geração de energia  |
| `a`     | Inclinação da reta  |
| `b`     | Intercepto          |

O coeficiente angular é calculado por:

```text
a = Σ((xi - média_x) * (yi - média_y)) / Σ((xi - média_x)²)
```

O intercepto é calculado por:

```text
b = média_y - a * média_x
```

Com isso, o sistema projeta a geração do próximo ciclo:

```python
previsao = a * proximo_ciclo + b
```

---

## Por que prever o próximo ciclo?

A colônia funciona em ciclos de 4 horas.

Se o CSV possui dados até `24:00`, o próximo ciclo será:

```text
28h = D+1 04:00
```

Isso significa que o sistema analisa o dia completo e estima a geração do primeiro ciclo do dia seguinte.

---

# 🛠️ Recomendações técnicas

Após gerar o diagnóstico e calcular a previsão, o SENTINEL recomenda ações práticas.

Exemplos:

```text
- Ativar modo economia e desligar módulos não essenciais.
- Reduzir consumo energético. O consumo superou a geração em vários horários.
- Manter tripulação em áreas protegidas devido à radiação elevada.
- Acionar canal de comunicação de emergência.
- Previsão energética baixa: priorizar suporte à vida e recarga das baterias.
- Verificar módulo laboratório, pois apresentou desligamento durante o ciclo.
```

Essas recomendações não são fixas: elas dependem do diagnóstico calculado durante a execução.

---

# 🤖 Help Service com IA

O sistema possui uma opção extra no menu:

```text
[3] 🤖 Help Service com IA
```

Essa funcionalidade funciona como um assistente inteligente baseado em regras.

O usuário pode perguntar sobre:

* SENTINEL;
* Projeto;
* Global Solution;
* Equipe;
* RM;
* Email.

Exemplo:

```text
Você: o que é o sentinel?

🤖 O SENTINEL é um sistema inteligente integrado de monitoramento da colônia marciana.
```

Essa funcionalidade simula um suporte interno da missão, capaz de responder dúvidas rápidas sobre o sistema.

---

# 🧪 Exemplo de execução

Ao escolher a opção `1`, o sistema inicia a análise diária:

```text
📡 Coletando dados da telemetria...
[██████████] 100%

⚡ Calculando consumo energético...
[██████████] 100%

🧠 Gerando diagnóstico da colônia...
[██████████] 100%

🚨 Verificando alertas críticos...
[██████████] 100%

✅ Análise concluída.
```

Em seguida, exibe gráficos, alertas, previsão e recomendações.

Exemplo de saída:

```text
===== ALERTAS CRÍTICOS =====
20:00 - ALERTA CRÍTICO: reserva zerada
24:00 - ALERTA CRÍTICO: reserva zerada

===== ALERTAS =====
08:00 - ALERTA: consumo maior que geração
12:00 - ALERTA: consumo maior que geração
16:00 - ALERTA: consumo maior que geração
20:00 - ALERTA: módulo laboratorio desligado
```

Previsão:

```text
Previsão para 28h: 10.25 kWh
```

Recomendações:

```text
===== RECOMENDAÇÕES TÉCNICAS =====
- Ativar modo economia e desligar módulos não essenciais.
- Reduzir consumo energético. O consumo superou a geração em vários horários.
- Manter tripulação em áreas protegidas devido à radiação elevada.
- Acionar canal de comunicação de emergência.
- Previsão energética baixa: priorizar suporte à vida e recarga das baterias.
```

---

# 💻 Como executar o projeto

## 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO_AQUI
```

Entrar na pasta:

```bash
cd GlobalSolution
```

---

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv .venv
```

Ativar:

```bash
.venv\Scripts\activate
```

---

### Linux/Mac

```bash
python3 -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

Caso o `pip` apresente problema, use:

```bash
python -m pip install -r requirements.txt
```

---

## 4. Executar o sistema

Na raiz do projeto:

```bash
python src/sistema.py
```

---

# 📦 Requirements

O arquivo `requirements.txt` deve conter as bibliotecas utilizadas no projeto.

Exemplo:

```text
pandas
matplotlib
```

Para gerar o arquivo automaticamente:

```bash
pip freeze > requirements.txt
```

Ou, se houver problema com o launcher do `pip`:

```bash
python -m pip freeze > requirements.txt
```

---

# 🧭 Como usar o menu

Após executar:

```bash
python src/sistema.py
```

Escolha uma opção:

```text
[1] 📊 Análise diária da colônia
[2] 📜 Logs do dia
[3] 🤖 Help Service com IA
[0] ❌ Encerrar sistema
```

## Opção 1

Executa a análise completa:

```text
1
```

## Opção 2

Exibe os logs registrados:

```text
2
```

## Opção 3

Abre o Help Service:

```text
3
```

## Opção 0

Encerra o sistema:

```text
0
```

---

# 👥 Equipe

| Integrante       | RM       | Email                                                        |
| ---------------- | -------- | ------------------------------------------------------------ |
| Vinicius Pelogia | RM 572675 | [vinipelogia@gmail.com](mailto:vinipelogia@gmail.com)       |
| David Tomaz      | RM 570348 | [daviddesatomaz@gmail.com](mailto:daviddesatomaz@gmail.com) |
| Eric Yuiti       | RM 573495 | [Eric.nissi@gmail.com](mailto:Eric.nissi@gmail.com)         |
| Antuny Menezes   | RM 572107 | [antunyyt@gmail.com](mailto:antunyyt@gmail.com)             |

---

# 🎥 Vídeo de apresentação

Link do vídeo no YouTube:

```text
INSERIR_LINK_DO_VIDEO_AQUI
```

O vídeo deve estar publicado como **não listado**.

---

# 🔗 Repositório

Link do GitHub:

```text
INSERIR_LINK_DO_REPOSITORIO_AQUI
```

---

# 🧠 Uso de Inteligência Artificial

A IA foi utilizada como apoio para:

* Organização de ideias;
* Revisão textual;
* Explicação de conceitos;
* Apoio na estruturação do README;
* Discussão sobre lógica de alertas, previsão e organização do sistema.

A implementação final, validação, testes e adaptação ao contexto da Global Solution foram realizados pela equipe, garantindo entendimento crítico sobre o funcionamento do sistema.

---

# 🌱 Sustentabilidade e segurança operacional

O SENTINEL também se conecta a conceitos de sustentabilidade, pois monitora desperdício energético, identifica consumo excessivo e sugere economia de recursos.

Em uma colônia marciana, energia não é apenas custo: é sobrevivência.

Por isso, o sistema prioriza:

* Suporte à vida;
* Habitat;
* Comunicação;
* Reserva energética;
* Redução de consumo;
* Desligamento de módulos não essenciais.

Essa lógica reflete uma abordagem responsável de uso de recursos limitados em ambientes extremos.

---

# 🏁 Conclusão

O SENTINEL representa uma solução de monitoramento inteligente para uma missão espacial experimental.

O sistema integra conceitos de programação, estruturas de dados, lógica booleana, análise energética, visualização de dados, regressão linear simples e tomada de decisão automatizada.

Mais do que um programa em Python, o SENTINEL funciona como uma central operacional capaz de transformar dados brutos de telemetria em informações úteis para proteger uma colônia marciana.

Em um ambiente onde cada kWh importa, cada módulo é essencial e cada decisão pode afetar a sobrevivência da tripulação, o SENTINEL atua como o vigia digital da missão.

> **SENTINEL — porque em Marte, monitorar é sobreviver.**
