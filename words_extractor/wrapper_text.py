import fr_core_news_sm


class WrapperText:

    def __init__(self, text):
        list_sentence = [sent.strip() for sent in text.split(".")]
        list_sentence_index = [(sentence, text.index(sentence)) for sentence in list_sentence]
        repertory_sentence = {}
        for sentence_index in list_sentence_index:
            repertory_sentence[sentence_index] = self.tokenise(sentence_index[0])
        self.repertory_sentence = repertory_sentence

    @staticmethod
    def tokenise(sentence):
        nlp = fr_core_news_sm.load()
        doc = nlp(sentence)
        extracted_word = [(token.text, token.idx) for token in doc if token.pos_ == "NOUN"]
        return extracted_word
