# picoGYM: crackme-py

Author: syreal

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 30](https://img.shields.io/badge/Score-30-brightgreen.svg)

## Description
> [crackme.py](https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py)

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

None

## Summary

The python script has everything necassary to get the flag. It just only executes the
`choose_greatest()`
function, which is useless.
By removing the call for this function and adding a
`decode_secret(bezos_cc_secret)` instead we get the correct flag.

The decoding function performs a ROT47 on every char of the secret which yields the flag.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{1|\/|_4_p34|\|ut_8c551048}
```

</details>
