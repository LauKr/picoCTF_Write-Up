#!/bin/python3
import string
import sys
import requests


def download(url: str) -> int:
    r = requests.get('https://artifacts.picoctf.net/c/504/message.txt')
    with open(filename , 'wb') as message:
        message.write(r.content)
    return 0


def find_inverse_modulo(x: int, p: int) -> int:
    y = pow(x, -1, p)
    return y


def decode(file: str, mod: int):
    nums = range(1, 38)
    alphs = list(string.ascii_uppercase)
    alphs.extend(range(0, 10))
    alphs.append("_")
    dic = dict(zip(nums, alphs))
    decoded_message = []

    with open("message.txt", 'r') as file_in:
        numbers = file_in.readlines()[0].split()
        for number in numbers:
            number = int(number) % mod
            inv = find_inverse_modulo(number, mod)
            decoded_message.append(dic[inv])
    with open("flag.txt", 'w') as f:
        f.write("picoCTF{")
        for char in decoded_message:
            f.write(str(char))
        f.write("}")


if __name__ == '__main__':
    filename = 'message.txt'
    download(filename)
    decode(filename, mod=41)
