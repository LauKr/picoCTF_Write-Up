# picoCTF 2022: basic-mod1

Author: Will Hong

![Cryptography category](https://img.shields.io/badge/category-Cryptography-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.
>
> Download the message [here](https://artifacts.picoctf.net/c/398/message.txt).
>
> Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
>
> Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Do you know what mod 37 means?
</details>
<details>
<summary>Hint 2</summary>
mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.
</details>

## Summary

Performing the [modulo](https://en.wikipedia.org/wiki/Modulo_operation) 37 operation on every number gives a new set of numbers. Syntax in most common languages:
```python
number % 37
```

You can either substitute the new numbers by hand or write a script for it. [Example](./solve/get_flag.py) is given in the _solve_ subfolder.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{}
```

</details>
