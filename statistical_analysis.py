import sys
import os
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix

# Example: python3 statistical_analysis.py programs

directory_path = sys.argv[1]

data = []
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.startswith("analysis_") and file.endswith(".txt"):
            filename = os.path.join(root, file)
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
if np.array_equal(y_true, y_pred):
    classes = np.unique(y_true)
    confusion = np.array([[len(y_true)]])
    tp = len(y_true)
    tn = 0
    fp = 0
    fn = 0
else:
    classes = ["False", "True"]
    confusion = confusion_matrix(y_true, y_pred)
    tp = confusion[1, 1]
    tn = confusion[0, 0]
    fp = confusion[0, 1]
    fn = confusion[1, 0]

accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp) if tp + fp > 0 else 0
recall = tp / (tp + fn) if tp + fn > 0 else 0
specificity = tn / (tn + fp) if tn + fp > 0 else 0
f1_score = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

print('Matriz de Confusão:')
print(confusion)
print('Acurácia:', accuracy)
print('Precisão:', precision)
print('Sensibilidade:', recall)
print('Especificidade:', specificity)
print('F1 Score:', f1_score)

# Plota a matriz de confusão
fig, ax = plot_confusion_matrix(conf_mat=confusion,
                                colorbar=True,
                                show_absolute=True,
                                show_normed=True,
                                class_names=classes)

ax.set_xlabel("ChatGPT")
ax.set_ylabel("Oráculo")

plt.show()
