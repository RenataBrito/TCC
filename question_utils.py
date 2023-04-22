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
        #Test to see the results
        #print(response.text)
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

def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def txt_to_json(txt_file, program_name):
    with open(txt_file, 'r') as f:
        data = f.read()

    dicts = [eval(line) for line in data.split('\n') if line]

    json_data = json.dumps(dicts)

    with open(f"{program_name}.json", 'w') as f:
        f.write(json_data)
    
    os.remove(txt_file)

def write_responses_to_file(responses, program_name):
    with open(f"{program_name}.txt", "w") as file:
        for response in responses:
            file.write(f"{response}\n")

def analysis(json_file, txt_file, output_file):
    with open(json_file, 'r') as f1:
        dados1 = json.load(f1)

    with open(txt_file, 'r') as f2:
        dados2 = f2.read().split()

    def extrair_numero_mutante(nome_arquivo):
        return int(nome_arquivo.split('_')[0].split('muta')[1])

    resultado = []

    for mutante1 in dados1:
        num_mutante1 = extrair_numero_mutante(mutante1['mutant_program'])
        equiv1 = mutante1['equivalent']
        equiv2 = str(num_mutante1) in dados2
        acertou_equiv = equiv1 == equiv2
        resultado.append([num_mutante1, equiv1, equiv2, acertou_equiv])

    with open(output_file, 'w') as f:
        for re in resultado:
            f.write(str(re) + '\n')