from eunjeon import Mecab
from konlpy.tag import Hannanum
from konlpy.utils import pprint
import nltk
import json
from WordManage import search_word
# import mecab
mecab = Mecab()
han=Hannanum()
# POS tag a sentence
sentence = input("문장 입력하시오:")
def NLP(sentence):
    words = Hannanum().pos(sentence)
    print(words)
    verb_re, noun_re, js_word, word_re, cant_word = [], [], [], [], []
    nnp = []

    grammar = """
    N: {<N.*>*<Suffix>?}   # Noun phrase
    P: {<P.*>*}         # Verb phrase
    J: {<J.*>*}
    V: {<V*.*>*}
    E: {<E.*>*}

    """

    parser = nltk.RegexpParser(grammar)

    chunks = parser.parse(words)
    print(chunks.pprint())
    for subtree in parser.parse(words).subtrees():
      if subtree.label() == 'N':
            if list(subtree)[0][1] == 'NNP':
                nnp.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
            else:
                noun_re.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
      if list(subtree)[0][0][-1]=="다"or list(subtree)[0][0][-1]=="요":
            if subtree.label() == 'P':
                verb_re.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
      else:
            if subtree.label() == 'P':
                verb_re.append(list(subtree)[0][0]+"다")
                word_re.append(list(subtree)[0][0] + "다")





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
    return(json_object)
print(NLP(sentence))


