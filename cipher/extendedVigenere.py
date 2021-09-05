from cipher.utilities import formatInput
import struct

relativeDir = "./static/dump/"

def extendedVigenere(mode: str = "e", filename: str = None):
  # mode: "e" untuk encrypt dan "d" untuk decrypt

  k = formatInput(input("Input key: "))
  while (k == ""):
    print("You must input key.")
    k = formatInput(input("Input key: "))
  nk = len(k)
  
  bytes = list()
  
  if filename == None:
    if mode == "e":
      filename = "./../static/dump/blue.png"
    elif mode == "d":
      filename = "./../static/dump/alteredImage.png"
  
  with open(filename, 'rb') as file:
    fileBytes = file.read()
    fileBytes = struct.unpack("c" * (len(fileBytes)), fileBytes)
    
    temp = list()
    i = 0
    # once = True
    print("yeah")
    for b in fileBytes:
      # Convert from bytes...
      # temp.append(int.from_bytes(b, "big"))
      
      # Encrypt/Decrypt
      if mode == "e":
        # temp.append(shiftASCII(b, k[i % nk], '+'))
        temp.append(int.from_bytes(b, "big"))
        temp[i] = (temp[i] + ord(k[i % nk])) % 256
        # to bytes...
        temp[i] = int.to_bytes(temp[i], 1, "big")
      elif mode == "d":
        # temp.append(shiftASCII(b, k[i % nk], '-'))
        temp.append(int.from_bytes(b, "big"))
        temp[i] = (temp[i] - ord(k[i % nk])) % 256
        # to bytes...
        temp[i] = int.to_bytes(temp[i], 1, "big")
        

      # Convert to bytes...
      # temp[i] = int.to_bytes(temp[i], 1, "big")
      i += 1
    bytes = b"".join(temp)

  if mode == "e":
    with open("./../static/dump/alteredImage.png", "wb") as outputFile:
      outputFile.write(bytes)
  else:
    with open("./../static/dump/recoveredImage.png", "wb") as outputFile:
      outputFile.write(bytes)

def extendedVigenereEncrypt(filename:str, keytext:str, outputFileName: str):
  # !outputFileName adalah masukan teks tanpa format (menyesuakan format input file)!
  bytes = list()
  nk = len(keytext)
  # if filename == None:
  #   if mode == "e":
  #     filename = "./../static/dump/blue.png"
  #   elif mode == "d":
  #     filename = "./../static/dump/alteredImage.png"
  
  print(filename)
  with open(f"{relativeDir}{filename}", 'rb') as file:
    fileBytes = file.read()
    fileBytes = struct.unpack("c" * (len(fileBytes)), fileBytes)
    
    temp = list()
    i = 0
    # once = True
    for b in fileBytes:
      # Convert from bytes...
      # temp.append(int.from_bytes(b, "big"))
      
      # Encrypt/Decrypt
      # temp.append(shiftASCII(b, k[i % nk], '+'))
      temp.append(int.from_bytes(b, "big"))
      temp[i] = (temp[i] + ord(keytext[i % nk])) % 256
      # to bytes...
      temp[i] = int.to_bytes(temp[i], 1, "big")


      # Convert to bytes...
      # temp[i] = int.to_bytes(temp[i], 1, "big")
      i += 1
    bytes = b"".join(temp)

  fileFormat = filename.split('.')[-1]
  if outputFileName == None:
    outputFileName = f"alteredFile.{fileFormat}"
  else:
    outputFileName = f"{outputFileName}.{fileFormat}"
  with open(f"{relativeDir}{outputFileName}", "wb") as outputFile:
    outputFile.write(bytes)
  
  return {
    "inputFileName": filename,
    "keytext": keytext,
    "outputFileName": outputFileName
  }

