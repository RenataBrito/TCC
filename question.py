STRING_1 = 'Given this original program code: \n\n'
STRING_2 = 'And this mutant code: \n'
STRING_3 = 'Return me in a JSON format, only, the name of the mutant program being the name of the function; identify if the mutant code is equivalent to the original program code; provide test set for both programs to run; provide the output of the original program according to the suggested test set and the output of the mutated program; NO explanations!!\n\n'
STRING_4 = 'If you identify that it is not equivalent, provide a test that results in different outputs.\n\n'

STRING_5 = '''Follow an example
{ 
 "mutant_program": "sum",
 "equivalent": true,
 "tests":[
   {
     "input": [1,2,3],
     "original_output": 0,
     "mutant_output": 1
   },
   {
     "input": [4,5,6],
     "original_output": 10,
     "mutant_output": 7
   },
   {
     "input": [7,8,9],
     "original_output": 12,
     "mutant_output": 16
   }
 ]
}'''


def get_big_string(program_folder, program_file, mutant_folder, mutante_file):
    with open(f'{program_folder}/{program_file}', 'r') as f1, open(f'{mutant_folder}/{mutante_file}', 'r') as f2:
        str1 = STRING_1 + f1.read().strip() + '\n\n'
        str2 = STRING_2 + f2.read().strip() + '\n\n'
    str3 = STRING_3
    str4 = STRING_4
    str5 = STRING_5
    return str1 + str2 + str3 + str4 + str5


def main():
    program_folder = '/mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum'
    program_file = 'sum.c'
    mutant_folder = '/mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum/mutants'
    mutante_file = 'muta0_sum.c'
    big_string = get_big_string(
        program_folder, program_file, mutant_folder, mutante_file)
    print(big_string)


if __name__ == '__main__':
    main()
