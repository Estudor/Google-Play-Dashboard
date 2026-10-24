# Google Play Dashboard
**Membros:** Bruno Dal Prá (Estudor), Bruno Shinjy Kemura (Bruno467890)
**Dataset:** Apps da Google Play (https://www.kaggle.com/datasets/lava18/google-play-store-apps)
**App publicado:** https://...streamlit.app

## Funcionalidades
- [x] Leitura do CSV
- [x] Conversão das colunas
- [x] Total de apps
- [x] Preço Médio
- [x] Quantidade de apps com nota maior ou igual 4.5
- [x] App com maior quantidade de instalações
- [x] App de menor tamanho
- [x] Filtro de categorias
- [x] Buscar apps por nome
- [x] Filtro de recentemente atualizados
      
## Funcionalidade extra
*O que ela faz, como usar e como foi feita.*

**O que ela faz**
Uma funcionalidade que usa a data de atualização do app para mostrar os apps que foram atualizados
em um periodo de tempo, assim o usuário sabe se o jogo está abandonado ou atualizado

**Como usar**
Apenas clique no checkbox escrito "Filtro recente atualizados", ao lado do filtro de categorias.

**Como foi feita**
Foi utilizada o modulo datetime do Python para transformar as datas dos apps do dataset em um objeto date, que então é comparado com uma data utilizada 
pelo sistema para simular uma "Data atual" (Já que o dataset é de 2018), para saber se a data fica dentro de um período de 30 dias da "Data atual",
se sim, o filtro mostra o app, se não, não mostra.

## Como rodar
Comandos para rodar o app no computador.

pip install -r trabalhoM2/requirements.txt
python -m streamlit run trabalhoM2/app.py
