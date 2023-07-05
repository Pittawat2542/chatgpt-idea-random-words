import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def main():
    with open('data/google-10000-english-no-swears.txt', 'r') as f:
        with open('data/google-10000-english-no-swears-no-stopwords.txt', 'w') as f2:
            for line in f:
                if line.strip() not in stop_words and len(line.strip()) > 2:
                    f2.write(line)


if __name__ == '__main__':
    main()