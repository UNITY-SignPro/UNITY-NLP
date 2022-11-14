from eunjeon import Mecab
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Okt
from konlpy.tag import Kkma
import time
a=time.time()
mecab = Mecab()
print("mecab load")
print(time.time()-a)
a=time.time()
han=Hannanum()
print("Han load")
print(time.time()-a)
a=time.time()
okt=Okt()
print("okt load")
print(time.time()-a)
a=time.time()
kk=Kkma()
print("kkma load")
print(time.time()-a)
a=time.time()
kom=Komoran()
print("komoran load")
print(time.time()-a)

# POS tag a sentence
sentence = input("문장 입력하시오:")
a=time.time()
print("Han")
print(Hannanum().pos(sentence))
print(time.time()-a)
a=time.time()

print("kkma")
print(Kkma().pos(sentence))
print(time.time()-a)
a=time.time()

print("komoran")
print(Komoran().pos(sentence))
print(time.time()-a)
a=time.time()

print("OKT")
print(Okt().pos(sentence))
print(time.time()-a)
a=time.time()

print("mecab")
print(Mecab().pos(sentence))
print(time.time()-a)


