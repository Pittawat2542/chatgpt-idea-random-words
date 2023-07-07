from pathlib import Path

import json

PROBLEMS_FILE_PATH = Path('data/problems.json')
RESULT_FILE_PATH = Path('data/results.json')
SURVEY_DATA_FILE_PATH = Path('data/survey_data.txt')
EXPORTED_RESULTS_FILE_PATH = Path('data/exported_results.json')


def main():
    with open(PROBLEMS_FILE_PATH, 'r') as problems_file, open(RESULT_FILE_PATH, 'r') as results_file, open(SURVEY_DATA_FILE_PATH, 'w') as survey_file, open(EXPORTED_RESULTS_FILE_PATH, 'w') as exported_results_file:
        problems = json.load(problems_file)['problems']
        results = json.load(results_file)

        json_result = {'problems': []}

        for problem in problems:
            standard_result = [result for result in results['standard'] if result['problem']['id'] == problem['id']]
            random_result = [result for result in results['random'] if result['problem']['id'] == problem['id']]
                        
            standard_str = ''
            for idx, idea in enumerate(standard_result[0]['ideas']):
                standard_str += f'{idx + 1}. {idea["title"]}: {idea["description"]}\n'
                        
            random_str = ''
            for idx, idea in enumerate(random_result[0]['ideas']):
                random_str += f'{idx + 1}. {idea["title"]}: {idea["description"]}\n'
                        
            survey_file.write(f'Problem: {problem["text"]}\n')
            survey_file.write('Standard:\n')
            survey_file.write(standard_str)
            survey_file.write('Random:\n')
            survey_file.write(random_str)
            survey_file.write('---\n')

            json_result['problems'].append({'problem': problem, 'standard': standard_str, 'random': random_str})
                        
            print(problem['text'])
            print('---')

        exported_results_file.write(json.dumps(json_result, indent=4))



if __name__ == '__main__':
    main()
