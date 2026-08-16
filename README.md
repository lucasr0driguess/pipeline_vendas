# Pipeline de Vendas

Pipeline ETL desenvolvido em Python para extração, transformação e carregamento de dados de vendas em um banco de dados PostgreSQL.

O projeto tem como objetivo praticar conceitos de Engenharia de Dados, como ETL, tratamento de dados com Pandas, conexão com bancos de dados, SQLAlchemy e modelagem de dados.

## Arquitetura

```text
CSV
 ↓
Extract
 ↓
DataFrames
 ↓
Transformation
 ↓
DataFrames tratados
 ↓
Load
 ↓
PostgreSQL
```

## Tecnologias

* Python
* Pandas
* SQLAlchemy
* PostgreSQL
* SQL

## Estrutura do projeto

```text
pipeline-vendas/
│
├── data/
│   ├── clientes.csv
│   ├── produtos.csv
│   └── vendas.csv
│
├── sql/
│   └── create_tables.sql
│
└── src/
    └── pipeline_vendas/
        ├── __init__.py
        ├── config.py
        ├── extraction.py
        ├── transformation.py
        ├── loading.py
        └── main.py
```
