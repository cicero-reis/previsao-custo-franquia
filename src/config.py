import streamlit as st
from src.css_style import css_style

def config():
    # ===== Tema visual customizado =====
    st.set_page_config(
        page_title="Previsão de Franquia",
        page_icon="💰",
        layout="wide"
    )

    st.markdown(css_style(), unsafe_allow_html=True)

    # ===== Título =====
    st.markdown('<p class="title">📈 Previsão de Custo Inicial para Montar uma Franquia</p>', unsafe_allow_html=True)

    # ===== Modelo CSV de exemplo =====
    exemplo_csv = "FrqAnual;CusInic\n1000;1050\n1125;1150\n1087;1213\n1070;1275\n"
    st.download_button(
        label="📎 Baixar modelo CSV de exemplo",
        data=exemplo_csv,
        file_name="modelo_exemplo.csv",
        mime="text/csv"
    )

    return st