import sys
import matplotlib.pyplot as plt

#example: python3 .\grafico.py programs\sum\analise.txt

filename = sys.argv[1]

x = []
y = []

with open(filename, 'r') as f:
    for line in f:
        data = eval(line.strip())
        print(data)
        x.append(data[0])
        y.append(data[3])

# cria um dicionário com as opções e seus respectivos contadores
counter = {True: 0, False: 0}
for item in y:
    counter[item] += 1

# verifica se o resultado de y para cada x é diferente de zero
diff_from_zero = []
for i in range(len(x)):
    if y[i] != 0:
        diff_from_zero.append(True)
    else:
        diff_from_zero.append(False)

# cria um gráfico de dispersão dos mutantes em relação ao acerto
fig, ax = plt.subplots()
plt.scatter(x, y)
plt.xticks(range(int(min(x)), int(max(x))+1, 1))
plt.xlabel('Mutante')
plt.ylabel('Acertou?')

# traça uma linha verde onde o resultado é diferente de zero e uma linha vermelha onde é igual a zero
for i in range(len(x)):
    if diff_from_zero[i]:
        ax.axvline(x=x[i], ymin=0, ymax=1, color='green', linewidth=2)
    else:
        ax.axvline(x=x[i], ymin=0, ymax=0.5, color='red', linewidth=2)

plt.show()
