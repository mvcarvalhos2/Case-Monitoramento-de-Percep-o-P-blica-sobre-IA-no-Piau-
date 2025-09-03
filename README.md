# Monitoramento de Notícias sobre IA no Piauí

Este projeto coleta notícias relacionadas à Inteligência Artificial no Piauí, processa o texto para identificar sentimentos e exibe os resultados em um dashboard interativo feito com Streamlit.

---

## Estrutura do Projeto

coleta.py # Coleta notícias via RSS do Google News
processo.py # Processa descrições e classifica sentimentos
dashboard.py # Dashboard interativo com Streamlit
requirements.txt # Dependências do projeto
data/ # Pasta onde os CSVs serão salvos

---

## Instalação

Clone este repositório e instale as dependências:

```bash
git clone https://github.com/mvcarvalhos2/Case-Monitoramento-de-Percep-o-P-blica-sobre-IA-no-Piau-.git
cd C:\Users\marco\OneDrive\Área de Trabalho\Case Monitoramento de Percepção Pública sobre IA no Piauí
pip install -r requirements.txt

Dependências usadas
O arquivo requirements.txt contém:
nginx
Copiar código
requests
pandas
matplotlib
wordcloud
streamlit
 
 ---

Como usar
1- Coletar notícias
python coleta.py
Isso gera o arquivo:
data/noticias.csv

2 - Processar dados
python processo.py
Isso cria o arquivo:
data/noticias_processadas.csv

3 - Rodar o dashboard
streamlit run dashboard.py

Abra o link no navegador que aparecer no terminal (geralmente http://localhost:8501).

- Funcionalidades do Dashboard
Gráfico de distribuição de sentimentos (positivo, negativo, neutro).
Nuvem de palavras com os termos mais frequentes.
Tabela interativa com título, sentimento e link das notícias.
Aviso ético sobre limitações da análise.

- Observações
A análise de sentimentos é baseada em palavras-chave simples.
Não captura sarcasmo, ironia ou contextos complexos.
Recomendado apenas como demonstração educacional.

- Autor

Desenvolvido por Marcos Carvalho (https://github.com/mvcarvalhos2)
#Projeto desenvolvido para monitoramento simples de notícias sobre Inteligência Artificial no Piauí.
