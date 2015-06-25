import codecs
from na_konv import na_konverte, na_obor
from chern import draft, not_sent

def main(text):
    text_arr = []
    f = codecs.open(text, 'r', 'utf-8')
    for line in f:
        text_arr.append(line)
    out = codecs.open('out_66.txt', 'w', 'utf-8')
    for i in na_konverte(na_obor(draft(not_sent(text_arr)))):
        out.write(i)
    out.close()
    return out
    
main('66_tagged.txt')
