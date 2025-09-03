# DECISIONS.md

Este documento registra as principais decisões de projeto tomadas durante o desenvolvimento do sistema de monitoramento de notícias sobre Inteligência Artificial no Piauí.

---

## Abordagem para Análise de Sentimento

Optamos por uma abordagem baseada em regras simples (palavras-chave positivas e negativas) em vez de treinar ou utilizar um modelo de Machine Learning.

Motivos:

- Simplicidade: não é necessário treinar, validar ou manter modelos complexos.
- Transparência: fácil explicar por que uma notícia foi classificada como "Positiva" ou "Negativa".
- Baixo custo: dispensa bibliotecas pesadas e processamento adicional.
- Adequado ao escopo: como o objetivo é demonstração educacional e não análise comercial crítica, uma solução simples é suficiente.

---

## Tratamento de Erros e Falhas de Coleta

Durante a coleta de notícias via Google News RSS, alguns problemas podem ocorrer, como ausência de resultados ou falha de conexão.

Decisões tomadas:

- Tratamento de exceções no carregamento de dados:  
  Se o arquivo `noticias_processadas.csv` não existir, o dashboard exibe uma mensagem clara ao usuário pedindo para executar primeiro o coletor e o processador.
- Falta de notícias no feed:  
  O sistema retorna apenas os dados disponíveis. Se o DataFrame ficar vazio, o dashboard mostra avisos amigáveis em vez de quebrar.

---

## Conclusão

Essas escolhas foram guiadas pela necessidade de criar um projeto funcional, leve e transparente, priorizando a educação e a facilidade de uso sobre sofisticação técnica.
