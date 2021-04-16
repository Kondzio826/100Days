import string

letters = string.ascii_lowercase

choice = input("Encode or Decode?\n")
word = input("Give me word: \n")
shift = int(input("How many shift?\n"))

def  decode(word_to_decode):
    result = ""
    for letter in word_to_decode:
        ID = letters.find(letter)
        if choice == "encode":
            letter = letters[(ID+shift)%25]
        elif choice == "decode":
            letter = letters[(ID-shift)%25]
        result += letter
    return result

print(decode(word))
