"""
Crypto.py
Authors: Jasper Sands, Jackson Kunde, William Akis, Daniel Tan, Colin Skinner
Date:
"""
import math
import string

###Dependencies
# Bit to byte: Takes a tuple of length 8 and converts it into an integer in [0, 255]
def bit_to_byte(bits):
    sum = 0
    for i in range(8):
        if int(bits[i]) == 1:
            sum += (2 ** (7 - i))
    return sum

# Byte to bit: Takes an integer in [0, 255] and converts it into a tuple of length 8
def byte_to_bit(byte):
    bits = []
    byteInt = int(byte)
    for i in range (8):
        x = 7 - i

        if (byteInt - (2 ** x)) >= 0:
            bits.append(1)
            byteInt = byteInt - (2 ** x)
        else:
            bits.append(0)
    return bits

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""

    for i in plaintext:
        if 64 < ord(i) < 91:
            new_index = ord(i) + offset

            if new_index < 91:
                encrypted = encrypted + chr(new_index)
            else:
                encrypted = encrypted + chr(new_index - 26)
        else:
            encrypted = encrypted + i


    return encrypted

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypted = ""

    for i in ciphertext:
        if 64 < ord(i) < 91:
            new_index = ord(i) - offset

            if new_index > 64:
                decrypted = decrypted + chr(new_index)
            else:
                decrypted = decrypted + chr(new_index + 26)
        else:
            decrypted = decrypted + i


    return decrypted

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    alphabet = string.ascii_uppercase

    for i in range(0, len(plaintext)):
        index = alphabet.find(keyword[i % len(keyword)])
        index2 = alphabet.find(plaintext[i])
        index3 = int(index + index2)
    
    encrytped = ""
    encrypted += alphabet[index3 % len(alphabet)]

    return encrypted

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    alphabet = string.ascii_uppercase

    for i in range(0, len(plaintext)):
        index = alphabet.find(keyword[i % len(keyword)])
        index2 = alphabet.find(plaintext[i])
        index3 = int(index2 - index)

    decrypted = ""
    decrypted += alphabet[index3 % len(alphabet)]

    return decrypted

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():

    a = input("Word: ").upper()
    num = int(input("Number: "))

    yes = encrypt_caesar(a, num)

    print(decrypt_caesar(yes, num))




    # bits = []
    # for i in range(8):
    #     bits.append(input("one character, 0 or 1: "))
    # print(bit_to_byte(bits))
    #
    # byte = input("one integer, 0 - 255: ")
    # print(byte_to_bit(byte))


if __name__ == "__main__":
    main()
