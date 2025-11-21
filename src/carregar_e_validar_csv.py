import os
import pandas as pd
import streamlit as st

def carregar_e_validar_csv(caminho):
    try:
        df = pd.read_csv(caminho, sep=";")

        colunas_esperadas = ["FrqAnual", "CusInic"]
        if list(df.columns) != colunas_esperadas:
            st.error("❌ O arquivo deve conter as colunas: 'FrqAnual' e 'CusInic'")
            st.warning("📎 Baixe o modelo CSV acima para seguir o padrão.")
            os.remove(caminho)
            return None

        if df.empty:
            st.error("❌ O arquivo CSV está vazio.")
            os.remove(caminho)
            return None

        st.success("📊 Arquivo validado com sucesso!")
        return df

    except Exception as e:
        st.error(f"❌ Erro ao ler o CSV: {e}")
        os.remove(caminho)
        return None