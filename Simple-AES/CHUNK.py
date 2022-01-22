import math

def len_of_txt(stri):
    return len(stri)
    
def len_of_parts(len_txt):
    return math.ceil(len_txt/16)

def len_of_padding(len_txt):
    return (16-(len_txt%16))%16

def padding(stri,len_padding):
    for i in range (len_padding):
        stri+='.'
    return stri

def split_to_128bit(stri,len_txt):
    parts=[]
    for i in range (0,len_txt,16):
        parts.append(stri[i:i+16])
    return parts

def chunking(stri):
    len_txt = len_of_txt(stri)
    len_parts = len_of_parts(len_txt)
    len_padding=len_of_padding(len_txt)
    stri = padding(stri,len_padding)
    parts = split_to_128bit(stri,len_txt)
    return parts

def removePadding(li,len_padd):
    li[-1]=li[-1][:16-len_padd]
    return li

#print(split_to_128bit("i am millad and im writing a aes algohritm and i have so much fun"))
