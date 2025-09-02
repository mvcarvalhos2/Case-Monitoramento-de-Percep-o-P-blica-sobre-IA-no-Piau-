import requests
import xml.etree.ElementTree as ET
import pandas as pd
import os

def coletar_noticias(query="Inteligência Artificial Piauí", limite=15):
    #Coleta notícias do Google News RSS baseado em uma query.
    #Retorna um DataFrame com título, descrição e link.

    url = f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    r = requests.get(url)
    root = ET.fromstring(r.content)

    items = []
    for item in root.findall(".//item")[:limite]:
        titulo = item.find("title").text
        link = item.find("link").text
        desc = item.find("description").text
        items.append({"título": titulo, "descrição": desc, "link": link})
    
    # Cria a pasta 'data' se não existir
    os.makedirs("data", exist_ok=True)

    # Salva o CSV
    df = pd.DataFrame(items)
    df.to_csv("data/noticias.csv", index=False)
    return df

if __name__ == "__main__":
    df = coletar_noticias()
    print(df.head())

