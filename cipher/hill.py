import numpy as np

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
    'J',
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

KEY = [
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19],
]

N = 26

def preprocess(text):
    # remove punctuation
    text = "".join(c for c in text if c not in ' ,.?!(){}')
    # to uppercase
    return text.upper()

def encrypt(plaintext, key):
    ciphertext = ""
    plaintext = preprocess(plaintext)
    keysize = len(key)
    plaintext += 'Z'*((3-(len(plaintext)%3))%3)
    p = 0
    n = len(plaintext)
    while p < n:
        c = [0 for _ in range(keysize)]
        for i in range(keysize):
            for j in range(keysize): 
                c[i] += (key[i][j] * ALFABET.index(plaintext[p+j]))
        for i in range(keysize):
            ciphertext += ALFABET[ c[i] % N ]
        p += 3
    return ciphertext

def reversekey(key):
    # asumsi key punya inverse
    rev = np.linalg.inv(key)
    det = np.linalg.det(key)
    inv = pow(int(round(det % N)), -1, N)
    size = len(key)
    for i in range(size):
        for j in range(size):
            key[i][j] = int(round(((rev[i][j] * det) * inv))) % N
    print(key)
    return key

def decrypt(ciphertext, key):
    ciphertext = preprocess(ciphertext)
    reversedkey = reversekey(key)
    return encrypt(ciphertext, reversedkey)

if __name__ == "__main__":
    choice = input()
    if choice == "c":
        plaintext = input("Masukkan plaintext: ")
        ciphertext = encrypt(plaintext, KEY)
        print(ciphertext)
    else :
        ciphertext = input("Masukkan ciphertext: ")
        plaintext = decrypt(ciphertext, KEY)
        # print(len(KEY))
        print(plaintext)