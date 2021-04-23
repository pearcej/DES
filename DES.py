
from Crypto.Cipher import DES, DES3
from Crypto import Random

KEY = "The key!"

iv = Random.new().read(DES3.block_size)
KEY2 = Random.new().read(DES3.key_size[-1])


def encryptDES(msg):

    cipher = ""
    return cipher


def decryptDES(cipher):

    plainOut = ""
    return plainOut


def encrypt3DES(msg):

    cipher = ""
    return cipher


def decrypt3DES(cipher):

    plainOut = ""
    return plainOut


def main():
    message = "Hi class!"
    print message
    cipher = encryptDES(message)
    print cipher
    print decryptDES(cipher)


    cipher = encrypt3DES(message)
    print cipher
    print decrypt3DES(cipher)

main()