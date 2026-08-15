# Linux Server Lab

Projeto prático de fundamentos Linux, Git e automação para Cloud/DevOps.

## Objetivo

Aprender a operar e monitorar um servidor Linux localmente antes de aplicar os mesmos conceitos em uma instância EC2 na AWS.

## Estrutura

- `scripts/bash/`: scripts de automação Bash.
- `scripts/python/`: scripts de automação em Python.
- `logs/`: relatórios gerados pelos scripts.
- `docs/`: anotações e documentação.

## Como executar

No terminal Ubuntu:

```bash
cd scripts/python
python3 monitor_serv.py

## Tecnologias utilizadas

- Python 3
- Linux Ubuntu (WSL)
- Git e GitHub

## Estrutura do projeto

```text
linux-lab/
├── scripts/
│   └── python/
│       └── monitor_serv.py
├── logs/
├── docs/
├── .gitignore
└── README.md
