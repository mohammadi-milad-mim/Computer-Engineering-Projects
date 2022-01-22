from AES_D import aes_d
from AES_E import aes_e
from CHUNK import chunking, len_of_padding, len_of_txt
from KEY_GENERATION import genRoundsKeys
from TXT_PROCESS import hex_to_txt, reArrangeOutPut, read_from_file, write_to_file, write_to_file_cipher

plain = read_from_file("files/plaintxt.txt")
plain_parts = chunking(plain)
len_padd = len_of_padding(len_of_txt(plain))
round_keys = genRoundsKeys()

cipher_parts = []
for i in plain_parts:
    cipher_parts.append(aes_e(i,round_keys))
    
#write cipher parts on cipher.txt  
#write_to_file_cipher(cipher_parts)

output_parts = []
for i in cipher_parts:
    output_parts.append(reArrangeOutPut(aes_d(i,round_keys)))


output_parts = removePadding(output_parts,len_padd)
write_to_file("files/output.txt",output_parts)
