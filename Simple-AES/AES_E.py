from pydoc import plain
from OPERATIONS import add_round_key, mix_columns, shift_rows, sub_bytes
from TXT_PROCESS import matrix_to_txt, txt_to_matrix

def round_encrypt(state_matrix, key_matrix):
        sub_bytes(state_matrix)
        shift_rows(state_matrix)
        mix_columns(state_matrix)
        add_round_key(state_matrix, key_matrix)
        
def aes_e(stri,round_keys):
    plain_state = txt_to_matrix(stri)
    #print(0,"     :",plain_state)
    add_round_key(plain_state,round_keys[0])
    #print(1,"     :",plain_state)
    for i in range(1, 10):
        round_encrypt(plain_state, round_keys[i])
        #print(i+1,"     :",plain_state)
    sub_bytes(plain_state)
    shift_rows(plain_state)
    add_round_key(plain_state, round_keys[10])
    #print(12,"     :",plain_state)
    return plain_state