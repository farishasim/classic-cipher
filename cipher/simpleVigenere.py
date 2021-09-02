from processor import shiftAlphabet, formatInput

def simpleVigenere():
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

  # return c

if __name__ == "main":
  simpleVigenere()