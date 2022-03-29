#!/bin/python3
import string
import sys
import requests


def decode(file: str):
    nums = range(0, 37)
    alphs = list(string.ascii_uppercase)
    alphs.extend(range(0, 10))
    alphs.append("_")
    dic = dict(zip(nums, alphs))
    decoded_message = []

    with open("message.txt", 'r') as file_in:
        numbers = file_in.readlines()[0].split()
        for number in numbers:
            number = int(number) % 37
            decoded_message.append(dic[number])
    with open("flag.txt", 'w') as f:
        f.write("picoCTF{")
        for char in decoded_message:
            f.write(str(char))
        f.write("}")


if __name__ == '__main__':
    filename = 'message.txt'
    r = requests.get('https://artifacts.picoctf.net/c/398/message.txt')
    with open(filename , 'wb') as message:
        message.write(r.content)
    decode(filename)
