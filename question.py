import os
from pathlib import Path

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


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


def get_big_string(original, mutant):
    str1 = f"{STRING_1}\n{original}\n\n"
    str2 = f"{STRING_2}\n{mutant}\n\n"
    str3 = f"{STRING_3}\n"
    str4 = f"{STRING_4}\n"
    str5 = f"{STRING_5}\n"
    return str1 + str2 + str3 + str4 + str5


def main():
    programs_path = Path("programs")
    programs = [prog for prog in programs_path.iterdir() if prog.is_dir()]

    previous_program = ""
    
    for program in programs:
        os.chdir(program)
        caminho_atual = Path.cwd()
        program_file = program.name + ".c"
        original_program = read_file(program_file)

        if program.name != previous_program:
            print(f"Starting questions for {program.name}...")
            previous_program = program.name

        mutants_path = caminho_atual / "mutants"
        if mutants_path.exists():
            mutants = [mutant for mutant in mutants_path.iterdir() if mutant.is_file()]
        else:
            mutants = []

        for mutant in mutants:
            question = get_big_string(original_program, read_file(mutant))
            print(f"Question for mutant: {mutant.name}")
            print(question)
        
        os.chdir("../..")


if __name__ == '__main__':
    main()
