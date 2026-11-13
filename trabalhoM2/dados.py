import csv
from pathlib import Path
from datetime import datetime

PASTA = Path(__file__).parent
CAMINHO_APPS = PASTA / "apps-google-play.csv"
CAMPOS_FAVORITO = ["titulo", "preco", "nota", "generos", "status", "comentario"]
CAMINHO_FAVORITOS = PASTA / "apps-favoritos.csv"

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

def calcular_preco_medio(apps):
    """Soma os preços de todos os apps e divide pelo total."""
    soma: float = 0
    for app in apps:
        soma += app["preco"]
    preco_medio: float = soma / len(apps)
    return preco_medio

def contar_nota_maior_igual_quatro_ponto_cinco(apps):
    """Conta quantos apps têm a nota 4.5 <="""
    contador: int = 0
    for app in apps:
        if app["nota"] >= 4.5:
            contador += 1

    return contador

def encontrar_mais_instalacao(apps):
    """Encontra e devolve o app de maior instalação."""
    mais_instalacao = apps[0]
    for app in apps:
        if app["instalacoes"] > mais_instalacao["instalacoes"]:
            mais_instalacao = app
    return mais_instalacao

def encontrar_menor_tamanho(apps, lista_tamanho):
    """Encontra e devolve o app de menor tamanho."""
    menos_tamanho = apps[0]
    for app in apps:
        if app["tamanho"] == "Varies with device":
            continue
        if lista_tamanho[app["apps"]] == "M":
            app["tamanho"] *= 1024
        if app["tamanho"] < menos_tamanho["tamanho"]:
            menos_tamanho = app
        if lista_tamanho[app["apps"]] == "M":
            app["tamanho"] /= 1024
    return menos_tamanho

def criar_lista_tamanho(apps):
    """Cria uma lista de tamanho dos apps.

    Se o tamanho tem megabytes adiciona na lista o nome do app e caracter de 'M',
    senão adiciona caracter de 'k' (kilobytes).
    """
    lista_tamanho = {}
    for app in apps:
        if app["tamanho"] != "Varies with device":
            if "M" in app["tamanho"]:
                lista_tamanho[app["app"]] = "M"
            elif "k" in app["tamanho"]:
                lista_tamanho[app["app"]] = "k"
        else:
            lista_tamanho[app["app"]] = "Varies with device"
    return lista_tamanho   

def converter_data(data):
    """Converte a data de atualização em uma date"""
    data_t = datetime.strptime(data, "%B %d, %Y").date()
    return data_t


def converter_instalacao(instalacao):
    """Converte as instalacao para número inteiro"""
    tabela = str.maketrans({
        ',': '',
        '+': ''
    })
    num_instalacao = instalacao.translate(tabela)
    return int(num_instalacao)

def converter_nota(nota):
    """Converte a nota para o tipo float"""
    return float(nota)

def converter_avaliacao(avaliacao):
    """Converte as avaliacoes para o tipo inteiro"""
    return int(avaliacao)

def converter_tamanho(tamanho):
    """Converte o tamanho para o tipo float se não é 'Varies with device'"""
    if tamanho != "Varies with device":
        return float(tamanho.replace("M", "").replace("k", ""))
    return tamanho

def converter_preco(preco):
    """Converte o preco para o tipo float"""
    return float(preco.replace("$", ""))

def preparar_apps(linhas):
    """Recebe as linhas lidas do CSV e devolve os apps com preço e nota em número."""
    apps = []
    for linha in linhas:
        app = {
            "apps": linha["app"],
            "categoria": linha["categoria"],
            "nota": converter_nota(linha["nota"]),
            "avaliacoes": converter_avaliacao(linha["avaliacoes"]),
            "tamanho": converter_tamanho(linha["tamanho"]),
            "instalacoes": converter_instalacao(linha["instalacoes"]),
            "tipo": linha["tipo"],
            "preco": converter_preco(linha["preco"]),
            "classificacao": linha["classificacao"],
            "generos": linha["generos"],
            "atualizado_em": linha["atualizado_em"]
        }
        apps.append(app)
    return apps

def carregar_apps():
        """Lê o CSV e já devolve os apps prontos para usar."""
        return preparar_apps(ler_apps())

def salvar_favorito(app):
    """Acrescenta um app no fim do arquivo de favoritos (modo "a")."""
    arquivo_ja_existia = CAMINHO_FAVORITOS.exists()
    with open(CAMINHO_FAVORITOS, "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_FAVORITO)
        if not arquivo_ja_existia:
            escritor.writeheader()
        escritor.writerow({
            "titulo": app["apps"],
            "preco": app["preco"],
            "nota": app["nota"],
            "generos": app["generos"],
            "status": "Quero jogar",
            "comentario": "",
        })


def carregar_favoritos():
    """Lê os favoritos e devolve um dicionário: {titulo: dados do favorito}."""
    favoritos = {}
    try:
        with open(CAMINHO_FAVORITOS, encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                favoritos[linha["titulo"]] = {
                    "preco": float(linha["preco"]),
                    "nota": linha["nota"],
                    "generos": linha["generos"],
                    "status": linha["status"],
                    "comentario": linha["comentario"],
                }
    except FileNotFoundError:
        pass
    return favoritos


if __name__ == "__main__":
    apps = ler_apps()
    print("Qtde", len(apps))
    print(type(apps[0]["nota"]))