![](assets/omixdata.png)
## Tutorial: Construindo um preditor de proteínas de membrana

## Requisitos

- Ubuntu Linux (>=16.04)
- Python (>=3.5)

## Programas e bibliotecas instaladas com o `make install`

- pip3: gerenciador de pacotes do Python 3.
- Pandas (python): biblioteca do Python para processar dados de tabelas.
- sklearn (python): biblioteca de do Python para aprendizagem de máquina.
- biopython (python): biblioteca do Python para manipular dados biológicos (ex: sequências de proteínas, DNAs).
- xgboost (python): biblioteca do Python para usar o algoritmo de árvore de decisão XGBoost 
- flask (python): microframework do Python para criação de web apps.

## Executando

```
# instalar dependências
make install

# baixar dados do UniProt
make download

# pre-processar arquivos de sequencias e converter para o formato estruturado
make preprocess

# treinar o algoritmo de predição
make train

# rodar servidor web
make server
```
