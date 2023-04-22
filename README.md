# Explorando o poder dos Large Language Models na identificação de mutantes equivalentes em programas escritos em linguagem C

## clearing_proteum_data.py
A função **clearing_proteum_data** serve para limpar o codigo dos mutantes gerados pela Proteum, você deverá passar como parametro os seguitens itens: 
- **base_dir** : Pasta que contem o codigo original e seus mutantes e o nome da pasta é igual ao nome do mutante
- **prog** : Nome do programa 
- **firstMutant** : Numero inicial do mutante que deseja fazer a limpeza
- **lastMutant** : Numero final do mutante que deseja fazer a limpeza
- **stringPattern** : String unica ate onde vc deseja excluir, no caso, a maioria dos programas foi utilizado a funlockfile

**Exemplo de como utilizar:**

```python3 clearing_proteum_data.py /mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum sum 0 2 funlockfile ```

Assim, na pasta de cada programa, será criado uma pasta **mutants** com os mutantes sem as variaveis geradas pela Proteum.

## question_and_analysis.py

É necessario ter um arquivo nessa pasta que seja o "Oráculo", para fins de comparação se o ChatGPT acertou ou não. E ele deve se chamar **equivalents_program.txt**

Após a limpeza dos mutantes, o script **question_and_analysis.py** vai gerar um prompt para ser enviado ao ChatGPT e analisa-lo.

Esse script irá:
1. Montar um prompt pra mandar para o ChatGPT, assim, ele navega dentro da pasta dos programas, e para cada programa, ele cria prompts de quantidade igual ao seus mutantes. 
2. Salvar na pasta do programa, um arquivo **programa.json** e **analysis_program.txt**

Onde:

- **programa.json** : terá um json com os dados retornados do ChatGPT
- **analysis_program.txt** : terá um arquivo onde cada linha é um vetor para cada mutante que foi analisado

**Exemplo de como utilizar:**

```python3 question.py sum```

## graphic.py

Para executar o script, é necessario passar como parametro a pasta onde foi gerado o arquivo **analysis_program.txt**.

**Exemplo de como utilizar:**

```python3 .\graphic.py programs\sum\analise_sum.txt```

O script irá gerar dois gráficos, o primeiro sendo um gráfico em formato de pizza mostrando a porcentagem de acerto do ChatGPT e o segundo sendo um gráfico de barra onde apresenta para cada mutante se o ChatGPT acertou ou não.
