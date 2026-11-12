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
- [ ] Imagens dos Apps
- [ ] Apps favoritos
- [ ] Comentários do usuário nos Apps favoritos
      
## Funcionalidade extra
*O que ela faz, como usar e como foi feita.*
Uma funcionalidade que usa a data de atualização do app para mostrar os apps que foram atualizados
em um periodo de tempo, assim o usuário sabe se o jogo está abandonado ou atualizado
## Como rodar
Comandos para rodar o app no computador.

temporario (dev)
git config --global user.name ""
git config --global user.email ""
pip install -r trabalhoM2/requirements.txt
python -m streamlit run trabalhoM2/app.py