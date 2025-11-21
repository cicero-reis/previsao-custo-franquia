import streamlit as st

total_de_registros = 10

def streamlit_header(dados):
    st.subheader(f"📊 Visualização inicial dos dados (Top {total_de_registros} registros)")
    st.dataframe(dados.head(total_de_registros), use_container_width=True)

    st.subheader("🔎 Realizar Previsão")
    valor = st.number_input(
        "Insira um novo valor (Taxa Anual):",
        min_value=1.0, value=1500.0, step=10.0
    )

    return valor