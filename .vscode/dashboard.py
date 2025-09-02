import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def dashboard():
    st.title("Monitoramento de IA no Piauí 📰🤖")

    try:
        df = pd.read_csv("data/noticias_processadas.csv")
    except FileNotFoundError:
        st.error("⚠️ Arquivo de dados não encontrado. Execute primeiro o coletor e o processador")
        return
    st.write("Colunas disponíveis no DataFrame:", df.columns.tolist())

#Gráfico de pizza
    st.subheader("Distribuição dos Sentimentos")
    fig, ax = plt.subplots()
    df["sentimento"].value_counts().plot.pie(autopct="%.1f%%", ax = ax)
    st.pyplot(fig)

# Nuvem de palavras
    st.subheader("Nuvem de Palavras")
    text = " ".join(df["descricao_limpa"])
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    st.image(wc.to_array())

# Tabela
    st.subheader("Notícias Coletadas")
    st.dataframe(df[["título", "sentimento", "link"]]) 

# Aviso ético
    st.markdown("---")
    st.caption("⚠️ Esta análise é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.")

if __name__ == "__main__":
    dashboard()