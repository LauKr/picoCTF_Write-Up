# picoCTF 2022: basic-mod2

Author: Will Hong

![Cryptography category](https://img.shields.io/badge/category-Cryptography-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> A new modular challenge!
>
> Download the message [here](https://artifacts.picoctf.net/c/504/message.txt).
>
> Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
>
> Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Do you know what the modular inverse is?
</details>
<details>
<summary>Hint 2</summary>
The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
</details>
<details>
<summary>Hint 3</summary>
It's recommended to use a tool to find the modular inverses
</details>

## Summary

This time we perform the [modulo](https://en.wikipedia.org/wiki/Modulo_operation) operation as well, but `mod 41` instead of `mod 37`.
Then we have to calculate the [modular inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse).


Again, you can either substitute the new numbers by hand or write a script for it. [Example](./solve/get_flag.py) is given in the _solve_ subfolder (Requires Python 3.8+).
> :warning: the character mapping is changed. Instead of 0-25 etc it is 1-26 now. So change your script accordingly.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{1NV3R53LY_H4RD_B7FB947C}
```

</details>
