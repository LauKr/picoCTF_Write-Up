#!/bin/python
import numpy as np
import codecs


def get_password(user: str) -> str:
    with open('leak/usernames.txt', 'r') as f:
        users = np.loadtxt(f, dtype=str)
    with open('leak/passwords.txt', 'r') as f:
        passwords = np.loadtxt(f, dtype=str)

    dictionary = dict(zip(users, passwords))
    user_passwd = dictionary[username]
    decoded_passwd = codecs.encode(user_passwd, 'rot_13')
    return decoded_passwd


if __name__ == '__main__':
    username = 'cultiris'
    passwd = get_password(username)
    print(passwd)
    with open('flag.txt', 'w') as f:
        f.write(passwd)
