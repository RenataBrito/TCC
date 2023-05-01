import sys
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix

#example: python3 statistical_analysis.py programs\sum\analysis_sum.txt

filename = sys.argv[1]

data = []
with open(filename) as f:
    for line in f:
        row = line.strip()[1:-1].split(',')
        data.append([row[0], eval(row[1]), eval(row[2]), eval(row[3])])

data = np.array(data)

# Extrai as colunas de interesse
#O y_true representa as respostas verdadeiras
#y_pred representa as previsões feitas pelo ChatGPT
y_true = data[:, 2]
y_pred = data[:, 1]

# Calcula a matriz de confusão
confusion = confusion_matrix(y_true, y_pred)

# Calcula as métricas de desempenho
tp = confusion[1, 1]
tn = confusion[0, 0]
fp = confusion[0, 1]
fn = confusion[1, 0]

accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
specificity = tn / (tn + fp)
f1_score = 2 * precision * recall / (precision + recall)

print('Matriz de Confusão:')
print(confusion)
print('Acurácia:', accuracy)
print('Precisão:', precision)
print('Sensibilidade:', recall)
print('Especificidade:', specificity)
print('F1 Score:', f1_score)

# Define as classes
classes = np.unique(y_true)

# Plota a matriz de confusão
fig, ax = plot_confusion_matrix(conf_mat=confusion,
                                colorbar=True,
                                show_absolute=True,
                                show_normed=True,
                                class_names=classes)

ax.set_xlabel("Previsões")
ax.set_ylabel("Respostas Verdadeiras")

plt.show()
