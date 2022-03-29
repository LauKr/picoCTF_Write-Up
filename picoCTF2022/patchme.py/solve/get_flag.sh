#!/usr/bin/env bash
wget -N https://artifacts.picoctf.net/c/391/flag.txt.enc
wget -N https://artifacts.picoctf.net/c/391/patchme.flag.py
echo '### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open("flag.txt.enc", "rb").read()


def my_pw_check():
    if True:
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")

my_pw_check()
' > patched.py
python3 patched.py | grep pico | tee flag.txt
