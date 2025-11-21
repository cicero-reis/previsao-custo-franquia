import streamlit as st
from sklearn.linear_model import LinearRegression
import pandas as pd
import plotly.graph_objects as go

def linear_regression(dados, valor):
    modelo = LinearRegression()
    X = dados[['FrqAnual']]
    y = dados['CusInic']
    modelo.fit(X, y)

    previsao = modelo.predict(pd.DataFrame({'FrqAnual': [valor]}))[0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dados['FrqAnual'], y=dados['CusInic'],
        mode='markers', name='Dados reais',
        marker=dict(color='#1f77b4', size=12),
        hovertemplate='Taxa Anual: %{x}<br>Custo Inicial: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=dados['FrqAnual'], y=modelo.predict(X),
        mode='lines', name='Linha de ajuste',
        line=dict(color='#ff7f0e', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=[valor], y=[previsao],
        mode='markers+text', name='Nova previsão',
        marker=dict(color='red', size=12),
        text=[f'R$ {previsao:,.2f}'], textposition='top center'
    ))
    fig.add_vline(x=valor, line=dict(color='red', dash='dash'))

    fig.update_layout(
        title="📉 Gráfico com linha de regressão e previsão",
        xaxis_title="Franquia - Taxa Anual",
        yaxis_title="Custo Inicial",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        height=680
    )

    st.plotly_chart(fig, use_container_width=True)

    return previsao