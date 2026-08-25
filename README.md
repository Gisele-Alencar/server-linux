# Linux Server Lab

Este projeto permite praticar comandos Linux para monitoramento e automação.
Nele, um script em Python monitora recursos do sistema e gera registros automaticamente.


**Estrutura**

- `scripts/python/`: scripts de automação em Python.
- `logs/`: relatórios gerados pelos scripts.
- `docs/`: anotações e documentação.

## Como executar

No terminal Ubuntu:

```bash
cd scripts/python
python3 monitor_serv.py
```

**Tecnologias utilizadas**

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
