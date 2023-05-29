file_path = input("Digite o caminho do arquivo: ")

# Lê o arquivo e obtém as linhas
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove os caracteres de quebra de linha
lines = [line.strip() for line in lines]

# Converte as linhas em listas e substitui as strings
data = []
for line in lines:
    item = eval(line)
    if isinstance(item[0], str):
        item[0] = eval(item[0])
    data.append(item)

# Substitui as strings "false" por False e "true" por True
for item in data:
    for i in range(1, len(item)):
        if isinstance(item[i], str):
            if item[i].lower() == 'false':
                item[i] = False
            elif item[i].lower() == 'true':
                item[i] = True

# Escreve as alterações de volta no arquivo
with open(file_path, 'w') as file:
    for item in data:
        file.write(str(item) + '\n')

print("As substituições foram feitas e o arquivo foi atualizado com sucesso.")
