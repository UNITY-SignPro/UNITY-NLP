from eunjeon import Mecab

m = Mecab()
m.pos("안녕하세요")
# [('안녕', 'NNG'), ('하', 'XSV'), ('세요', 'EP+EF')]