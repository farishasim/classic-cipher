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
N = 26

def preprocess(text):
    # remove punctuation
    text = "".join(c for c in text if c not in ' ,.?!(){}')
    # to uppercase
    return text.upper()

def encrypt(plaintext, m, b):
    ciphertext = ""
    plaintext = preprocess(plaintext)
    for p in plaintext:
        ciphertext += ALFABET[ (ALFABET.index(p)*m + b) % N ]
    return ciphertext

def decrypt(ciphertext, m, b):
    plaintext = ""
    ciphertext = preprocess(ciphertext)
    dec = pow(m, -1, N)
    for c in ciphertext:
        plaintext += ALFABET[ ((ALFABET.index(c)-10)*dec) % N ]
    return plaintext

if __name__ == "__main__":
    choice = input()
    if choice == "c":
        plaintext = input("Masukkan plaintext: ")
        m = int(input("Masukkan key m: "))
        b = int(input("Masukkan key b: "))
        ciphertext = encrypt(plaintext, m, b)
        print(ciphertext)
    else :
        ciphertext = input("Masukkan ciphertext: ")
        m = int(input("Masukkan key m: "))
        b = int(input("Masukkan key b: "))
        plaintext = decrypt(ciphertext, m, b)
        print(plaintext)
