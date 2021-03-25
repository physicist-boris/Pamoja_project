import csv
import os

from wrapper_text import WrapperText


class WordsExtractor:

    def __init__(self, filename, output):
        self.filename = filename
        self.output = output

        self.csv_columns = ["Texte Origine", "mot", "phrase", "ID phrase", "PositionMot"]

    def extract(self) -> None:

        with open(self.filename, 'r', encoding='utf-8') as f:
            text = f.read()
        text_data = WrapperText(text).repertory_sentence

        with open(self.output, mode='w', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", lineterminator='\n')
            writer.writerow(self.csv_columns)

            for sentence_tuple in text_data:
                sentence, sentence_id = sentence_tuple
                if self.__sentence_is_valid(sentence):
                    for word_tuple in text_data[sentence_tuple]:
                        word, word_id = word_tuple
                        if self.__word_is_valid(word):
                            writer.writerow([os.path.basename(self.filename), word, sentence, sentence_id, word_id])

    @staticmethod
    def __word_is_valid(word: str) -> bool:
        return not not word

    @staticmethod
    def __sentence_is_valid(sentence: str) -> bool:
        return True

    @staticmethod
    def __document_is_valid(document) -> bool:
        return True


if __name__ == '__main__':
    WordsExtractor('data/file.txt', "output.csv").extract()
