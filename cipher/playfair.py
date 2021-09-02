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

def e_bigram(p1,p2,mat):
    # encrypt bigram
    i1, j1 = getIdx(mat,p1)
    i2, j2 = getIdx(mat,p2)

    if (i1 == i2):
        return mat[i1][(j1+1) % KEYSIZE], mat[i1][(j2+1) % KEYSIZE]
    elif j1 == j2:
        return mat[(i1+1) % KEYSIZE][j1], mat[(i2+1) % KEYSIZE][j1]
    
    return mat[i1][j2], mat[i2][j1]

def d_bigram(p1,p2,mat):
    # decrypt bigram
    i1, j1 = getIdx(mat,p1)
    i2, j2 = getIdx(mat,p2)

    if (i1 == i2):
        return mat[i1][(j1-1) % KEYSIZE], mat[i1][(j2-1) % KEYSIZE]
    elif j1 == j2:
        return mat[(i1-1) % KEYSIZE][j1], mat[(i2-1) % KEYSIZE][j1]
    
    return mat[i1][j2], mat[i2][j1]

def encrypt(plaintext:str, key:str):

    ciphertext = ""

    # strip all blanks, j, J an punctuation.
    plaintext = "".join(c for c in plaintext if c not in ' ,.?!(){}')
    key = "".join(c for c in key if c not in ' ,.?!(){}jJ')
    
    # to uppercase
    plaintext = plaintext.upper()
    plaintext = plaintext.replace('J', 'I')
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

    i = 0
    n = len(plaintext)
    while i < n:
        if i+1 < n:
            if plaintext[i] == plaintext[i+1]:
                plaintext = plaintext[:i+1] + 'X' + plaintext[i+1:]
                n += 1
        else: 
            # akhir ganjil
            plaintext += 'X'
        
        c1, c2 = e_bigram(plaintext[i], plaintext[i+1], mat)

        ciphertext += c1 + c2

        i += 2

    return ciphertext


def decrypt(ciphertext, key):

    plaintext = ""

    # strip all blanks, j, J an punctuation.
    ciphertext = "".join(c for c in ciphertext if c not in ' ,.?!(){}')
    key = "".join(c for c in key if c not in ' ,.?!(){}jJ')
    
    # to uppercase
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace('J', 'I')
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

    i = 0
    n = len(ciphertext)
    while i < n:
        if i+1 < n:
            if ciphertext[i] == ciphertext[i+1]:
                ciphertext = ciphertext[:i+1] + 'X' + ciphertext[i+1:]
                n += 1
        else: 
            # akhir ganjil
            ciphertext += 'X'
        
        c1, c2 = d_bigram(ciphertext[i], ciphertext[i+1], mat)

        plaintext += c1 + c2

        i += 2

    return plaintext

if __name__ == "__main__":

    choice = input()

    if choice == "c":

        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan key: ")

        ciphertext = encrypt(plaintext, key)

        print(ciphertext)

    else :
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan key: ")

        plaintext = decrypt(ciphertext, key)

        print(plaintext)
