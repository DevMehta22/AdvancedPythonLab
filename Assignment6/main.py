from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class FileNotFoundError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self):
        return f"File not found: {self.message}"


class InvalidInputDataError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self):
        return f"Invalid input data: {self.message}"


class DiskSpaceFullError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self):
        return f"Disk space full: {self.message}"


def read_input_data(input_file):
    try:
        with open(input_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Invalid file path or file not found")


def process_text_data(data: str):
    try:
        words = data.split()
        count = 0
        word_count = defaultdict(int)
        for word in words:
            if not word.isalpha():
                continue

            word_count[word] += 1
            count += 1
        return word_count, count
    except ValueError:
        raise InvalidInputDataError("Invalid input data")


def store_processed_results(output_file, results, count):
    try:
        with open(output_file, "w") as file:
            file.write(f"Total words: {count}\n")
            for word, count in results.items():
                file.write(f"{word}: {count}\n")
    except OSError:
        raise DiskSpaceFullError("Insufficient disk space to write output file")


def build_word_cloud(frequency):
    comment_words = ""

    for word, count in frequency.items():
        comment_words += (word + " ") * count

    wordcloud = WordCloud(width=600,height=600,background_color="black",min_font_size=8,stopwords=set()).generate(comment_words)

    plt.figure(figsize=(6, 6), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


print("Name: Dev Mehta\nRoll No: 22BCP282")

input_file = 'dev.txt'

data = read_input_data(input_file)

words, count = process_text_data(data)

output_file = 'result.txt'
store_processed_results(output_file, words, count)
build_word_cloud(words)
print("Text processing completed successfully!")