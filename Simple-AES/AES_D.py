from OPERATIONS import add_round_key, inv_mix_columns, inv_shift_rows, inv_sub_bytes
from TXT_PROCESS import matrix_to_txt, txt_to_matrix


def round_decrypt(state_matrix, key_matrix):
    add_round_key(state_matrix, key_matrix)
    inv_mix_columns(state_matrix)
    inv_shift_rows(state_matrix)
    inv_sub_bytes(state_matrix)
    
def aes_d(ciphertext,round_keys):
    #print(ciphertext)
    cipher_state = ciphertext
    add_round_key(cipher_state, round_keys[10])
    inv_shift_rows(cipher_state)
    inv_sub_bytes(cipher_state)

    for i in range(9, 0, -1):
        round_decrypt(cipher_state, round_keys[i])

    add_round_key(cipher_state,round_keys[0])
    return matrix_to_txt(cipher_state)