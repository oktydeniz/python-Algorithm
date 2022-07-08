import string
import os

abc = string.ascii_lowercase
max_len = len(abc)

clear = ("cls" if os.name == "nt" else "clear")


def options():
    while 1:

        option = input(" Your Options  : ").lower()
        if option in ("encrypt", "Encrypt", "encrypt"):
            encrypt()
        elif option in ("Decrypt", "decrypt", "find"):
            decrypt()
        elif option in ("close", "exit", "shutdown"):
            break
        else:
            print("For Encrypt : (%s) For Decrypt (%s) For Exit (%s)" % ("encrypt", "decrypt", "exit"))


def encrypt():
    text = input("Text :").lower()
    encryption = encryption_key()
    decrypt_text = ""
    for i in text:
        if i.isalpha():
            char_row_no = ord(i)
            char_row_no += encryption
            if char_row_no > ord("z"):
                char_row_no -= max_len
            elif char_row_no < ord("a"):
                char_row_no += max_len
            decrypt_char = chr(char_row_no)
            decrypt_text += decrypt_char
        else:
            decrypt_text += i
    os.system(clear)
    print(f" The encryption of {text} with the {encryption} key :  {decrypt_text}")
    input("Press ")


def decrypt():
    encrypt_text = input("text :").lower()
    encryption = encryption_key()
    decrypt_text = ""

    for i in encrypt_text:
        if i.isalpha():
            char_row_no = ord(i)
            char_row_no -= encryption
            if char_row_no > ord("z"):
                char_row_no -= max_len
            elif char_row_no < ord("a"):
                char_row_no += max_len
            decrypt_char = chr(char_row_no)
            decrypt_text += decrypt_char
        else:
            decrypt_text += i
    os.system(clear)
    print(f" The decryption of {encrypt_text} with the {encryption} key :  {decrypt_text}")
    input("Press ")


def encryption_key():
    key = int(input("Encryption Key (1 %s) :" % max_len))
    if 1 <= key <= max_len:
        return key
    else:
        return 1


options()
