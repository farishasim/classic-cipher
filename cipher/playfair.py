ALFABET = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]
KEYSIZE = 5;

def getIdx(mat, c):
    for i in range(KEYSIZE):
        for j in range(KEYSIZE):
            if mat[i][j] == c:
                return i,j
    return -1,-1

def encrypt(plaintext:str, key:str):

    # strip all blanks, j, J an punctuation.
    plaintext = "".join(c for c in plaintext if c not in ' ,.?!(){}jJ')
    key = "".join(c for c in key if c not in ' ,.?!(){}jJ')
    
    # to uppercase
    plaintext = plaintext.upper()
    key = key.upper()

    # create key matrix
    # remove multiple occurences
    newkey = ""
    for c in key:
        if c not in newkey:
            newkey += c
    key = newkey

    # add all remaining alfabet
    for c in ALFABET:
        if c not in key:
            key += c

    mat = [[key[KEYSIZE*i+j] for j in range(KEYSIZE)] for i in range(KEYSIZE)]

    ciphertext = plaintext + " " + key

    return ciphertext























def decrypt(ciphertext, key):

    plaintext = ciphertext

    return plaintext

if __name__ == "__main__":
    plaintext = input("Masukkan plaintext: ")
    key = input("Masukkan key: ")

    ciphertext = encrypt(plaintext, key)

    print(ciphertext)