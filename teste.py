import os
import sys

def count_mutants(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split()
        return len(numbers), set(numbers)

def compare_files(dir_x, dir_y):
    for root, _, files in os.walk(dir_x):
        for file in files:
            if file.startswith('equivalents_') and file.endswith('.txt'):
                program_name = file[11:-4]  # Extract program name
                file_x = os.path.join(root, file)
                file_y = os.path.join(dir_y, 'equivalents' + program_name + '.txt')
                if os.path.isfile(file_y):
                    count_x, mutants_x = count_mutants(file_x)
                    count_y, mutants_y = count_mutants(file_y)
                    common_mutants = mutants_x.intersection(mutants_y)
                    y_only_mutants = mutants_y.difference(mutants_x)

                    print(f"Nome do mutante: equivalents_{program_name}.txt")
                    print(f"Number of file mutants in PRIMEIRO ARQUIVO QUE EU TINHA: {count_x}")
                    print(f"Number of file mutants in ARQUIVO ATUALIZADO: {count_y}")
                    print(f"Numbers that are in both files: {common_mutants}")
                    print(f"Numbers that are in the file ARQUIVO ATUALIZADO and not in PRIMEIRO ARQUIVO QUE EU TINHA: {y_only_mutants}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide two directory paths as command line arguments.")
    else:
        dir_x = sys.argv[1]
        dir_y = sys.argv[2]
        compare_files(dir_x, dir_y)
