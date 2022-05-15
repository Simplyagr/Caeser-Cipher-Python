
import string
import os 

os.system('cls')
message = str(input("Enter string: "))
message = message.strip()
key_shift = int(input("Enter no. of shifts or Key: "))
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

os.system('cls')
def caeser_encrypt(message, key_shift):
    encrypt = ''
    for i in message:
        if i == ' ':
            encrypt+= ' '
        elif i in string.ascii_lowercase:
            position = alphabet_lower.find(i)
            newposition = (position+key_shift)%26
            encrypt +=alphabet_lower[newposition]
        elif i in string.ascii_uppercase:
            position = alphabet_upper.find(i)
            newposition = (position+key_shift)%26
            encrypt +=alphabet_upper[newposition]
    return (encrypt)


def caeser_decrypt(encrypt,key_shift ):
    decrypt = ''
    for i in encrypt:
            if i == ' ':
                decrypt+= ' '
            if i in string.ascii_lowercase:
                position = alphabet_lower.find(i)
                newposition = (position-key_shift)%26
                decrypt +=alphabet_lower[newposition]
            elif i in string.ascii_uppercase:
                position = alphabet_upper.find(i)
                newposition = (position-key_shift)%26
                decrypt+=alphabet_upper[newposition]
    return (decrypt)

encrypted_string = caeser_encrypt(message, key_shift)
print("Encrypted String=> ",encrypted_string)

print("Do you want to see the decrypted message?(Y/N): ")
if (input()=="Y"):
    authen_key = int(input("Enter key: "))
    if (authen_key==key_shift):
        decrypted_string = caeser_decrypt(encrypted_string, key_shift)
        print(decrypted_string)
    else:
        print("INCORRECT KEY! USER NOT AUTHORIZED!!")







