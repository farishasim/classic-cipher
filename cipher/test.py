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