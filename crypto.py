"""
Crypto.py
Authors: Jasper Sands, Jackson Kunde, William Akis, Daniel Tan, Colin Skinner
Date: Sep 30
"""
import math
import string
import random

### Dependencies
# Bit to byte: Takes a tuple of length 8 and converts it into an integer in [0, 255]
def bit_to_byte(bits):
    sum = 0
    if len(bits) == 8:
        for i in range(8):
            if int(bits[i]) == 1:
                sum += (2 ** (7 - i))

        return sum
    else:
        print("invalid byte representation")

# Byte to bit: Takes an integer in [0, 255] and converts it into a tuple of length 8
def byte_to_bit(byte):
    bits = []
    byteInt = int(byte)
    if 0 <= byte <= 255:
        for i in range (8):
            x = 7 - i
            if (byteInt - (2 ** x)) >= 0:
                bits.append(1)
                byteInt = byteInt - (2 ** x)
            else:
                bits.append(0)

        return bits
    else:
        print("out of 8-bit bounds")

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""
    if not plaintext.isupper():
        plaintext = plaintext.upper()
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
    if not ciphertext.isupper():
        ciphertext = ciphertext.upper()
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
    encrypted = ""
    if not plaintext.isupper():
        plaintext = plaintext.upper()
    if not keyword.isupper():
        keyword = keyword.upper()
    iterator = 0
    for i in plaintext:
        if iterator == len(keyword):
            iterator = 0
        if 64 < ord(i) < 91:
            #65 - ASCII value of "A", supposed shift 0
            new_index = ord(i) + (ord(keyword[iterator]) - 65)
            if new_index < 91:
                encrypted = encrypted + chr(new_index)
            else:
                encrypted = encrypted + chr(new_index - 26)
        else:
            encrypted = encrypted + i
        iterator += 1

    return encrypted

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypted = ""
    if not ciphertext.isupper():
        ciphertext = ciphertext.upper()
    if not keyword.isupper():
        keyword = keyword.upper()
    iterator = 0
    for i in ciphertext:
        if iterator == len(keyword):
            iterator = 0
        if 64 < ord(i) < 91:
            #65 - ASCII value of "A", supposed shift 0
            new_index = ord(i) - (ord(keyword[iterator]) - 65)
            if new_index > 64:
                decrypted = decrypted + chr(new_index)
            else:
                decrypted = decrypted + chr(new_index + 26)
        else:
            decrypted = decrypted + i
        iterator += 1

    return decrypted

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n = 8):
    W = []

    W.append(random.randint(1, 100))
    for i in range(n - 1):
        W.append(sum(W) + random.randint(1, 100))

    private_key = [tuple(W)]
    Q = sum(W) + random.randint(0, 100)

    private_key.append(Q)
    R = 0

    for r in range(2, Q):
        if math.gcd(r, Q) == 1:
            R = r #because it's R
            break

    private_key.append(R)

    return private_key

# Arguments: tuple (W, Q, R)
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    public_key = []

    for line in (private_key[0]):
        public_key.append((private_key[2] * line) % private_key[1])

    return public_key

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    encrypt = []

    for i in plaintext:
        tmp = []
        binary = byte_to_bit(ord(i))
        for x in range(8):
            tmp.append(binary[x] * public_key[x])
        encrypt.append(sum(tmp))

    return encrypt

# Arguments: two integers, q and r
# Returns: result of inverse modulus function
def mod_inverse(q, r):
    for num in range(2, r):
        if (r * num % q) == 1:
            return num

# Arguments: list of integers, tuple (W,Q,R)
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    final_list = []

    for c in ciphertext: # each letter in text
        letter_values = []

        r_prime = mod_inverse(private_key[1], private_key[2])
        c_prime = (c * r_prime) % private_key[1]

        for value in private_key[0][::-1]:
            if c_prime >= value:
                c_prime -= value
                letter_values.append(value)

        indices = []

        for z in letter_values:
            for t in range(len(private_key[0])):
                if z == private_key[0][t]:
                    indices.append(t)

        final = 0

        for pos in indices:
            final += math.pow(2, 7 - pos)
        final_list.append(chr(int(final)))

    final_string = "".join(final_list)

    return final_string

def main():
    print(bit_to_byte([1, 0, 0, 0, 1, 0, 1, 0]))
    print(byte_to_bit(138))
    print(encrypt_caesar("hello", 4))
    print(decrypt_caesar(encrypt_caesar("hello", 15), 11))
    print(encrypt_vigenere("hello", "aaaaa"))
    print(decrypt_vigenere(encrypt_vigenere("hello", "ABCDE"), "ABCDE"))
    print(encrypt_vigenere("what", "lsl"))
    print(encrypt_vigenere("what", "lslllslslsl"))

    # private_key = ([2, 7, 11, 21, 42, 89, 180, 354], 881, 588)
    # # private_key = generate_private_key()
    # public_key = (create_public_key(private_key))
    #
    # print(encrypt_mhkc("a", public_key))
    #
    # print(decrypt_mhkc(encrypt_mhkc("", public_key), private_key))

if __name__ == "__main__":
    main()
