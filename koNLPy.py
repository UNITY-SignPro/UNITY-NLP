from konlpy.tag import Mecab
from konlpy.utils import pprint


def NLP(input_text):
    kkma = Mecab()
    pprint(kkma.pos(input_text))

input_text= input("문장을 입력하시오:")
NLP(input_text)