import sys
import matplotlib.pyplot as plt
import numpy as np

#example: python3 .\grafico.py programs\sum\analise_sum.txt

filename = sys.argv[1]

# Ler o arquivo e armazenar os vetores em uma lista
with open(filename, 'r') as f:
    data = [eval(line.strip()) for line in f]

# Calcular a proporção de acertos na quarta informação
num_correct = sum(vec[3] for vec in data)
prop_correct = num_correct / len(data)

# Criar um dicionário para armazenar a contagem de valores True e False para cada posição
counts = {}

# Percorrer a lista de vetores e atualizar a contagem no dicionário
for vec in data:
    pos = vec[0]
    val = int(vec[3])
    if pos not in counts:
        counts[pos] = [0, 0]
    counts[pos][val] += 1

# Gerar um gráfico de pizza com a proporção calculada
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
labels = ['True', 'False']
sizes = [prop_correct, 1 - prop_correct]
colors = ['lightgreen' if label == 'True' else 'salmon' for label in labels]
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
ax1.set_title('Proporção de acertos')

# Gerar um gráfico de barras com os dados do dicionário
x = np.arange(max(counts.keys()) + 1)
width = 0.35
rects1 = [counts[i][1] if i in counts else 0 for i in range(len(x))]
colors = ['lightgreen' if h > 0 else 'gray' for h in rects1]
rects1 = ax2.bar(x, rects1, width, color=colors)
ax2.set_ylabel('Acertou?')
ax2.set_xlabel('Mutante')
ax2.set_xticks(x)
ax2.set_xticklabels([str(i) for i in x])
ax2.set_yticks([0, 1])
ax2.set_yticklabels(['FALSE', 'TRUE'])
ax2.set_title('Contagem de acertos por mutante')

plt.show()
