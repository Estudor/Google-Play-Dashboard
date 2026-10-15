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

def montar_tabela(apps):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for app in apps:
        linha = {
            "Título": app["titulo"],
            "Categoria": app["categoria"],
            "Nota": app["nota"] * "⭐",
            "Preço": f"£ {app["preco"]:.2f}"
        }
        tabela.append(linha)
    return tabela

def preparar_apps(linhas):
    """Recebe as linhas lidas do CSV e devolve os livros com preço e nota em número."""
    apps = []
    for linha in linhas:
        app = {
            "titulo": linha["titulo"],
            "categoria": linha["categoria"],
            "url": linha["url"]
        }
        apps.append(app)

def carregar_apps():
    """Lê o CSV e já devolve os livros prontos para usar."""
    return preparar_apps(ler_apps())