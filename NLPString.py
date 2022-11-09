from eunjeon import Mecab
import nltk
import json
# from WordManage import search_word
def search_word(word):
    return c.execute(f"SELECT * FROM word WHERE origin = '{word}'").fetchone()
# import mecab
mecab = Mecab()
# POS tag a sentence
sentence = input("문장 입력하시오:")
words = Mecab().pos(sentence)

verb_re, noun_re, js_verb, js_noun = [], [], [], []
nnp = []

grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
AP: {<VA.*>*}            # Adjective phrase
VX: {<VX.*>*}
VV: {<VV.*>*}         # Verb phrase
MP: {<M.*>*}
VC: {<VC*.*>*}
EC: {<EC.*>*}

"""
parser = nltk.RegexpParser(grammar)
for subtree in parser.parse(words).subtrees():
    if subtree.label() == 'NP':
        if list(subtree)[0][1] == 'NNP':
            nnp.append(list(subtree)[0][0])
        else:
            noun_re.append(list(subtree)[0][0])

    if list(subtree)[0][0][-1]=="다":
        if subtree.label() == 'VV':
           verb_re.append(list(subtree)[0][0])
        if subtree.label() == 'AP':
            verb_re.append(list(subtree)[0][0])
        if subtree.label() == 'VX':
            verb_re.append(list(subtree)[0][0])
    else:
        if subtree.label() == 'VV':
           verb_re.append(list(subtree)[0][0]+"다")
        if subtree.label() == 'AP':
            verb_re.append(list(subtree)[0][0]+"다")
        if subtree.label() == 'VX':
            verb_re.append(list(subtree)[0][0]+"다")
    if subtree.label() == 'MP':
        noun_re.append(list(subtree)[0][0])

print(nnp)
print(noun_re)
print(verb_re)


for i in verb_re:
    try:
        js_verb.append(search_word(i)[1])
    except:
        try:
            js_verb.append(search_word(i)[1])
        except:
            print(i + "없는단어입니다")
    # js_verb.append(search_word(i)[1])
for i in noun_re:
    try:
        js_noun.append(search_word(i)[1])
    except:
        try:
            js_verb.append(search_word(i)[1])
        except:
            print(i + "없는단어입니다")
json_object = \
    {
        "for_backend": {
            "nnp": nnp,
            "noun": js_noun,
            "verb": js_verb
        },
        "for_front": {
            "nnp": nnp,
            "noun": noun_re,
            "verb": verb_re
        }
    }
print(json_object)

with open('output.json', 'w') as f:
    json.dump(json_object, f, indent=2, ensure_ascii=False)
