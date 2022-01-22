import binascii

def hb2i(hb):
    return int(hb, 16)

def i2hb(i):
    hx = hex(i)
    hxb = hx[2:]
    res = bytes(hxb, 'utf-8')
    return res

def txt_to_hex (txt):
    t = bytes(txt, 'utf-8')
    return binascii.hexlify(t)

def hex_to_txt (hexdata):
    x=binascii.unhexlify(hexdata)
    return str(x,'ascii')

#print(txt_to_hex("ABCDEFGHIJKLMNOP"))
#print(hex_to_txt(txt_to_hex("ABCDEFGHIJKLMNOP")))

#takes a hex value and returns binary
def hex_to_binary(hexi):
	return bin(int(str(hexi), 16))

def binary_to_hex(binary):
    hexed = hex(binary)[2:]
	#leading 0s get cut above, if not length 8 add a leading 0
    if len(hexed) != 8:
        hexed = '0' + hexed
    return hexed
  
def tuple_to_hextring(t):
    return ''.join(t)

def group(seq, n):
    return [seq[i:i+n] for i in range(0, len(seq), n)]
def hex_to_int(num):
    return int(num, base=16)

def txt_to_matrix(txt):
    a1= txt_to_hex(txt)
    a=hexint_to_hexstring(a1)[:-1]
    #print(a)
    #print(type(a))
    matrix = []
    ite = 2
    for i in range(4):
        tmp=[]
        for j in range(4):
            stm = bytes(a[ite-2:ite], 'utf-8')
            tmp.append(stm)
            ite+=2
        matrix.append(tmp)
    #print(matrix)
    te = []
    for i in range(4):
        te.append(list(matrix[i]))
    return te

def to_matrix(hexi):
    matrix = list(zip(*group(group(hexi, 2), 4)))
    te = []
    for i in range(4):
        te.append(list(matrix[i]))
    return te
#print(txt_to_matrix("193DE3BEA0F4E22B9AC68D2AE9F84808"))

def int_to_str(num):
    nchars = len(str(num))
    return ''.join(chr((num>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))

def matrix_to_txt (matrix):
    text = ''
    for j in range(4):
        for i in range(4):
            intt = hb2i(matrix[i][j])
            #print(intt)
            #print(type(matrix[i][j]))
            #print(chr(intt))
            text += chr(intt)
    #print(text)
    return text

def hexint_to_hexstring(hexi):
    #will skip the b' at the begining
    return str(hexi)[2:]
def hexstring_to_hexint(st):
    return hex(int(st, 16))

def chunk_to_16element_list(hexi):
    st = hexint_to_hexstring(hexi)
    li = []
    for i in range(0,32,2):
        li.append(st[i:i+2])
    return li
#print(hex_to_16element_list(txt_to_hex("0f1571c947d9e8590cb7add6af7f6798")))
#print(txt_to_matrix("ABCDEFGHIJKLMNOP"))
#print(matrix_to_txt(txt_to_matrix("ABCDEFGHIJKLMNOP")))
def hexstring_to_byte(hexi):
    int_val = int(hexi,0)
    str_val = str(int_val)
    byte_val = str_val.encode()
    return byte_val
    
    
#from https://www.tutorialspoint.com/hamming-distance-in-python#:~:text=The%20hamming%20distance%20is%20the,the%20Hamming%20distance%20is%201.
def hammingDistance(x, y):
      """
      :type x: int
      :type y: int
      :rtype: int
      """
      ans = 0
      for i in range(31,-1,-1):
         b1= x>>i&1
         b2 = y>>i&1
         ans+= not(b1==b2)
         #if not(b1==b2):
            # print(b1,b2,i)
      return ans
  
#print(hammingDistance(7,8))
#print(hammingDistance(3,7))


def read_from_file(pathf):
    f = open(pathf, "r")
    t=f.read()
    f.close()
    return t

def write_to_file(pathf,li):
    textfile = open(pathf, "w")
    for element in li:
        textfile.write(element)
    textfile.close()
    
    
def char_to_hex(ch):
    ch = ch.lower()
    int_val = ord(ch)-(ord('a')-1)
    return hex(int_val)

def write_to_file_cipher(li):
    textfile = open("files/ciphertxt.txt", "w")
    for p in li:
        te = ""
        for i in range(4):
            for j in range(4):
                print(p[i][j])
                intt = hb2i(p[i][j])
                te += chr(intt)
        textfile.write(te)
    textfile.close()

def reArrangeOutPut(txt):
    #print(txt)
    w1=""
    w2=""
    w3=""
    w4=""
    for i in range(0,16,4):
        w1+=txt[i+0]
        w2+=txt[i+1]
        w3+=txt[i+2]
        w4+=txt[i+3]
    te=w1+w2+w3+w4
    return te