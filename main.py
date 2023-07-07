import os
import json
import random
import time
from pathlib import Path

import openai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY


PROBLEMS_FILE_PATH = Path('data/problems.json')
COMMON_WORDS_FILE_PATH = Path('data/google-10000-english-no-swears-no-stopwords.txt')
RESULT_FILE_PATH = Path('data/results.json')


def data_generation(target_problem, concepts=[]):
    problem = target_problem['text'].lower()
    prompt = f'''Give me a list of 5 ideas to solve the following problem. Please make sure to format your output as a code block using triple backticks (```json and ```).
Problem: {problem}

Output format:
```json
{{
    "ideas": [{{"id": number, "title": idea name, "description": brief idea description, "reason": reason, "pros": [<text>], "cons": [<text>]}}]
}}
```'''

    if len(concepts) > 0:
        concepts_str = ', '.join(concepts[:-1]) + ', ' + concepts[-1] if len(concepts) > 1 else concepts[0]

        prompt = f'''Give me a list of 5 ideas to solve the following problem. Please make sure to format your output as a code block using triple backticks (```json and ```).
In the "Inner thought" process, it is important to explore new ideas and think outside the box. One way to do this is by incorporating concepts from the "Concepts" section and establishing connections between them. By reusing concepts and using multiple concepts per idea, creativity can flourish. Although ideas may seem unconventional or out of this world, it is still valuable to consider them. To ensure practicality, reasons for the ideas should be provided, and existing ideas can be combined in unique ways to experiment. While immediate applicability is not necessary, it is crucial to ensure that the ideas can eventually be put into practice. Finally, the outputted ideas should be in JSON format.

Problem: {problem}

Concepts: {concepts_str}

Output format:
```json
{{
    "ideas": [{{"id": number, "title": idea name, "description": brief idea description, "concepts": [<text>], "reason": reason, "pros": [<text>], "cons": [<text>]}}]
}}
```'''

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": prompt}, ],
                                                   temperature=0)

    response = chat_completion.choices[0].message.content
    content = response.split('```json')[1].split('```')[0]

    if not os.path.exists(RESULT_FILE_PATH):
        with open(RESULT_FILE_PATH, 'w') as result_file:
            result_file.write('{"standard": [], "random": []}')

    with open(RESULT_FILE_PATH, 'r+') as result_file:
        result = json.load(result_file)
        if len(concepts) > 0:
            result['random'].append({'problem': target_problem, 'concepts': concepts, 'ideas': json.loads(content)['ideas']})
        else:
            result['standard'].append({'problem': target_problem, 'ideas': json.loads(content)['ideas']})

        result_file.seek(0)
        result_file.write(json.dumps(result, indent=4))


def main():
    with open(PROBLEMS_FILE_PATH, 'r') as problems_file:
        with open(COMMON_WORDS_FILE_PATH, 'r') as words_file:
            words = words_file.read().splitlines()
            concepts = random.choices(words, k=10)
            problems = json.load(problems_file)['problems']

            for problem in problems:
                print(f"current: {problem['text']}")
                data_generation(problem)
                time.sleep(5)
                data_generation(problem, concepts)
                time.sleep(5)


if __name__ == '__main__':
    main()
