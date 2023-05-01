import os
from pathlib import Path
import argparse
import json
from question_utils import *

#example: python3 .\question_and_analysis.py sum

STRING_1 = 'Given this original program code: \n\n'
STRING_2 = 'And this mutant code: \n'
STRING_3 = 'Return me in a JSON format, only ONE, the name of the mutant program being the name of the function; identify if the mutant code is equivalent to the original program code; provide test set for both programs to run; provide the output of the original program according to the suggested test set and the output of the mutated program; with explanations!!\n\n'
STRING_4 = 'If you identify that it is not equivalent, provide a test that results in different outputs.\n\n'

STRING_5 = '''Follow an example
{ 
 "mutant_program": "sum",
 "equivalent": true,
 "tests":[
   {
     "input": [1,2,3],
     "original_output": 0,
     "mutant_output": 1,
     "explanation": "text"
   },
   {
     "input": [4,5,6],
     "original_output": 10,
     "mutant_output": 7,
     "explanation": "text"
   },
   {
     "input": [7,8,9],
     "original_output": 12,
     "mutant_output": 16,
     "explanation": "text"
   }
 ]
}'''

def get_big_string(original, mutant, program):
    str1 = f"{STRING_1} {program}\n{original}\n\n"
    str2 = f"{STRING_2} {program}\n{mutant}\n\n"
    str3 = f"{STRING_3}\n"
    str4 = f"{STRING_4}\n"
    str5 = f"{STRING_5}\n"
    big_string = str1 + str2 + str3 + str4 + str5
    response = generate_response(big_string)
    message_json = None
    if response:
        message_content = response["choices"][0]["message"]["content"]
        #print to see all response
        #print("message_content: ", message_content)
        #print("\n"*2)
        message_content_handled = handle_response(message_content)
        message_json = json.loads(message_content_handled)
    return message_json

def main(program_name):
    program_path = Path("programs") / program_name
    os.chdir(program_path)
    current_path = Path.cwd()
    program_file = program_name + ".c"
    original_program = read_file(program_file)

    mutants_path = current_path / "mutants"
    if mutants_path.exists():
        mutants = [mutant for mutant in mutants_path.iterdir() if mutant.is_file()]
    else:
        mutants = []
    
    # Testar sem chamar a api
    # responses = [{'mutant_program': 'muta0_sum.c', 'equivalent': False, 'tests': [{'input': [1, 2, 3], 'original_output': 6, 'mutant_output': 1, 'explanation': 'The original program correctly adds all the elements in the array to calculate the sum, while the mutant program has an infinite loop because the condition for the loop (0 < size) is always true, resulting in an incorrect and smaller output.'}, {'input': [4, 5, 6], 'original_output': 15, 'mutant_output': 4, 'explanation': 'Similarly to the previous test, the original program correctly calculates the sum, while the mutant program has an infinite loop resulting in an incorrect and smaller output.'}, {'input': [7, 8, 9], 'original_output': 24, 'mutant_output': 7, 'explanation': 'The original program correctly calculates the sum of the array, but the mutant program has an infinite loop resulting in an incorrect and smaller output.'}]}, {'mutant_program': 'muta1_sum.c', 'equivalent': False, 'tests': [{'input': [1, 2, 3], 'original_output': 6, 'mutant_output': 0, 'explanation': 'The original program correctly calculates the sum of the input array, which is 6. The mutant code, on the other hand, has an incorrect loop termination condition (i < 0), causing the loop to never execute and s to be returned as 0.'}, {'input': [4, 5, 6], 'original_output': 15, 'mutant_output': 0, 'explanation': 'The original program correctly calculates the sum of the input array, which is 15. The mutant code, however, has an incorrect loop termination condition (i < 0), causing the loop to never execute and s to be returned as 0.'}, {'input': [7, 8, 9], 'original_output': 24, 'mutant_output': 0, 'explanation': 'The original program correctly calculates the sum of the input array, which is 24. The mutant code, however, has an incorrect loop termination condition (i < 0), causing the loop to never execute and s to be returned as 0.'}]}]
    responses = []
    #comenta esse for se nao quer chamar a api
    for mutant in mutants:
        response = get_big_string(original_program, read_file(mutant), program_name)
        response['mutant_program'] = mutant.name
        responses.append(response)

    #Escrevendo em um arquivo txt o que vem do ChatGPT
    write_responses_to_file(responses, program_name)
    #Transformando em um arquivo no formado JSON valido o que vem do ChatGPT
    txt_to_json(f"{program_name}.txt", program_name)
    #Cria um arquivo que contem um vetor de analise 
    #[1,2,3,4]
    #1 = Numero do mutante
    #2 = Resultado da equivalencia do ChatGPT
    #3 = Resultado da equivalencia arquivo
    #4 = ChatGPT acertou?
    analysis(f"{program_name}.json",f"equivalents_{program_name}.txt",f"analysis_{program_name}.txt")
    os.chdir("../..")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("program_name", help="name of the program to generate questions")
    args = parser.parse_args()

    main(args.program_name)
