import os
from pathlib import Path
import argparse
import json
from question_utils import *

#example: python3 .\question_and_analysis.py sum

STRING_1 = 'Given this original program code: \n\n'
STRING_2 = 'And this mutant code: \n'
STRING_3 = 'Return me in a JSON format, only ONE, the name of the mutant program being the name of the function; identify if the mutant code is equivalent to the original program code, think about it because I could be sending you some that are really equivalent and others that are not; provide test set for both programs to run; provide the output of the original program according to the suggested test set and the output of the mutated program; with explanations! if you can not predict the output by non-deterministic changes, do not provide tests. just tell me if it is equivalent\n'
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
    #print("pergunta: ",big_string)
    #print("\n"*2)
    response = generate_response(big_string)
    message_json = None
    if response:
        #print("response: ", response)
        #print("Original message content:", response)
        message_content = response["choices"][0]["message"]["content"]
        #print to see all response
        #print("message_content: ", message_content)
        #print("\n"*2)
        try:
            message_content_handled = remover_quebra_linha(message_content)
            message_content_handled = handle_response(message_content_handled)
            message_json = json.loads(message_content_handled)
        except json.JSONDecodeError as e:
            processed_json = format_json(message_content_handled)
            processed_json = transform_to_json(processed_json)
            message_json = json.loads(processed_json)
        except Exception as e:
            print("Error occurred:", e)
            print("Original message content:", message_content_handled)

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
    
    responses = []
    #comenta esse for se nao quer chamar a api
    for mutant in mutants:
        print(mutant)
        response = get_big_string(original_program, read_file(mutant), program_name)
        #testar sem chamar api
        #response = {'mutant_program': 'muta2_boundedQueue.c', 'equivalent': False, 'tests': [{'input': [-1], 'original_output': 'Invalid size.\n', 'mutant_output': 'Invalid size.\n', 'explanation': 'For invalid input, both the original and mutant programs output the same error message.'}, {'input': [2], 'original_output': '[1, 2]\n', 'mutant_output': '', 'explanation': "The test case enqueues two elements, then prints the queue. The original program correctly outputs the queue with both elements. The mutant program, however, doesn't add any elements to the queue and therefore prints out an empty array."}, {'input': [2], 'original_output': 'Queue is Full\nQueue is already empty!\n', 'mutant_output': 'Queue is Full\nQueue is already empty!\n', 'explanation': 'This test inserts two elements, then attempts to insert a third element (resulting in a full queue) and then attempts to remove three elements (resulting in empty queue and already empty queue error messages). Both programs output the same messages in the same order.'}]}
        response['mutant_program'] = mutant.name
        #Escrevendo em um arquivo json o que vem do ChatGPT
        write_responses_to_file(response, program_name)
        responses.append(response)

    #Cria um arquivo que contem um vetor de analise 
    #[1,2,3,4]
    #1 = Numero do mutante
    #2 = Resultado da equivalencia do ChatGPT
    #3 = Resultado da equivalencia arquivo
    #4 = ChatGPT acertou?
    analysis(f"{program_name}.json",f"equivalents_{program_name}.txt", f"minimal_{program_name}.txt",f"analysis_{program_name}.txt")
    os.chdir("../..")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("program_name", help="name of the program to generate questions")
    args = parser.parse_args()

    main(args.program_name)
