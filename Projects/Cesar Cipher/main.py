import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(alphabet, text, shift):
    decrypted_word = ""
    for i in text:
        if i in alphabet:
            shifted_index = alphabet.index(i)+25-shift+1
            if (shifted_index > 25):
                decrypted_word += alphabet[shifted_index - 26]
            else:
                decrypted_word += alphabet[shifted_index]
        else:decrypted_word+=i
    return decrypted_word

def encrypt(alphabet, text, shift):
    encrypted_word = ""
    for i in text:
        if i in alphabet:
            shifted_index = alphabet.index(i) + shift
            if (shifted_index > 25):
                encrypted_word += alphabet[shifted_index - 26]
            else:
                encrypted_word += alphabet[shifted_index]
        else:encrypted_word+=i
    return encrypted_word

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
flag = True
while flag:
    print(art.logo)
    direction = input("Which direction of Cesar-Cipher: encrypt or decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    if direction == "encrypt":
        result = encrypt(alphabet, text, shift)
    else:
        result = decrypt(alphabet, text, shift)
    print(f"Your {direction}ed text is:", result)
    descison = input("Enter yes to Continue and no to stop: ").lower()
    if descison=="no":
        flag=False
        print("GoodBye: ")