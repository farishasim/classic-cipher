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
    # text = "".join(c for c in text if c not in ' ,.?!(){}')
    # to uppercase
    return text.upper()

def encrypt(plaintext, m, b):
    try: # cek apakah m relatif prima terhadap 26
        pow(m, -1, N);
    except ValueError:
        return "-1"
    ciphertext = ""
    plaintext = preprocess(plaintext)
    for p in plaintext:
        if ALFABET.count(p) != 0 :
            ciphertext += ALFABET[ (ALFABET.index(p)*m + b) % N ]
        else :
            ciphertext += p
    return ciphertext

def decrypt(ciphertext, m, b):
    try: # cek apakah m relatif prima terhadap 26
        dec = pow(m, -1, N);
    except ValueError:
        return "-1"
    plaintext = ""
    ciphertext = preprocess(ciphertext)
    for c in ciphertext:
        if ALFABET.count(c) != 0 :
            plaintext += ALFABET[ ((ALFABET.index(c)-b)*dec) % N ]
        else :
            plaintext += c
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
