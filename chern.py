import re, codecs

def draft(arr):
    out = []
    for i in arr:
        k = re.sub(u'Черновое', u'<correspDesc><correspAction type="draft">Черновое</correspAction></correspDesc>', i)
        out.append(k)
    return out

def not_sent(arr):
    out = []
    for i in arr:
        k = re.sub(u'Неотправленное', u'<correspDesc><correspAction type="notSent">Неотправленное</correspAction></correspDesc>', i)
        out.append(k)
    return out


