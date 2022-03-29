# picoCTF 2022: unpackme.py

Author: LT 'syreal' Jones

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you get the flag?  
Reverse engineer this [Python program](https://artifacts.picoctf.net/c/469/unpackme.flag.py).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

None

## Summary

First understand what this program does.  
It decrypts `payload` with a `key_str` and executes the stuff in payload. So if we print the decrypted payload we can get a hardcoded password. I just patched the file by adding one print statement.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{175_chr157m45_45a1a353}
```

</details>
