def encode_decode():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(text, shift):
        result = []
        final = ""
        result = [alphabet[(alphabet.index(i) + shift - 26) if (alphabet.index(i) + 1 + shift > len(alphabet)) else (alphabet.index(i) + shift)] for i in text]

        final = "".join(result)
        return final
        

    def decrypt(text, shift):
        result = []
        final = ""
        result = [alphabet[(alphabet.index(i) - shift + 26) if (alphabet.index(i) + 1 - shift < 0) else (alphabet.index(i) - shift)] for i in text]

        final = "".join(result)
        return final

    if direction == "encode":
        print(encrypt(text, shift))
    elif direction == "decode":
        print(decrypt(text, shift))
    i = str(input("Wanna one more? 'yes' or 'no': "))
    if  i == "yes":
        encode_decode()
    elif i == "no":
        return "bye bye"

from art import logo
print(logo)
encode_decode()