def extendedVigenereDecrypt(filename:str, keytext:str, outputFileName:str):
  # !outputFileName adalah masukan teks tanpa format (menyesuakan format input file)!
  nk = len(keytext)
  bytes = list()
  
  # if filename == None:
  #   if mode == "e":
  #     filename = "./../static/dump/blue.png"
  #   elif mode == "d":
  #     filename = "./../static/dump/alteredImage.png"
  
  with open(f"{relativeDir}{filename}", 'rb') as file:
    fileBytes = file.read()
    fileBytes = struct.unpack("c" * (len(fileBytes)), fileBytes)
    
    temp = list()
    i = 0
    # once = True
    for b in fileBytes:
      # Convert from bytes...
      # temp.append(int.from_bytes(b, "big"))
      
      # Encrypt/Decrypt
      # temp.append(shiftASCII(b, k[i % nk], '-'))
      temp.append(int.from_bytes(b, "big"))
      temp[i] = (temp[i] - ord(keytext[i % nk])) % 256
      # to bytes...
      temp[i] = int.to_bytes(temp[i], 1, "big")
        

      # Convert to bytes...
      # temp[i] = int.to_bytes(temp[i], 1, "big")
      i += 1
    bytes = b"".join(temp)

  fileFormat = filename.split('.')[-1]
  if outputFileName == None:
    outputFileName = f"recoveredImage.{fileFormat}"
  else:
    outputFileName = f"{outputFileName}.{fileFormat}"

  with open(f"{relativeDir}{outputFileName}", "wb") as outputFile:
    outputFile.write(bytes)
  
  return {
    "inputFileName": filename,
    "keytext": keytext,
    "outputFileName": outputFileName
  }

def emptyResult(filename=""):
  return {
    "inputFileName": filename,
    "keytext": "",
    "outputFileName": ""
  }

def testOpen(filename = "./../static/dump/blue.png"):
  with open(filename, mode='rb') as file: # b is important -> binary
    fileContent = file.read()
    start = struct.unpack("1000c", fileContent[:1000])
    body = struct.unpack("c" * (len(fileContent) -1400), fileContent[1000:-400])
    end = struct.unpack("400c", fileContent[-400:])
    print("start: ", start)
    print("end: ", end)

    # print(body)
    # for s in start:
    #   print(s)
    # for b in body:
      # print((int) b)
    
    # Migrate bytes
    # 1. start
    temp1 = list()
    for s in start:
      temp1.append(s)
    bytes1 = b"".join(temp1)

    # 2. body
    temp2 = list()
    i = 0
    # once = True
    for b in body:
      # Convert bytes
      # from bytes...
      temp2.append(int.from_bytes(b, "big"))
      # if once and temp2[i] == 255:
      #   print(i, temp2[i], b)
      #   temp2[i] = (temp2[i] + 30) % 256
      #   print(i, temp2[i], int.to_bytes(temp2[i], 1, "big"))
      #   once = False
      temp2[i] = (temp2[i] + 30) % 256
      # to bytes...
      temp2[i] = int.to_bytes(temp2[i], 1, "big")
      i += 1
    bytes2 = b"".join(temp2)
      
    # 1. start
    temp3 = list()
    for e in end:
      temp3.append(e)
    bytes3 = b"".join(temp3)
    

    # Concatenate bytes
    temp = [bytes1, bytes2, bytes3]
    print("temp[0]", temp[0])
    print("temp[2]", temp[2])
    allBytes = b"".join(temp)

    # Pack bytes, nope

    # Write bytes
    with open("alteredImage.png", "wb") as outputFile:
      outputFile.write(allBytes)

def extendedVigenereMain():
  promptMode = False
  choice = ""
  while not promptMode:
    print("  ? ? ? ? ?")
    print("  Do you want to encrypt(e) or decrypt(d)?")
    print("  > e")
    print("  > d")
    choice = input("  >>> ")
    if choice not in ["e", "d"]:
      continue

    print("    ? ? ? ? ?")
    print("    Do you want to input filename?")
    if choice == "e":
      print("    1. Yes (default: ./assets/blue.png")
    elif choice == "d":
      print("    1. Yes (default: ./assets/alteredImage.png")
    print("    2. Nope, continue")
    print("    Press any other key to exit")

    submenu = input("    >>> ")

    if submenu == "1":
      filename = input("    >>> Input filename: ")
      extendedVigenere(mode=choice, filename=filename)
    elif submenu == "2":
      extendedVigenere(mode=choice)
    else:
      promptMode = True

if __name__ == "__main__":
  extendedVigenereMain()