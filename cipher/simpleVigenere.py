from processor import shiftAlphabet, formatInput

def simpleVigenereMain():
  p = formatInput(input("Input plainteks: "))
  k = formatInput(input("Input key: "))
  while (k == ""):
    print("You must input key.")
    k = formatInput(input("Input key: "))
  nk = len(k)

  c = ""
  i = 0
  for letter in p:
    c += shiftAlphabet(letter, k[i % nk], '+')
    i += 1

  d = ""
  i = 0
  for letter in c:
    d += shiftAlphabet(letter, k[i % nk], '-')
    i += 1

  print("Your plaintext: " + p)
  print("Your key: " + k)
  print("Your ciphertext: " + c)
  print("Decrypted ciphertext: " + d)

  # return {
  #   "plaintext": p,
  #   "key": k,
  #   "ciphertext": c,
  #   "decryptedtext": d
  # }

def simpleVigenereEncrypt(plaintext: str, keytext:str):
  plaintext = formatInput(plaintext)
  keytext = formatInput(keytext)
  nk = len(keytext)

  ciphertext = ""
  i = 0
  for letter in plaintext:
    ciphertext += shiftAlphabet(letter, keytext[i % nk], '+')
    i += 1
  
  return ciphertext

def simpleVigenereDecrypt(ciphertext: str, keytext:str):
  ciphertext = formatInput(ciphertext)
  keytext = formatInput(keytext)
  nk = len(keytext)

  decryptedtext = ""
  i = 0
  for letter in ciphertext:
    decryptedtext += shiftAlphabet(letter, keytext[i % nk], '-')
    i += 1
  
  return decryptedtext

if __name__ == "__main__":
  simpleVigenereMain()