alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(alphabet,text,shift):
  encrypted_word=""
  for i in range(len(text)):
    shifted_index = alphabet.index(text[i]) + shift
    if (shifted_index >25):
      encrypted_word+=alphabet[shifted_index - 26]
    else:
      encrypted_word+=alphabet[shifted_index]

  return encrypted_word

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
result = encrypt(alphabet,text,shift)
print("Encoded text is:",result)



