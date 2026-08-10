# CEASA/SC - Previsão de Sazonalidade de Preços

Sistema de Machine Learning para analisar o histórico de preços diários de alimentos comercializados no CEASA/SC (Santa Catarina) e identificar a melhor época do ano para cada produto, cruzando os dados com variáveis climáticas (temperatura, precipitação) para indicar se o preço atual está bom ou não.

## Objetivo

- Consolidar 5 anos de boletins diários de cotação de preços do CEASA/SC.
- Identificar padrões de sazonalidade por produto (em qual época cada alimento costuma ficar mais barato).
- Cruzar os preços com dados climáticos históricos da região.
- Treinar modelos que apontem se o preço atual de um produto está dentro do esperado, acima ou abaixo, dado o contexto sazonal e climático.
- Evoluir para um sistema (API + interface) que outras pessoas possam consultar.

## Fonte dos dados

Boletins diários publicados publicamente pelo [CEASA/SC](https://www.ceasa.sc.gov.br/index.php/cotacao-de-precos) em formato PDF, um arquivo por dia útil, organizados por ano e mês.

## Status do projeto

🚧 Em desenvolvimento — fase de coleta e estruturação dos dados.

## Roadmap

- [x] Mapear estrutura do site e criar scraper de download dos PDFs
- [x] Testar extração de texto/tabela dos boletins
- [ ] Consolidar os PDFs em uma base única (data, produto, unidade, preço mín/méd/máx)
- [ ] Padronizar nomenclatura de produtos
- [ ] Coletar dados climáticos históricos (Open-Meteo / INMET) para a região da Grande Florianópolis
- [ ] Análise exploratória de sazonalidade por produto
- [ ] Modelo de sazonalidade (Prophet / SARIMAX)
- [ ] Modelo de ajuste climático (XGBoost/LightGBM) para score de "preço bom ou não"
- [ ] API de consulta (FastAPI)
- [ ] Pipeline de atualização e retreino automático
- [ ] Interface para consulta pública

## Estrutura do repositório

```
.
├── scripts/
│   ├── download_ceasa.py        # Scraper: baixa todos os boletins PDF do CEASA/SC
│   └── testar_extracao_pdf.py   # Script auxiliar para testar extração de um PDF
├── raw_pdfs/                    # PDFs baixados (não versionar - ver .gitignore)
├── data/                        # Bases processadas (csv/parquet)
└── README.md
```

## Como rodar

### Pré-requisitos

```bash
pip install requests beautifulsoup4 pdfplumber
```

### 1. Baixar os boletins históricos

```bash
python scripts/download_ceasa.py
```

Para baixar apenas anos específicos:

```bash
python scripts/download_ceasa.py --anos 2023 2024 2025
```

Os arquivos são salvos em `raw_pdfs/{ano}/{mes}/{dd-mm-aaaa}.pdf`. O script pode ser interrompido e retomado sem perder progresso — arquivos já baixados são pulados.

### 2. Testar extração de um PDF

```bash
python scripts/testar_extracao_pdf.py raw_pdfs/2025/07/31-07-2025.pdf
```

## Tecnologias

- Python (requests, BeautifulSoup, pdfplumber)
- pandas para consolidação e limpeza dos dados
- Prophet / SARIMAX para modelagem de sazonalidade
- XGBoost / LightGBM para ajuste com variáveis climáticas
- Open-Meteo / INMET para dados climáticos históricos


## Aviso

Os dados de origem são públicos, disponibilizados pelo CEASA/SC. Este projeto não possui vínculo oficial com a instituição.
