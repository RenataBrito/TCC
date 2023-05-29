from dotenv import load_dotenv
import requests
import json
import os
import re

load_dotenv()
API_KEY = os.getenv("API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def generate_response(content):
    link = "https://api.openai.com/v1/chat/completions"
    id_model = "gpt-3.5-turbo"
    body_message = {
        "model": id_model,
        "messages": [{"role": "user", "content": content}]
    }
    body_message = json.dumps(body_message)

    try:
        response = requests.post(link, headers=headers, data=body_message)
        response_json = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

    if response_json.get("error"):
        error_message = response_json["error"]["message"]
        print(f"An error occurred: {error_message}")
        return None

    return response_json

def handle_response(string):
    match = re.search(r'{.*}', string, re.DOTALL)
    if match:
        return match.group(0)
    else:
        return None

def format_json(json_str):
    # Regular expression pattern to match square brackets with text inside
    pattern = r'(?<!")(\[([^[\]]+)\])'

    # Find all matches and replace them with double quotes around the text
    formatted_json = re.sub(pattern, r'["\1"]', json_str)

    # Load the formatted JSON string to validate its correctness
    try:
        parsed_json = json.loads(formatted_json)
        return parsed_json
    except json.JSONDecodeError as e:
        print("format_json - Invalid JSON format:", e)
        mutant_program_pattern = r'"mutant_program":\s*"([^"]+)"'
        equivalent_pattern = r'"equivalent":\s*(\w+)'

        # Find the matches
        mutant_program_match = re.search(mutant_program_pattern, json_str)
        equivalent_match = re.search(equivalent_pattern, json_str)

        # Extract the values
        mutant_program = mutant_program_match.group(1) if mutant_program_match else None
        equivalent = equivalent_match.group(1) if equivalent_match else None
        error_json = {
            "mutant_program": mutant_program,
            "equivalent": equivalent,
            "tests": []
        }
        print("error_json: ", error_json)
        print("response: ", json_str)
        return error_json
        #return None

def transform_to_json(input_dict):
    json_object = json.dumps(input_dict)
    return json_object

def remover_quebra_linha(string):
    padrao = re.compile(r'\n')
    return re.sub(padrao, '', string)

def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def write_responses_to_file(response, program_name):
    filename = f"{program_name}.json"
    file_exists = os.path.isfile(filename)

    with open(filename, "a") as file:
        if file_exists:
            # Remove o colchete de fechamento anterior
            file.seek(file.tell() - 1)
            file.truncate()

            # Adiciona uma vírgula para separar os objetos JSON
            file.write(",")

        else:
            file.write("[")

        json.dump(response, file, indent=2)

    # Adicione o colchete de fechamento no final do arquivo JSON
    with open(filename, "a") as file:
        file.write("]")



def analysis(json_file, equivalent_file, minimal_file, output_file):
    with open(json_file, 'r') as f1:
        dados1 = json.load(f1)

    with open(equivalent_file, 'r') as f2:
        dados2 = f2.read().split()
    
    with open(minimal_file, 'r') as f3:
        dados3 = f3.read().split()

    def extrair_numero_mutante(nome_arquivo):
        return int(nome_arquivo.split('_')[0].split('muta')[1])

    resultado = []

    for mutante1 in dados1:
        num_mutante1 = extrair_numero_mutante(mutante1['mutant_program'])
        equiv1 = mutante1['equivalent']
        if str(num_mutante1) in dados2:
            equiv2 = str(num_mutante1) in dados2
        elif str(num_mutante1) in dados3:
            equiv2 = False
        acertou_equiv = equiv1 == equiv2
        resultado.append([num_mutante1, equiv1, equiv2, acertou_equiv])

    with open(output_file, 'w') as f:
        for re in resultado:
            f.write(str(re) + '\n')