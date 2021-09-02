from processor import shiftAlphabet, formatInput

def autoKeyVigenere():
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

if __name__ == "__main__":
  autoKeyVigenere()