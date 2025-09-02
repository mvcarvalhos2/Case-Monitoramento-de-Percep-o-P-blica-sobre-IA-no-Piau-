import re
import pandas as pd

positivas = ["avanço","benefício", "inovação", "oportunidade", "melhoria", "progresso"]
negativas = ["risco", "ameaça", "problema", "desemprego", "preocupação", "crise"]

def limpar_texto(txt):
    return re.sub(r"<.*?>|[^a-zA-ZÀ-ÿ\s]", "", str(txt)).lower()

def classificar_sentimento(txt):
    txt = limpar_texto(txt)
    if any(p in txt for p in positivas):
        return "Positivo"
    
    elif any(n in txt for n in negativas):
        return "Negativo"
    
    return "Neutro"

def processar_dados(caminho="data/noticias.csv"):
    df = pd.read_csv(caminho)
    df["descricao_limpa"] = df["descrição"].apply(limpar_texto)
    df["sentimento"] = df["descricao_limpa"].apply(classificar_sentimento)
    df.to_csv("data/noticias_processadas.csv", index=False)
    return df

if __name__ == "__main__":
    df = processar_dados()
    print(df.head)