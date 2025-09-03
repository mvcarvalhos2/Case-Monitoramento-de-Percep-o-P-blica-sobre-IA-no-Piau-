import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def dashboard() -> None:
    
    st.title("Monitoramento de IA no Piauí 📰🤖")

    #Cria a interface gráfica do monitoramento de notícias.
    st.markdown(
        """
        <style>
        /* Fundo com gradiente */
        .stApp {
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            color: #f5f6fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Títulos */
        h1, h2, h3, h4 {
            color: #f5f6fa;
            text-align: center;
            font-weight: 600;
        }

        /* DataFrame estilizado */
        .stDataFrame {
            border: 1px solid #444;
            border-radius: 12px;
            background-color: #2c2c34;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
        }

        /* Texto da tabela */
        .stDataFrame table {
            color: #f5f6fa;
            font-size: 14px;
        }

        /* Subtítulos */
        .css-10trblm, .css-16idsys, .css-1d391kg {
            color: #f5f6fa !important;
        }

        /* Aviso final */
        .stCaption {
            font-size: 0.9em;
            color: #dcdde1;
            font-style: italic;
        }

        /* Botões (quando usar) */
        button {
            background-color: #353b48 !important;
            color: #f5f6fa !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 8px 16px !important;
        }
        button:hover {
            background-color: #40739e !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

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