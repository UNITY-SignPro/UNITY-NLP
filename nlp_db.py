from eunjeon import Mecab
import pandas as pd
import numpy as np
import re
import nltk
import json
import sqlite3

conn = sqlite3.connect('word.db')
excel_sheet_1 = pd.read_csv('인간.csv')

c = conn.cursor()  # 커서 생성

c.execute('''CREATE TABLE IF NOT EXISTS word
            (origin text, rename text)''')



excel_sheet_1=list(np.array(excel_sheet_1.values.tolist()))


def formmating(word):
    return re.sub(pattern=r'\([^)]*\)', repl='', string= word).strip()

for origin, rename in iter(excel_sheet_1):

    c.execute("INSERT INTO word VALUES(?,?);", (formmating(origin), formmating(rename)))

conn.commit()


mecab = Mecab()



def chan(word):
    a=c.execute(f"SELECT * FROM word WHERE origin = '{word}'").fetchone()
    print(">>>", a)
    # a=list(a)
    return a




# POS tag a sentence
sentence= input("문장 입력하시오:")
words = Mecab().pos(sentence)
outplist= ""
verb=""
noun=""

verb_re=[]
noun_re=[]
js_verb=[]
js_noun=[]
# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VV: {<V.*>*}            # Verb phrase
AP: {<VA.*>*}            # Adjective phrase
MP: {<M.*>*}
EC: {<EC.*>*}
"""
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(words)
print("# Print whole tree")

print(chunks.pprint())


for subtree in chunks.subtrees():
    if subtree.label()=='NP':
        noun=' '.join((e[0] for e in list(subtree)))
        noun_re.append(noun)
    if  subtree.label()=='VV':
        verb=' '.join((e[0] for e in list(subtree)))+"다"
        verb_re.append(verb)
    if  subtree.label()=='AP':
        verb=' '.join((e[0] for e in list(subtree)))+"다"
        verb_re.append(verb)
    if  subtree.label()=='MP':
        noun=' '.join((e[0] for e in list(subtree)))
        noun_re.append(noun)

for i in verb_re:

  js_verb.append(chan(i)[1])


for i in noun_re:
  js_noun.append(chan(i)[1])
json_object = { "word_chan":[{
    "noun": js_noun,
    "verb": js_verb
}], "word_ori":[{
    "noun": noun_re,
    "verb": verb_re
}]
}

with open('output.json', 'w') as f:
    json.dump(json_object, f, indent=2)
