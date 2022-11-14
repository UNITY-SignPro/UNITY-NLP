from eunjeon import Mecab
from konlpy.tag import Hannanum
from konlpy.utils import pprint
import nltk
import json
from WordManage import search_word
# import mecab
mecab = Mecab()
han = Hannanum()

# POS tag a sentence
sentence = input("문장 입력하시오:")
def NLP(sentence):
    words_han = Hannanum().pos(sentence)
    words = Mecab().pos(sentence)
    print(words)
    verb_re, noun_re, js_word, word_re, cant_word = [], [], [], [], []
    nnp = []

    for subtree in words:
        if subtree[1] == 'NNG' or subtree[1] == 'NP' or subtree[1] == 'NR' or subtree[1] == 'NNB':
            noun_re.append(list(subtree)[0])
            word_re.append(list(subtree)[0])
        if subtree[1] == 'NNP':
            nnp.append(list(subtree)[0])
            word_re.append(list(subtree)[0])


    for subtree in words_han:
        print(subtree)
        if subtree[1][0] == 'P':
            verb_re.append(list(subtree)[0]+"다")
            word_re.append(list(subtree)[0]+"다")









    for i in word_re:
        try:
            js_word.append(search_word(i)[1])
        except:
            cant_word.append(i)

    json_object = \
        {
            "for_backend": {
                "nnp": nnp,
                "word": js_word,
                "cant": cant_word
            },
            "for_front": {
                "nnp": nnp,
                "noun": noun_re,
                "verb": verb_re
            }
        }
    return json_object
print(NLP(sentence))
