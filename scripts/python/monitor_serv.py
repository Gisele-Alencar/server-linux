import shutil
from pathlib import Path
from datetime import datetime
import platform

# Cria ou usa a pasta onde os relatórios serão guardados
pasta_logs = Path("../../logs")
pasta_logs.mkdir(exist_ok=True)

# Coleta informações do sistema
data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
sistema = platform.system()
versao_sistema = platform.release()

# Consulta o uso do disco principal do Linux
total, usado, livre = shutil.disk_usage("/")

# Converte bytes para gigabytes
total_gb = total / (1024 ** 3)
usado_gb = usado / (1024 ** 3)
livre_gb = livre / (1024 ** 3)

# Calcula a porcentagem usada
percentual_usado = (usado / total) * 100

# Cria um alerta usando uma condicional if/else
if percentual_usado >= 80:
    status = "ALERTA: o disco está acima de 80% de uso!"
else:
    status = "OK: espaço em disco dentro do limite."

# Monta o relatório
relatorio = f"""
==================================
MONITOR DE SAÚDE DO SERVIDOR
==================================
Data e hora: {data_hora}
Sistema: {sistema} {versao_sistema}

--- Disco ---
Total: {total_gb:.2f} GB
Usado: {usado_gb:.2f} GB
Livre: {livre_gb:.2f} GB
Uso: {percentual_usado:.2f}%

Status: {status}
"""

# Mostra o relatório no terminal
print(relatorio)

# Salva o relatório no arquivo de log
arquivo_log = pasta_logs / "monitoramento.log"

with open(arquivo_log, "a", encoding="utf-8") as arquivo:
    arquivo.write(relatorio + "\n")

print("Relatório salvo em logs/monitoramento.log")
