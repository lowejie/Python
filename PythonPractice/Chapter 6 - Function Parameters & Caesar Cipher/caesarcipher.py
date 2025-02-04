alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

proceed = True
def encode_decode(text,shift_amount,direction):
    output = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in text:
        if letter not in text:
            output+=letter
        new_letter_index = alphabet.index(letter)+shift_amount
        new_letter_index %= len(alphabet)
        output+=alphabet[new_letter_index]
    print(output)

while proceed:

    code_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encode_decode(message,shift,code_type)
    restart = input("do again?:\n").lower()
    if restart == "no":
        proceed = False
        print("session end.")