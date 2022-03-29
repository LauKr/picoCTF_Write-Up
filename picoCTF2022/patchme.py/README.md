# picoCTF 2022: patchme.py

Author: LT 'syreal' Jones

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you get the flag? Run this [Python program](https://artifacts.picoctf.net/c/391/patchme.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/391/flag.txt.enc).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

None

## Summary

In the downloaded python file you can read out the password easily.
<details><summary>Password</summary>ak98-=90adfjhgj321sleuth9000</details>

But it is also possible to just patch the file to skip the password check. (e.g. removing it completely or changing to `if True:`)

## Flag

<details><summary>Show flag</summary>

```
picoCTF{p47ch1ng_l1f3_h4ck_68aa6913}
```

</details>
