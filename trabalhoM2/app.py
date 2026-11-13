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

def listar_titulos(apps):
    titulos = []
    for app in apps:
        titulos.append(app["apps"])
    return titulos

def filtrar_recentes(apps):
    """Retorna apenas os apps atualizados dentro de um período de 1 mês da data_at"""
    data_at = "July 26, 2018"
    encontrados = []
    for app in apps:
        if timedelta(days=0) <= (dados.converter_data(app["atualizado_em"]) - dados.converter_data(data_at)) <= timedelta(days=30):
           encontrados.append(app)
    return(encontrados)

def somar_favoritos(favoritos):
    total = 0

    for favorito in favoritos.values():
        total += favorito["preco"]

    return total

def montar_tabela(apps, lista_tamanho):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for app in apps:
        if app["tamanho"] != "Varies with device":
            if lista_tamanho[app["apps"]] == "M":
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
            elif lista_tamanho[app["apps"]] == "k":
                linha = {
                    "Apps": app["apps"],
                    "Categoria": app["categoria"],
                    "Nota": app["nota"],
                    "Avaliações": app["avaliacoes"],
                    "Tamanho": f"{app["tamanho"]}k",
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

def montar_tabela_favoritos(favoritos):
    tabela = []

    for titulo, favorito in favoritos.items():
        linha = {
            "Título": titulo,
            "Preço": f"$ {favorito['preco']}",
            "Nota": favorito["nota"],
            "Gêneros": favorito["generos"],
            "Status": favorito["status"],
            "Comentário": favorito["comentario"]
        }

        tabela.append(linha)

    return tabela

def main():
    st.set_page_config(page_title="Dashboard - Google Play", page_icon="🗂️", layout="wide")
    st.title("🗂️ Dashboard - Google Play")

    aba_catalogo, aba_favoritos = st.tabs(["Catálogo", "Favoritos"])

    apps = dados.carregar_apps()
    def mostrar_catalogo(apps):
        """Mostra o catalogo de apps"""

        col1, col2, col3, col4, col5 = st.columns(5)
        qtd_apps = len(apps)
        col1.metric("Total de Apps", qtd_apps)
        
        preco_medio = dados.calcular_preco_medio(apps)
        col2.metric("Preço médio", f"${preco_medio:.2f}")

        nota_maior_igual_quatro_ponto_cinco = dados.contar_nota_maior_igual_quatro_ponto_cinco(apps)
        col3.metric("Qtd. apps nota >= 4.5", nota_maior_igual_quatro_ponto_cinco)

        mais_instalado = dados.encontrar_mais_instalacao(apps)
        col4.metric("App mais instalado", f"{mais_instalado["instalacoes"]}+")
        col4.caption(mais_instalado["apps"])

        lista_tamanho = dados.criar_lista_tamanho(dados.ler_apps())

        menor_tamanho = dados.encontrar_menor_tamanho(apps, lista_tamanho)
        col5.metric("App de menor tamanho", f"{menor_tamanho["tamanho"]}k")
        col5.caption(menor_tamanho["apps"])

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
            st.dataframe(montar_tabela(encontrados, lista_tamanho))

            titulo = st.selectbox("Escolha um app", listar_titulos(encontrados))
            if st.button("Adicionar aos favoritos"):
                favoritos = dados.carregar_favoritos()
                if titulo in favoritos:
                    st.warning("Esse app já está nos favoritos.")
                else:
                    app_sel = busca_com_titulo(encontrados, titulo)
                    dados.salvar_favorito(app_sel[0])
                    st.success("App adicionado aos favoritos!")

    def mostrar_favoritos():
        """Mostra os favoritos salvos."""
        favoritos = dados.carregar_favoritos()
        if len(favoritos) == 0:
            st.info("Nenhum app marcado como favorito.")
            return
        col1, col2 = st.columns(2)
        col1.metric("Favoritos", len(favoritos))
        col2.metric("Total", f"£ {somar_favoritos(favoritos):.2f}")
        st.dataframe(montar_tabela_favoritos(favoritos), hide_index=True, width="stretch")
        titulo = st.selectbox("Escolha um favorito", list(favoritos.keys()))
        favorito = favoritos[titulo]
    
    with aba_catalogo:
        mostrar_catalogo(apps)
    with aba_favoritos:
        mostrar_favoritos()


if __name__ == "__main__":
    main()
