# TCC

## clearing_proteum_data
A função **clearing_proteum_data** serve para limpar o codigo dos mutantes gerados pela Proteum, como a ultima variavel gerada pela Proteum se chama funlockfile, então o script procupra por ela e cria um novo arquivo somente das informações que tem dela pra frente.

Dentro do projeto original eu criei uma pasta chamada **programs** onde eu coloco o código do programa original e os mutantes gerados pela Proteum.

Para fazer a limpeza basta chamar a função **clearing_proteum_data.py** e passar como parametro a pasta do programa, o nome do programa original sem a extensão, o numero do mutante inicial, numero do mutante final e o nome da ultima variavel criada pela Proteum **funlockfile**. 

Exemplo:

```python3 clearing_proteum_data.py /mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum sum 0 2 funlockfile ```

Assim, na pasta de cada programa, será criado uma pasta **mutants** com os mutantes sem as variaveis geradas pela Proteum.

## question.py

Após a limpeza dos mutantes, o script **question.py** vai gerar um prompt para ser enviado ao ChatGPT.

Esse script tem como objetivo montar um prompt pra mandar para o ChatGPT, assim, ele navega dentro da pasta dos programas, e para cada programa, ele cria prompts de quantidade igual ao seus mutantes. Inicialmente estou printando **Starting questions for PROGRAM ...**, **Question for mutant:** e a questão, apenas por questão de visualização, no futuro será enviado somenete as questões como request para API do ChatGPT.

Exemplo de como utilizar:

```python3 question.py > check.txt```

Assim é possivel visualizar no **check.txt** como ficou os prompts.