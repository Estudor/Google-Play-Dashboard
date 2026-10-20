
import streamlit as st
import dados

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
    """Retorna apenas os livros da categoria escolhida"""
    if categoria == "Todas":
        return apps

    encontrados = []
    for app in apps:
        if app["categoria"] == categoria:
            encontrados.append(app)

    return encontrados

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

    col_busca, col_categoria = st.columns(2)
    busca = col_busca.text_input("Buscar apps")
    categoria = col_categoria.selectbox("Filtro de categorias", ["Todas"] + pegar_categorias(apps))

    apps_categoria = encontrar_com_categoria(apps, categoria)
    encontrados = busca_com_titulo(apps_categoria, busca)
    st.dataframe(montar_tabela(encontrados))
    
     


if __name__ == "__main__":
    main()