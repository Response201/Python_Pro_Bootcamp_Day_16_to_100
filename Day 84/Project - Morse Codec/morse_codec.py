from morse_code_dict import MORSE_CODE_DICT
run_crypter = True
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encrypt(msg):

    morse_code = ""

    for letter in msg:

            if letter == " ":
                morse_code += "  "
            else:
                try:
                    morse_code += f"{MORSE_CODE_DICT[letter]} "

                except KeyError:
                     morse_code += "? "

    return morse_code



def decrypt(msg):
    text = ""
    message = msg.split(" ")

    for letter in message:
        try:
            if letter == '':
                text += " "
            else:
                text += REVERSE_DICT[letter]
        except KeyError:
            text += "?"

    return text.lower()




while run_crypter:
    choice = input(f"Enter E to encrypt, D to decrypt, or STOP to exit: \n").upper()

    if choice == "STOP":
        run_crypter = False

    else:
        message = input(f"Enter a message:\n")

        if choice == "D":
            result = decrypt(message)

        else:
            result = encrypt(message.upper())

        print(result)