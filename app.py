import streamlit as st
from src.config import config
from src.salvar_arquivo_unico import salvar_arquivo_unico
from src.carregar_e_validar_csv import carregar_e_validar_csv
from src.streamlit_header import streamlit_header
from src.linear_regression import linear_regression

st = config()

# ===== Upload do arquivo =====
uploaded_file = st.file_uploader("📥 Envie um arquivo CSV com os dados de previsão", type=["csv"])

if uploaded_file:
    caminho = salvar_arquivo_unico(uploaded_file)
    dados = carregar_e_validar_csv(caminho)
else:
    dados = None
    st.info("💡 Aguarde ou envie um arquivo para iniciar as previsões.")

# Continuar somente se dados válidos
if dados is not None:

    col1, col2 = st.columns([1.2, 1.8])

    with col1:
        valor = streamlit_header(dados)

    with col2:
        previsao = linear_regression(dados, valor)

    with col1:
        st.markdown(f"""
        <div class="result-card">
            💰 Previsão de Custo Inicial: <span>R$ {round(previsao, 2):,.2f}</span>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("📌 Envie um CSV válido para continuar.")
