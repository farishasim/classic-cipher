from cipher.utilities import charToInt, intToChar, formatInput, arrangeText
from random import shuffle

# key table
table = list()

def fullVigenere():
  p = formatInput(input("Input plainteks: "))
  k = formatInput(input("Input key: "))
  while (k == ""):
    print("You must input key.")
    k = formatInput(input("Input key: "))
  nk = len(k)

  # !Table is now a global variable!
  # table = [[intToChar(j) for j in range(26)] for i in range(26)]
  # for r in table:
  #   shuffle(r)
  # print("Key is randomly generated.")
  
  c = ""
  i = 0
  for letter in p:
    i_col = charToInt(letter)
    i_row = charToInt(k[i % nk])
    c += table[i_row][i_col] # stil at question
    i += 1

  d = ""
  i = 0
  for letter in c:
    i_col = charToInt(letter)
    i_row = charToInt(k[i % nk])
    
    row = table[i_row]
    j = 0
    for letter_row in row:
      if letter_row == letter:
        d += intToChar(j)  # stil at question
        break
      j += 1
    
    i += 1
  
  print("Your plaintext: " + p)
  print("Your key: " + k)
  print("Your ciphertext: " + c)
  print("Decrypted ciphertext: " + d)

def fullVigenereEncrypt(plaintext:str, keytext:str):
  getTable()
  plaintext = formatInput(plaintext)
  keytext = formatInput(keytext)
  nk = len(keytext)

  ciphertext = ""
  i = 0
  for letter in plaintext:
    i_col = charToInt(letter)
    i_row = charToInt(keytext[i % nk])
    ciphertext += table[i_row][i_col] # stil at question
    i += 1

  result = {
    "plaintext": plaintext,
    "keytext": keytext,
    "ciphertext": ciphertext,
    "ciphertext_spaced": arrangeText(ciphertext)
  }

  with open("./cipher/dump/full-vigenere-cipher.txt", "w") as file:
    file.write(arrangeText(ciphertext))
  
  return result

def fullVigenereDecrypt(ciphertext:str, keytext:str):
  getTable()
  ciphertext = formatInput(ciphertext)
  keytext = formatInput(keytext)
  nk = len(keytext)

  decryptedtext = ""
  i = 0
  for letter in ciphertext:
    i_col = charToInt(letter)
    i_row = charToInt(keytext[i % nk])
    
    row = table[i_row]
    j = 0
    for letter_row in row:
      if letter_row == letter:
        decryptedtext += intToChar(j)  # stil at question
        break
      j += 1
    
    i += 1

  result = {
    "plaintext": decryptedtext,
    "keytext": keytext,
    "ciphertext": ciphertext
  }
  
  return result

def generateTable():
  # writes to fullVigenereTable.txt a new randomly generated key table
  table = [[intToChar(j) for j in range(26)] for i in range(26)]
  for r in table:
    shuffle(r)
  print("    Key is randomly generated.")

  pList = ["table = [\n"]
  for row in table:
    temp = "\t["
    for letter in row:
      temp += f"\'{letter}\', "
    temp += "]\n"
    pList.append(temp)
  pList.append("]\n")

  with open("cipher/dump/fullVigenereTable.txt", "w") as file:
    file.writelines(pList)

def getTable():
  # read table from fullVigenereTable.txt and modify the table variable
  global table
  table = []

  with open("cipher/dump/fullVigenereTable.txt", "r") as file:
    text = file.readlines()

    for row in text[1: len(text)-1]:
      row = row.replace("[", "").replace("]", "")
      row = row[2:-4].replace("\', \'", ",")
      temp = list()
      for letter in row.split(","):
        temp.append(letter)
      table.append(temp)

def showTable():
  # printout key table to commandLine(sementara ini)
  # format:
  #   A B C D E ...
  # A X D A S C
  # B L P O M D
  # ...

  # update table value
  getTable()

  result = list()

  # first line
  temp = [' ']
  for i in range(26):
    temp.append(intToChar(i))
  result.append(temp)
  
  # next lines
  for i in range(26):
    temp = []
    temp.append(intToChar(i))
    for j in range(26):
      temp.append(table[i][j])
    result.append(temp)
  
  return result

# ! text based !
def showTableText():
  # printout key table to commandLine(sementara ini)
  # format:
  #   A B C D E ...
  # A X D A S C
  # B L P O M D
  # ...

  # update table value
  getTable()

  result = "\t  "

  # first line
  for i in range(26):
    result += intToChar(i) + " "
  result += "\n"
  
  # next lines
  for i in range(26):
    result += "\t" + intToChar(i) + " "
    for j in range(26):
      result += table[i][j] + " "
    result += "\n"
  
  return result

# ! text based !
def fullVigenereMain():
  promptMode = False
  while not promptMode:
    print("    ? ? ? ? ?")
    print("    Do you want to generate new key?")
    print("    1. Show current key")
    print("    2. Generate new key")
    print("    3. Nope, continue")
    submenu = input("    >>> ")

    if submenu == "1":
      print(showTableText())
    elif submenu == "2":
      generateTable()
    elif submenu == "3":
      fullVigenere()
    else:
      promptMode = True

def emptyResult():
  return {
    "plaintext": "",
    "ciphertext": "",
    "keytext": ""
  }

if __name__ == "__main__":
  getTable()
  fullVigenereMain()
  # generateTable()
  # fullVigenere()