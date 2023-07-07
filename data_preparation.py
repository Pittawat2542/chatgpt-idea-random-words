from pathlib import Path

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

INPUT_FILE_PATH = Path('data/google-10000-english-no-swears.txt')
OUTPUT_FILE_PATH = Path('data/google-10000-english-no-swears-no-stopwords.txt')

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        with open(OUTPUT_FILE_PATH, 'w') as f2:
            for line in f:
                if line.strip() not in stop_words and len(line.strip()) > 2:
                    f2.write(line)


if __name__ == '__main__':
    main()