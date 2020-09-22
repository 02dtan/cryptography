"""
Crypto.py
Authors: Jasper Sands, Jackson Kunde, William Akis, Daniel Tan, Colin Skinner
Date:
"""
import math

###Dependencies
# Bit to byte: Takes a tuple of length 8 and converts it into an integer in [0, 255]
def bit_to_byte(bits):
    sum = 0
    for i in range(0, 7):
        sum += int(bits[i]) ** (7-i)
    return sum

# Byte to bit: Takes an integer in [0, 255] and converts it into a tuple of length 8
def byte_to_bit(byte):
    bits = []
    for i in range (0, 7):
        x = 7 - i
        # something something math.pow(2, x)
        if (byte - (2 ** x)) > 0:
            bits.append(1)
            byte = byte % (2 ** x)
            # byte = byte - (2 ** x)
        else:
            bits.append(0)
    return bits

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    pass

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    pass

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

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
    # Testing code here
    bits = []
    for i in range(0, 7):
        bits.append(input("one character, 0 or 1: "))
    print(bit_to_byte(bits))

    byte = input("one integer, 0 - 255: ")
    print(byte_to_bit(byte))
    # 01000101

if __name__ == "__main__":
    main()
