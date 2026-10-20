
import streamlit as st
import dados

def busca_com_titulo(apps, busca):
    """Retorna os apps que incluem esse texto no titulo"""
    encontrados = []
    for app in apps:
        if busca.lower().strip() in app["app"].lower().strip():
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

    col1, col2, col3, col4 = st.columns(4)
    qtd_apps = len(apps)
    col1.metric("Total de Apps", qtd_apps)
    
    preco_medio = dados.calcular_preco_medio(apps)
    col2.metric("Preço médio", f"${preco_medio}")
    
    st.dataframe(montar_tabela(apps))
    
     


if __name__ == "__main__":
    main()