#  -*- coding: utf-8 -*-
import re, codecs

def na_konverte(arr):
    out = []
    i = 0
    while i != len(arr):        
        k = re.sub(u'<hi>На конверте:(.*)</hi>', u'<hi>На конверте:\\1</hi><facsimile><surface type="envelope">', arr[i])
        out.append(k)
        if k != arr[i]:
            m = i + 1
            while m != len(arr):
                if '<p rend="Textpetit_otstup left">' in arr[m]:
                    z = re.sub(u'<p rend="Textpetit_otstup left">', u'</surface></facsimile><p rend="Textpetit_otstup left">', arr[m])
                    out.append(z)
                    i = m
                    break
                out.append(arr[m])
                m += 1
        i += 1
    return out

def na_obor(arr):
    out = []
    i = 0
    while i != len(arr):        
        k = re.sub(u'<hi>На обороте:(.*)</hi>', u'<hi>На обороте:\\1</hi><facsimile><surface type="turn">', arr[i])
        out.append(k)
        if k != arr[i]:
            m = i + 1
            while m != len(arr):
                if '<p rend="Textpetit_otstup left">' in arr[m]:
                    z = re.sub(u'<p rend="Textpetit_otstup left">', u'</surface></facsimile><p rend="Textpetit_otstup left">', arr[m])
                    out.append(z)
                    i = m
                    break
                out.append(arr[m])
                m += 1
        i += 1
    return out



