# Datasets do Trabalho M2

Sugestões de datasets para o trabalho da M2, em formato CSV (separador `,`, codificação UTF-8).

---

## 1. Filmes e séries da Netflix: `filmes-series-netflix.csv`

- **Fonte original:** [Netflix Movies and TV Shows](https://www.kaggle.com/shivamb/netflix-shows), de Shivam Bansal (Kaggle)
- **Obtido via:** [TidyTuesday 2021-04-20](https://github.com/rfordatascience/tidytuesday/tree/main/data/2021/2021-04-20)

| Coluna | Exemplos de valores |
|---|---|
| `titulo` | `3%`, `Dark`, `Klaus` |
| `tipo` | `Movie`, `TV Show` |
| `pais` | `Brazil`, `United States, India` (pode ter vários países ou ficar vazio) |
| `data_adicao` | `August 14, 2020` |
| `ano` | `2019`, `2020` |
| `classificacao` | `TV-MA`, `TV-14`, `PG-13` |
| `duracao` | `95 min` (filmes), `1 Season`, `4 Seasons` (séries) |
| `generos` | `International TV Shows, TV Dramas, TV Sci-Fi & Fantasy` |

## 2. Barras de chocolate: `chocolates.csv`

- **Fonte original:** [Flavors of Cacao](http://flavorsofcacao.com/chocolate_database.html), avaliações de 2006 a 2021
- **Obtido via:** [TidyTuesday 2022-01-18](https://github.com/rfordatascience/tidytuesday/tree/main/data/2022/2022-01-18)

| Coluna | Exemplos de valores |
|---|---|
| `barra` | `Kokoa Kamili, batch 1` (origem do grão ou nome da barra) |
| `fabricante` | `5150`, `Valrhona` |
| `pais_fabricante` | `U.S.A.`, `France`, `Brazil` |
| `ano_avaliacao` | `2019` |
| `origem_cacau` | `Tanzania`, `Madagascar`, `Blend` |
| `cacau` | `70%`, `76%` |
| `ingredientes` | `3- B,S,C`: quantidade e siglas |
| `caracteristicas` | `rich cocoa, fatty, bready` |
| `nota` | `1` a `4`, em passos de `0.25` |

## 3. Móveis da IKEA: `moveis-ikea.csv`

- **Fonte original:** loja on-line da [IKEA Arábia Saudita](https://www.ikea.com/sa/en/cat/furniture-fu001/), raspada em 2020 por Ahmed Kallam ([Kaggle](https://www.kaggle.com/ahmedkallam/ikea-sa-furniture-web-scraping))
- **Obtido via:** [TidyTuesday 2020-11-03](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-11-03)
- Os preços estão em **riais sauditas (SR)**. O mesmo móvel pode aparecer em mais de uma categoria.

| Coluna | Exemplos de valores |
|---|---|
| `nome` | `BILLY`, `NORDVIKEN / NORDVIKEN` |
| `categoria` | `Beds`, `Chairs`, `Tables & desks` (17 categorias) |
| `descricao` | `Bar table, in/outdoor, 51x51 cm` |
| `preco` | `265.0` |
| `preco_antigo` | `No old price`, `SR 2,375` |
| `vende_online` | `True`, `False` |
| `outras_cores` | `Yes`, `No` |
| `profundidade`, `altura`, `largura` | em cm: `50`, ou vazio quando não informado |
| `link` | página do produto |

## 4. Lámen instantâneo: `lamens.csv`

- **Fonte original:** [The Ramen Rater, "The Big List"](https://www.theramenrater.com/resources-2/the-list/)
- **Obtido via:** [TidyTuesday 2019-06-04](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-06-04)

| Coluna | Exemplos de valores |
|---|---|
| `variedade` | `Kelp Broth Shio Ramen` |
| `marca` | `Nissin`, `Maruchan` |
| `estilo` | `Pack`, `Cup`, `Bowl`, `Tray` (2 linhas estão vazias) |
| `pais` | `Japan`, `Brazil`, `South Korea` |
| `estrelas` | `0` a `5`, como `3.75`; `NA` quando não há nota |

## 5. Jogos da Steam: `jogos-steam.csv`

- **Fonte original:** [Steam Spy](https://steamspy.com/year/), coletado por [Liza Wood](https://github.com/lizawood/apps-and-games)
- **Obtido via:** [TidyTuesday 2019-07-30](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-07-30)
- **Recorte:** só os jogos lançados entre 2004 e 2018 que têm nota no Metacritic (`metascore`).

| Coluna | Exemplos de valores |
|---|---|
| `jogo` | `Half-Life 2`, `Portal 2` |
| `lancamento` | `Nov 16, 2004` |
| `preco` | `9.99` em dólares; `NA` quando não informado |
| `donos` | `10,000,000 .. 20,000,000` (faixa estimada de jogadores que têm o jogo) |
| `desenvolvedora` | `Valve` |
| `publicadora` | `Valve`, `Ubisoft` |
| `tempo_medio_min` | `110` (minutos jogados, em média); `NA` em 2 linhas |
| `metascore` | `0` a `100` |

## 6. Vulcões: `vulcoes.csv`

- **Fonte original:** [Smithsonian Institution, Global Volcanism Program](https://volcano.si.edu/)
- **Obtido via:** [TidyTuesday 2020-05-12](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-05-12)

| Coluna | Exemplos de valores |
|---|---|
| `nome` | `Etna`, `Vesuvius` |
| `tipo` | `Stratovolcano`, `Stratovolcano(es)`, `Shield`, `Caldera` |
| `ultima_erupcao` | `1972`, `-6850` (negativo = antes de Cristo), `Unknown` |
| `pais` | `Japan`, `Chile` |
| `regiao` | `South America`, `Japan, Taiwan, Marianas` (19 regiões) |
| `altitude_m` | `3976` (metros; alguns são negativos, submarinos) |
| `evidencia` | `Eruption Observed`, `Eruption Dated`, `Evidence Credible`, `Evidence Uncertain`, `Unrest / Holocene` |
| `populacao_10km` | pessoas morando a até 10 km |
| `latitude`, `longitude` | `14.501`, `-90.876` |

## 7. Raças de cães: `racas-de-caes.csv`

- **Fonte original:** [American Kennel Club](https://www.akc.org/dog-breeds/), coletado por [KKakey](https://github.com/kkakey/dog_traits_AKC)
- **Obtido via:** [TidyTuesday 2022-02-01](https://github.com/rfordatascience/tidytuesday/tree/main/data/2022/2022-02-01)

| Coluna | Exemplos de valores |
|---|---|
| `raca` | `Retrievers (Labrador)`, `French Bulldogs` |
| `tipo_pelo` | `Double`, `Smooth`, `Wiry`, `Curly` |
| `comprimento_pelo` | `Short`, `Medium`, `Long` |
| `afeto_familia`, `bom_com_criancas`, `bom_com_outros_caes`, `queda_pelo`, `energia`, `latidos`, `treinabilidade` | de `1` (pouco) a `5` (muito) |
| `popularidade_2020` | `1` = raça mais registrada nos EUA em 2020 |
| `link` | página da raça no site da AKC |
| `imagem` | ilustração da raça (URL) |

## 8. Países do mundo: `paises.csv`

- **Fonte original:** CIA World Factbook, compilado por Fernando Lasso no [Kaggle (Countries of the World)](https://www.kaggle.com/fernandol/countries-of-the-world)
- **Obtido via:** [espelho no GitHub](https://github.com/PacktPublishing/Hands-On-Data-Preprocessing-in-Python/tree/main/Chapter14)
- Os números decimais usam **vírgula**, como no Brasil.

| Coluna | Exemplos de valores |
|---|---|
| `pais` | `Brazil`, `Japan` |
| `regiao` | `LATIN AMER. & CARIB`, `WESTERN EUROPE` (11 regiões) |
| `populacao` | `188078227` |
| `area_mi2` | área em milhas quadradas |
| `densidade` | `48,0` (habitantes por milha quadrada) |
| `pib_per_capita` | `8000` (dólares); vazio em 1 país |
| `alfabetizacao` | `86,4` (%); pode ficar vazio |
| `telefones_por_mil` | `225,3` |
| `natalidade`, `mortalidade` | por mil habitantes: `16,56` |
| `mortalidade_infantil` | por mil nascimentos: `29,61` |

## 9. Apps da Google Play: `apps-google-play.csv`

- **Fonte original:** [Google Play Store Apps](https://www.kaggle.com/lava18/google-play-store-apps), de Lavanya Gupta (Kaggle), coletado em 2018
- **Obtido via:** [espelho no GitHub](https://github.com/michalis0/Business-Intelligence-and-Analytics/tree/main/data/google-play-store-apps)
- **Recorte:** só apps com pelo menos 1 milhão de instalações, sem apps repetidos.

| Coluna | Exemplos de valores |
|---|---|
| `app` | `Infinite Painter`, `WhatsApp Messenger` |
| `categoria` | `GAME`, `TOOLS`, `ART_AND_DESIGN` (32 categorias) |
| `nota` | `4.5`; `NaN` em 2 linhas |
| `avaliacoes` | `87510` (quantidade de avaliações) |
| `tamanho` | `19M`, `8.7M`, `695k`, `Varies with device` |
| `instalacoes` | `1,000,000+`, `50,000,000+` |
| `tipo` | `Free`, `Paid` |
| `preco` | `0`, `$4.99` |
| `classificacao` | `Everyone`, `Teen`, `Everyone 10+`, `Mature 17+` |
| `generos` | `Art & Design`, `Puzzle;Brain Games` |
| `atualizado_em` | `August 1, 2018` |

## 10. Carros usados: `carros-usados.csv`

- **Fonte original:** anúncios do site CarDekho (Índia), publicados por Nehal Birla no [Kaggle (Vehicle dataset)](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho)
- **Obtido via:** [espelho no GitHub](https://github.com/ishu17077/ML-Projects/tree/main/car_price_pred)
- **Recorte:** só carros de 2015 em diante, sem anúncios repetidos e sem linhas com o consumo vazio.
- Os preços estão em **rupias indianas**.

| Coluna | Exemplos de valores |
|---|---|
| `nome` | `Hyundai i20 Sportz Diesel` |
| `ano` | `2017` |
| `preco_rupias` | `450000` |
| `km` | `45000` (quilômetros rodados) |
| `combustivel` | `Petrol`, `Diesel`, `CNG`, `LPG` |
| `vendedor` | `Individual`, `Dealer`, `Trustmark Dealer` |
| `cambio` | `Manual`, `Automatic` |
| `dono` | `First Owner`, `Second Owner`, `Third Owner`, `Fourth & Above Owner`, `Test Drive Car` |
| `consumo` | `23.4 kmpl`, `26.6 km/kg` (gás) |
| `motor` | `1248 CC` |
| `potencia` | `74 bhp` |
| `assentos` | `5` |

---
