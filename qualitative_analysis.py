import argparse
import os
import matplotlib.pyplot as plt

def create_charts(data):
    # Define empty lists to store the values of Mutante and Analise ChatGPT
    data_0_values = []
    data_minus_1_values = []

    # Extract the values of Mutante and Analise ChatGPT from the data
    for line in data:
        # Extract the values of Mutante and Analise ChatGPT
        data_0_values.append(line[0])
        data_minus_1_values.append(line[-1])

    # Count the number of True and False values in Analise ChatGPT
    true_count = sum(data_minus_1_values)
    false_count = len(data_minus_1_values) - true_count

    # Print the count of True and False values
    print("Count of True values in Analise ChatGPT:", true_count)
    print("Count of False values in Analise ChatGPT:", false_count)

    # Plot the bar chart
    x = range(len(data_0_values))
    plt.bar(x, data_minus_1_values)
    plt.xlabel('Mutante')
    plt.ylabel('Analise ChatGPT')
    plt.title('Relacionamento entre Mutante e a Analise do ChatGPT')

    # Set x-axis ticks and labels
    plt.xticks(x, data_0_values)

    plt.show()

def process_files(folder_path):
    data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith("analysis_"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as file:
                    for line in file:
                        line = line.strip()[1:-1]  # Remove square brackets and leading/trailing spaces
                        values = line.split(', ')
                        values = [int(values[0])] + [value == 'True' for value in values[1:]]
                        data.append(values)
    
    return data

# Example usage
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analise qualitativa')
    parser.add_argument('path', type=str, help='Path para pasta')
    args = parser.parse_args()

    if os.path.isdir(args.path):
        data = process_files(args.path)
        create_charts(data)
    else:
        print("Invalid folder path.")
