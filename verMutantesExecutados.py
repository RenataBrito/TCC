import os

# Caminho para o arquivo X
program = "UnixCal"
caminho_arquivo_X = f'programs\\{program}\\analysis_{program}.txt'

# Caminho para a pasta Y
caminho_pasta_Y = f'programs\\{program}\\mutants'

# Ler o arquivo X
with open(caminho_arquivo_X, 'r') as arquivo_X:
    linhas_X = arquivo_X.readlines()

# Criar uma lista com os números do arquivo X
numeros_X = [eval(linha)[0] for linha in linhas_X]

# Listar arquivos na pasta Y
arquivos_Y = os.listdir(caminho_pasta_Y)

# Verificar se há algum arquivo na pasta Y que não tenha o número do arquivo X
for arquivo in arquivos_Y:
    numero = int(arquivo.split('_')[0].replace('muta', ''))
    
    if numero not in numeros_X:
        print(numero)
        #print(f"O arquivo {arquivo} não tem um número correspondente no arquivo X.")
