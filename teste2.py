import os
import shutil
import sys

def copiar_arquivos(pasta_origem, pasta_destino, numeros, nomeprograma):
    # Verifica se a pasta de destino existe, caso contrário, cria-a
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Lê o conteúdo do arquivo
    with open(numeros, 'r') as file:
        numeros = file.read().split()
    
     # Converte os números para inteiros
    numeros = [int(num) for num in numeros]

    # Percorre os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        if nome_arquivo.startswith("muta"):
            # Obtém o número do arquivo atual
            numero_arquivo = int(nome_arquivo.split('_')[0][4:])
            # Verifica se o número do arquivo está presente na lista de números
            if numero_arquivo in numeros:
                # Copia o arquivo para a pasta de destino
                origem = os.path.join(pasta_origem, nome_arquivo)
                destino = os.path.join(pasta_destino, nome_arquivo)
                shutil.copy2(origem, destino)

# Obtém os caminhos das pastas de origem e destino e o nome do arquivo

pasta_origem = "C:\\Users\\renat\\Desktop\\TCC\\Pesquisa\\Pesquisa\\mutants\\Mutants\\stats\\Mutants"
pasta_destino = "C:\\Users\\renat\\Desktop\\TCC\\projeto\\TCC\\programs\\stats"
arquivo_numerosMin = "C:\\Users\\renat\\Desktop\\TCC\\projeto\\TCC\\programs\\stats\\minimal_stats.txt"
arquivo_numerosEqui = "C:\\Users\\renat\\Desktop\\TCC\\projeto\\TCC\\programs\\stats\\equivalents_stats.txt"

copiar_arquivos(pasta_origem, pasta_destino, arquivo_numerosMin, "stats")
copiar_arquivos(pasta_origem, pasta_destino, arquivo_numerosEqui, "stats")

