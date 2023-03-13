from nltk.corpus import wordnet
from deep_translator import GoogleTranslator


def syn_func(word):
    synonyms = []
    word = GoogleTranslator(source='ru', target='en').translate(word)
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())

    rusynonyms = []

    for synonym in synonyms:
        if synonym.isalpha():
            rusynonyms.append(GoogleTranslator(source='en', target='ru').translate(synonym))

    return list(set((rusynonyms)))
print(syn_func('имя'))

"""
функция для получения списка синонимов/ассоциаиций для слова
"""