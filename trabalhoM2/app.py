
import streamlit as st
import dados
from datetime import timedelta

def busca_com_titulo(apps, busca):
    """Retorna os apps que incluem esse texto no titulo"""
    encontrados = []
    for app in apps:
        if busca.lower().strip() in app["apps"].lower().strip():
            encontrados.append(app)

    return encontrados

def pegar_categorias(apps):
    """Retorna as categorias dos apps, sem repetidos (ordem alfabética)"""
    categorias = []
    for app in apps:
        if app["categoria"] not in categorias:
            categorias.append(app["categoria"])

    categorias.sort()
    return categorias

def encontrar_com_categoria(apps, categoria):
    """Retorna apenas os apps da categoria escolhida"""
    if categoria == "Todas":
        return apps

    encontrados = []
    for app in apps:
        if app["categoria"] == categoria:
            encontrados.append(app)

    return encontrados


def filtrar_recentes(apps):
    """Retorna apenas os apps atualizados dentro de um período de 1 mês da data_at"""
    data_at = "July 26, 2018"
    encontrados = []
    for app in apps:
        if timedelta(days=0) <= (dados.converter_data(app["atualizado_em"]) - dados.converter_data(data_at)) <= timedelta(days=30):
           encontrados.append(app)
    return(encontrados)


def montar_tabela(apps):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for app in apps:
        if app["tamanho"] != "Varies with device":
            linha = {
                "Apps": app["apps"],
                "Categoria": app["categoria"],
                "Nota": app["nota"],
                "Avaliações": app["avaliacoes"],
                "Tamanho": f"{app["tamanho"]}M",
                "Instalações": f"{app["instalacoes"]}+",
                "Tipo": app["tipo"],
                "Preço": f"$ {app["preco"]}",
                "Classificação": app["classificacao"],
                "Gêneros": app["generos"],
                "Atualizado em": app["atualizado_em"]
            }
        else:
            linha = {
                "Apps": app["apps"],
                "Categoria": app["categoria"],
                "Nota": app["nota"],
                "Avaliações": app["avaliacoes"],
                "Tamanho": app["tamanho"],
                "Instalações": f"{app["instalacoes"]}+",
                "Tipo": app["tipo"],
                "Preço": f"$ {app["preco"]}",
                "Classificação": app["classificacao"],
                "Gêneros": app["generos"],
                "Atualizado em": app["atualizado_em"]
            }
        tabela.append(linha)
    return tabela

def main():
    st.set_page_config(page_title="Dashboard - Google Play", page_icon="🗂️", layout="wide")
    st.title("🗂️ Dashboard - Google Play")

    apps = dados.carregar_apps()

    col1, col2 = st.columns(2)
    qtd_apps = len(apps)
    col1.metric("Total de Apps", qtd_apps)
    
    preco_medio = dados.calcular_preco_medio(apps)
    col2.metric("Preço médio", f"${preco_medio}")

    col_busca, col_categoria, col_recente = st.columns(3)
    busca = col_busca.text_input("Buscar apps")
    categoria = col_categoria.selectbox("Filtro de categorias", ["Todas"] + pegar_categorias(apps))
    recentes = col_recente.checkbox("Filtro recente atualizados")

    apps_categoria = encontrar_com_categoria(apps, categoria)
    encontrados = busca_com_titulo(apps_categoria, busca)
    if recentes:
           encontrados = filtrar_recentes(encontrados)
    
    if (len(encontrados) == 0):
        st.warning("App não encontrado.")
    else:
        st.write("Apps encontrados", len(encontrados))    
        st.dataframe(montar_tabela(encontrados))
    
     


if __name__ == "__main__":
    main()