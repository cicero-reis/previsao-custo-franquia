import streamlit as st

def streamlit_header(dados):
    st.subheader("📊 Dados (Primeiras linhas)")
    st.dataframe(dados.head(10), use_container_width=True)

    st.subheader("🔎 Realizar Previsão")
    valor = st.number_input(
        "Insira um novo valor (Taxa Anual):",
        min_value=1.0, value=1500.0, step=10.0
    )

    return valor