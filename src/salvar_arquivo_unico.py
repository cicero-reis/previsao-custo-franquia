import os
import streamlit as st

# ===== Configuração pasta =====
PASTA_CSV = "csv"
NOME_ARQUIVO = "dados_producao.csv"
CAMINHO_COMPLETO = os.path.join(PASTA_CSV, NOME_ARQUIVO)
os.makedirs(PASTA_CSV, exist_ok=True)

def salvar_arquivo_unico(uploaded_file):
    # Remove antigos
    for arquivo in os.listdir(PASTA_CSV):
        if arquivo.endswith(".csv"):
            os.remove(os.path.join(PASTA_CSV, arquivo))

    # Salva novo
    with open(CAMINHO_COMPLETO, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✔️ Novo arquivo carregado com sucesso!")
    return CAMINHO_COMPLETO