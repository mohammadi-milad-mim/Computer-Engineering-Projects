import binascii
from cgitb import text
from weakref import WeakMethod
from OPERATIONS import RotWord, Sbox, SubWord, hexor, toRCON
from TXT_PROCESS import chunk_to_16element_list, hex_to_txt, hexstring_to_hexint, to_matrix, tuple_to_hextring, txt_to_matrix, txt_to_hex


def get_MASTER_KEY():
    f = open("files/MASTER_KEY.txt", "r")
    t = f.read()
    #print(t)
    f.close()
    return txt_to_hex(t)



#Ben Ryan
#AES Key Expansion
#Program uses provided key as input, outputs the corresponding keywords w0 - w43 as given in table to cmd

def keyExpansion(key):
	#prep w list to hold 44 tuples
	w = [()]*44
	#print(key)
	#fill out first 4 words based on the key
	for i in range(4):
		w[i] = (key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
		
	#fill out the rest based on previews words, rotword, subword and rcon values
	for i in range(4, 44):
		#get required previous keywords
		temp = w[i-1]
		word = w[i-4]

		#if multiple of 4 use rot, sub, rcon etc
		if i % 4 == 0:
			#print(temp)
			x = RotWord(temp)
			y = SubWord(x)
			rcon = toRCON(i)

			temp = hexor(y, hex(rcon)[2:]) 
			
		#creating strings of hex rather than tuple
		word = tuple_to_hextring(word)
		temp = tuple_to_hextring(temp)
		
		#xor the two hex values
		xord = hexor(word, temp)
		w[i] = (xord[:2], xord[2:4], xord[4:6], xord[6:8])
		

  
	return w

def words_to_keys(w):
    te = []
    #print(len(w))
    i=0
    while(i<len(w)):
        j=0
        tem2=""
        while(j<4):
            tem = w[j+i][0]+w[j+i][1]+w[j+i][2]+w[j+i][3]
            tem2 += tem
            j+=1
        i+=4
        mt = to_matrix(tem2)
        #print(mt)
        mt_byte = []
        for ii in range(4):
            tbyte = []
            for jj in range(4):
                tbyte.append(bytes(mt[ii][jj], 'utf-8'))
            mt_byte.append(tbyte)
        #print(mt_byte)
        te.append(mt_byte)
    return te




	
#takes from 1 to the end, adds on from the start to 1

#FOR TEST: used to display the keywords neatly in this form: w0 = 0f 15 71 c9 in the Keys File
def keysToFile(w):
	temp="\n\nKeys: \n"
	for i in range(len(w)):
		temp+=("w" + str(i)+" = "+w[i][0]+' '+w[i][1]+' '+w[i][2]+' '+w[i][3]+'\n')
	ftest = open("files/Keys.txt",'w')
	ftest.write(temp)
	ftest.close()



def genRoundsKeys():
    master_key = get_MASTER_KEY()
    #print(master_key)
    wordList = keyExpansion(chunk_to_16element_list(master_key))
    #print(wordList)
    keyList = words_to_keys(wordList)
    #print(keyList)
    keysToFile(wordList)
    return keyList
    
'''
def round_key_gen():
    round_keys = master_key
    for i in range(4, 4 * 11):
                round_keys.append([])
                if i % 4 == 0:
                    byte = round_keys[i - 4][0] ^ Sbox[int(round_keys[i - 1][1], base=16)] ^ Rcon[i / 4]
                    round_keys[i].append(byte)

                    for j in range(1, 4):
                        byte = round_keys[i - 4][j] ^ Sbox[int(round_keys[i - 1][(j + 1) % 4], base=16)]
                        round_keys[i].append(byte)
                else:
                    for j in range(4):
                        byte = round_keys[i - 4][j] ^ round_keys[i - 1][j]
                        round_keys[i].append(byte)
    print(round_keys)
    return round_keys

round_key_gen()

def main():
	#hardcoding input key for demonstration purposes, could be read in from user/program via cmd/gui etc.
	key = ["0f", "15", "71", "c9", "47", "d9", "e8", "59", "0c", "b7", "ad", "d6", "af", "7f", "67", "98"]

	#expand key
	w = keyExpansion(key)
	
	#display nicely
	print("Key provided: " + "".join(key))
	prettyPrint(w)
	

if __name__ == '__main__':
	main()
'''
 
 #https://github.com/benjimr/AES-Key-Expansion/blob/master/AESKeyExpansion.py#L3