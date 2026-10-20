
import streamlit as st
import dados

def montar_tabela(apps):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for app in apps:
        linha = {
            "Título": app["titulo"],
            "Categoria": app["categoria"],
            "Nota": app["nota"] * "⭐",
            "Preço": f"£ {app["preco"]:.2f}",
            
        }
        tabela.append(linha)
    return tabela

def main():
     st.set_page_config(page_title="Dashboard - Google Play", page_icon="📚", layout="wide")
     st.title("📚 Dashboard - Google Play")

     apps = dados.carregar_apps()

     col1, col2, col3, col4 = st.columns(4)
     qtd_apps = len(apps)
     col1.metric("Total de Apps", qtd_apps)

     preco_medio = dados.calcular_preco_medio(apps)
     col2.metric("Preço médio", f"£{preco_medio:.2f}")


if __name__ == "__main__":
    main()
