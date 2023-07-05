import json


def main():
    with open('data/problems.json', 'r') as problems_file:
        with open('data/results.json', 'r') as results_file:
            with open('data/survey_data.txt', 'w') as survey_file:
                problems = json.load(problems_file)['problems']
                results = json.load(results_file)

                for problem in problems:
                    standard_result = [result for result in results['standard'] if
                                       result['problem']['id'] == problem['id']]
                    random_result = [result for result in results['random'] if result['problem']['id'] == problem['id']]
                    survey_file.write(f'Problem: {problem["text"]}\n')
                    survey_file.write('Standard:\n')
                    for idx, idea in enumerate(standard_result[0]['ideas']):
                        survey_file.write(f'{idx + 1}. {idea["title"]}: {idea["description"]}')
                        survey_file.write('\n')
                    survey_file.write(f'Random:\n')
                    for idx, idea in enumerate(random_result[0]['ideas']):
                        survey_file.write(f'{idx + 1}. {idea["title"]}: {idea["description"]}')
                        survey_file.write('\n')
                    survey_file.write('---\n')
                    print(standard_result)
                    print(random_result)
                    print('---')


if __name__ == '__main__':
    main()
