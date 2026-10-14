import csv
from pathlib import Path

PASTA = Path(__file__).parent
CAMINHO_APPS = PASTA / "apps-google-play.csv"
   
def ler_apps():
    """Lê o CSV de apps e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    apps = []
    try:
        with open(CAMINHO_APPS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                apps.append(linha)
    except FileNotFoundError:
        print("O arquivo apps-google-play.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return apps
