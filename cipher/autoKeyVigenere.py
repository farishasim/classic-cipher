from cipher.utilities import shiftAlphabet, formatInput, arrangeText

def autoKeyVigenereMain():
  p = formatInput(input("Input plainteks: "))
  k = formatInput(input("Input key: "))
  while (k == ""):
    print("You must input key.")
    k = formatInput(input("Input key: "))
  nk = len(k)

  c = ""
  i = 0
  for letter in p:
    if i >= nk:
      c += shiftAlphabet(letter, p[i - nk], '+')
    else:
      c += shiftAlphabet(letter, k[i], '+')
    i += 1

  d = ""
  i = 0
  for letter in c:
    if i >= nk:
      d += shiftAlphabet(letter, d[i - nk], '-')
    else:
      d += shiftAlphabet(letter, k[i], '-')
    i += 1

  print("Your plaintext: " + p)
  print("Your key: " + k)
  print("Your ciphertext: " + c)
  print("Decrypted ciphertext: " + d)

def autoKeyVigenereEncrypt(plaintext:str, keytext:str):
  plaintext = formatInput(plaintext)
  keytext = formatInput(keytext)
  nk = len(keytext)

  ciphertext = ""
  i = 0
  for letter in plaintext:
    if i >= nk:
      ciphertext += shiftAlphabet(letter, plaintext[i - nk], '+')
    else:
      ciphertext += shiftAlphabet(letter, keytext[i], '+')
    i += 1

  result = {
    "plaintext": plaintext,
    "keytext": keytext,
    "ciphertext": ciphertext,
    "ciphertext_spaced": arrangeText(ciphertext)
  }

  with open("./cipher/dump/auto-key-vigenere-cipher.txt", "w") as file:
    file.write(arrangeText(ciphertext))

  return result

def autoKeyVigenereDecrypt(ciphertext:str, keytext:str):
  ciphertext = formatInput(ciphertext)
  keytext = formatInput(keytext)
  nk = len(keytext)

  decryptedtext = ""
  i = 0
  for letter in ciphertext:
    if i >= nk:
      decryptedtext += shiftAlphabet(letter, decryptedtext[i - nk], '-')
    else:
      decryptedtext += shiftAlphabet(letter, keytext[i], '-')
    i += 1

  result = {
    "plaintext": decryptedtext,
    "keytext": keytext,
    "ciphertext": ciphertext
  }

  return result

def emptyResult():
  return {
    "plaintext": "",
    "ciphertext": "",
    "keytext": ""
  }

if __name__ == "__main__":
  autoKeyVigenereMain()