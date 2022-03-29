# picoCTF 2022: credstuff

Author: Will Hong / LT 'syreal' Jones

![Cryptography category](https://img.shields.io/badge/category-Cryptography-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?  
Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar).  
The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Maybe other passwords will have hints about the leak?
</details>

## Summary

Just look up the corresponding password for the user. I loaded both files into lists in python and created a dictionary. The resulting password is ROT13 encrypted. Decrypt and you'll have the flag. For an automated solution look in [solve](./solve/)

## Flag

<details><summary>Show flag</summary>

```
picoCTF{C7r1F_54V35_71M3}
```

</details>
