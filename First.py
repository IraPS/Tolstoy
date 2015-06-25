#  -*- coding: utf-8 -*-
#from main import main
import re, codecs
to_read = 'Volume_66.txt'
to_write = '66_tagged.txt'
text_r = codecs.open(to_read, 'r', 'utf-8')
text_w = codecs.open(to_write, 'w', 'utf-8')
t = text_r.read()

global arr
arr = []

def publ(text):

    text = re.sub(u'(Впервые опубликовано.*?\.)( [А-Я])', '<publicationStmt>' + '\\1'
                  + '</publicationStmt>' + '\\2', text)
    text = re.sub(u'(Печатается по.*?[А-Я]\. [А-Я]\..*?\.)( [А-Я])', '<publicationStmt>' + '\\1'
                  + '</publicationStmt>' + '\\2', text)
    text = re.sub(u'(Печатается по.*?копии.*?\.)([А-Яа-яё])', '<publicationStmt>' + '\\1'
                  + '</publicationStmt>' + '\\2', text)
    text1 = text
    # text_w.write(text)
    return text1



def prev(text):

    text = re.sub(u'(Ответ на.*?письм.*?\.)(\s*\<\/p)', '<correspDesc><correspContext><reftype="prev">'+ '\\1'
                  + '</ref></correspContext></correspDesc>' + '\\2', text)
    text2 = text
    return text2


def adr(text):
    text = re.sub(u'(<head rend=".+">\r\n\s*<hi>)((.*?)([0-9]+\.?))(.*?)(</hi>.*?\r\n\s*</head>)',
                  '\\1\\2<persName role="addressee" type="person">\\5</persName>\\6', text)
    text3 = text
    return text3


def salute_beg(text):
    text = re.sub(u'(<p rend="Obrashenie.*? left">\r\n)(.*?)(\s*</p>)', u'\\1<salute>\\2</salute>\\3', text)
    text4 = text
    return text4


def salute_end(text):
    text = re.sub(u'(<p rend="right">)([^0-9]*?)(</p>)', u'\\1<signedt>\\2</signedt>\\3', text)
    text5 = text
    return text5

def izum(text):
    arr = []
    signedmark = re.findall(u'<salute>s*(.*?)</salute>', text, flags=re.U)
    print type(signedmark), len(signedmark)
    for q in signedmark:
        arr.append(q)
    print len(signedmark)
    for q1 in arr:
        print q1




def ref1(text):
    text = re.sub(u'(См\..*? т\. )([0-9]*)(, ?(\r\n\s*)? ?стр\. )([0-9]+)(\.)',
               u'<ref target=\"v\\2 p\\5\">\\1\\2\\3\\5\\6</ref>', text)
    text6 = text
    return text6


def ref2(text):
    text = re.sub(u'(См\..*? т\. )([0-9]*)(, ?(\r\n\s*)? ?стр\. )([0-9]+\—[0-9]+)(\.)',
                  u'<ref target=\"v\\2 pp\\5\">\\1\\2\\3\\5\\6</ref>', text)
    text7 = text
    return text7



#print arr

#text_w.write(salute_end(t))

t1 = (ref2(ref1(salute_end(salute_beg(adr(publ(prev(t))))))))
text_w.write(t1)

# print izum(t1)


#text_w.write(ref2(t))

text_r.close()
text_w.close()


