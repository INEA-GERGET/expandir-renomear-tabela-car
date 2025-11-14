# Expandir e renomear tabela do CAR

## Sumário
1. [Descrição](#Descrição)
2. [Uso](#Uso)
   - [Sobre os arquivos](#Sobre-os-arquivos)
4. [Instalação](#Instalação)
5. [Exemplos](#Exemplos)

## Descrição

Script para expandir a [tabela do CAR](https://www.car.gov.br/#/) que vem com nome e CPF/CNPJ com múltiplos dados na mesma célula, expandindo-os para linhas distintas e repetindo o restante da informação. Também renomeia as colunas para ficar de acordo com as entradas nos formulários do Survey123. 


## Uso
Para utilizar os scripts deste repositório é necessário substituir o arquivo `Tabela_CAR.csv` na pasta desse repositório.
Execute o código `01_limpar_renomear.py` para remover algumas colunas e renomeá-las. 
Execute o código `02_expandir.py` para expandir as células com múltiplos dados.

### Sobre os arquivos

* [**01_limpar_renomear.py**](01_limpar_renomear.py): Tem como input a `Tabela_CAR.csv` e output `Tabela_CAR_limpa.csv` com colunas removidas e renomeadas.
* [**02_expandir.py**](02_expandir.py): Tem como input a `Tabela_CAR_limpa.csv` e retorna a `Tabela_CAR_Final.csv` com os dados expandidos, é possível verificar no terminal a quantidade de linhas a mais que foram geradas na tabela final. 
* [**Tabela_CAR.csv**](Tabela_CAR.csv): Tabela CAR vazia para preservar os dados sensíveis contidos nela. 

## Instalação

Para utilizar os scripts é necessária a instalação das bibliotecas Python:

* **pandas**: Esta é a biblioteca fundamental para manipulação e análise de dados. É utilizada para ler o arquivo CSV (pd.read_csv), estruturar os dados em DataFrames, aplicar filtros (df.loc[...] ou df[...]), renomear colunas (df.rename()), concatenar DataFrames (pd.concat()) e exportar resultados (df.to_csv(), df.to_excel()).

## Exemplos 

A expansão de dados da planilha acontece da seguinte forma: 
* **Planilha de exemplo antes** -> Essa planilha contém multiplos dados em uma única célula no 'Nome' e no 'CPF', mas infromações que são comuns entre elas como 'Index' e 'Município':
<img src="/arquivo-readme/planilha_exemplo_antes.png"/>

* **Planilha de exemplo expandida** -> O arquivo de saída com mais linhas, pois elas foram separadas das células que estavam:
<img src="/arquivo-readme/planilha_exemplo_expandida.png"/>

