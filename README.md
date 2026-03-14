# POC ABSA — Aspect-Based Sentiment Analysis

Motor de IA que coleta reviews da Google Play Store e classifica o sentimento por aspecto de produto.

## O que faz

1. Coleta reviews de um app educacional na Google Play Store
2. Classifica cada review em um dos quatro aspectos: Usabilidade, Conteúdo Didático, Performance Técnica ou Engajamento
3. Analisa o sentimento (positivo, negativo ou neutro) com score de confiança
4. Gera um relatório CSV pronto para alimentar dashboards

## Requisitos

- Python 3.10+
- Conexão com internet (para coleta de reviews e download dos modelos na primeira execução)

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```bash
# Executar com o app padrão (Duolingo)
python main.py

# Executar com outro app
python main.py --app-id com.memrise.android.memrisecompanion --output memrise_report
```

O relatório será salvo em `data/output/`.

## Estrutura do projeto

```
src/
  scraper/       # Coleta de reviews da Google Play
  absa/          # Classificacao de aspectos e sentimentos
  pipeline/      # Orquestrador do fluxo completo
  report/        # Geracao do relatorio CSV
config/
  settings.py    # Configuracoes centralizadas
data/
  output/        # Relatorios gerados
```

## Colunas do relatório

| Coluna | Descrição |
|---|---|
| texto_original | Texto do review |
| aspecto_detectado | Aspecto identificado |
| sentimento | positivo, negativo ou neutro |
| confiança_modelo | Score de confiança (0 a 1) |
