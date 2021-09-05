import re

def charToInt(c: str) -> int:
  # 'a' = 0, 'b' = 2, ..., 'z' = 25
  return ord(c) - ord('A')

def intToChar(i: int) -> str:
  return chr(i + ord('A'))

def shiftAlphabet(p: str, k: str, mode: str):
  # p: char awal
  # k: char shift
  # mode: char '+' or '-'
  if mode == '+':
    return intToChar((charToInt(p) + charToInt(k)) % 26)
  if mode == '-':
    return intToChar((charToInt(p) - charToInt(k)) % 26)

def formatInput(inp: str) -> str:
  # remove anything except alphanumeric and underscores
  inp = re.sub(r'[^\w]', ' ', inp)

  # remove underscores
  inp = re.sub(r'\_', ' ', inp)
  
  # remove numbers
  inp = re.sub(r'\d', ' ', inp)

  # remove whitespaces
  inp = inp.replace(' ', '')

  # UPPERCASE
  return inp.upper()

def arrangeText(input: str) -> str:
  # Memisahkan teks string ke dalam kata-kata dengan 5 huruf
  result = ""
  i = 0
  for letter in input:
    i += 1

    result += letter

    if i == 5:
      result += " "
      i = 0
  return result


# def shiftASCII(p: str, k: str, mode: str):
#   # Sama dengan shift alphabet, tapi include semua 256 karakter ASCII
#   # p: byte awal
#   # k: char shift
#   # mode: char '+' or '-'
  
#   if mode == '+':
#     return bytes(chr((ord(p) + ord(k)) % 256), 'utf-8')
#   if mode == '-':
#     return bytes(chr((ord(p) - ord(k)) % 256), 'utf-8')

