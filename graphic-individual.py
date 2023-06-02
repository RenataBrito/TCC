import argparse
import matplotlib.pyplot as plt

def create_charts(file_path, program, option):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()[1:-1]  # Remove square brackets and leading/trailing spaces
            values = line.split(', ')
            values = [int(values[0])] + [value == 'True' for value in values[1:]]
            data.append(values)

    if option == 0:
        data = [item for item in data if item[2]]  # Filter data where the 3rd element is True
    elif option == 1:
        data = [item for item in data if not item[2]]  # Filter data where the 3rd element is False

    # Calculate the percentage of True values in the fourth element of each vector
    true_percentages = sum(1 for item in data if item[3]) / len(data) * 100
    false_percentages = 100 - true_percentages

    # Create the pie chart
    labels = ['True', 'False']
    sizes = [true_percentages, false_percentages]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # Explode the 'True' slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

    # Add legends for colors
    legend_labels = ['True', 'False']
    plt.legend(legend_labels, loc='upper right')

    plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle
    if option == 0:
        plt.title(f'Porcentagem do ChatGPT - {program} - equivalentes')
    elif option == 1:
        plt.title(f'Porcentagem do ChatGPT - {program} - minimais')
    else:
        plt.title(f'Porcentagem do ChatGPT - {program} - todos mutantes')
    plt.show()

# Example usage
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create pie charts based on file data.')
    parser.add_argument('file_path', type=str, help='Path to the file')
    parser.add_argument('program', type=str, help='Name of the program')
    parser.add_argument('option', type=int, choices=[0, 1, 2], help='Option to filter the data')
    args = parser.parse_args()

    create_charts(args.file_path, args.program, args.option)
