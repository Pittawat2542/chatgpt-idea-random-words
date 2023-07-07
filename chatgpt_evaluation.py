import os
import json
from pathlib import Path

import openai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

EVALUATION_MODEL = 'gpt-3.5-turbo'

INPUT_FILE_PATH = Path('data/exported_results.json')
RESULT_FILE_PATH = Path(f'data/{EVALUATION_MODEL}_evaluation_results.json')


def main():
    with open(INPUT_FILE_PATH, 'r') as exported_results_file:
        exported_results = json.load(exported_results_file)

    for problem in exported_results['problems']:
        prompt = f"""Please select the set of ideas from each pair that you believe are more innovative for a problem. Please make sure to format your output as a code block using triple backticks (```json and ```).
Problem: {problem['problem']['text']}

Set of ideas:
A:
{problem['standard']}

B:
{problem['random']}

Output format:
```json
{{
    "problem": "{problem['problem']['text']}",
    "selected_set": "A" or "B"
}}
```"""
        
        chat_completion = openai.ChatCompletion.create(model=EVALUATION_MODEL,
                                                       messages=[{"role": "user", "content": prompt}, ],
                                                       temperature=0)
    
        response = chat_completion.choices[0].message.content
        content = response.split('```json')[1].split('```')[0]
        
        
        if not os.path.exists(RESULT_FILE_PATH):
            with open(RESULT_FILE_PATH, 'w') as eval_result_file:
                eval_result_file.write('{"results": []}')

        with open(RESULT_FILE_PATH, 'r+') as eval_result_file:
            result = json.load(eval_result_file)
            
            result['results'].append({'problem': problem['problem']['text'], 'result': 'standard' if json.loads(content)['selected_set'] == 'A' else 'random'})

            eval_result_file.seek(0)
            eval_result_file.write(json.dumps(result, indent=4))
    
if __name__ == '__main__':
  main()