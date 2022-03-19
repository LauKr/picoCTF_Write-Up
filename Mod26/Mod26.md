# picoGYM: Mod 26

Author: Pandu

![general_skills category](https://img.shields.io/badge/category-General_Skills-red.svg)
![Score: 10](https://img.shields.io/badge/Score-10-brightgreen.svg)

## Description
> Cryptography can be easy, do you know what ROT13 is?
> ```cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}```

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
This can be solved online if you don't want to do it by hand!
</details>

## Summary

The flag was 'encrypted' using Rot13, a Caesar cipher. It works by shifting every letter by 13.
In fact it's a substitution of `a -> n, b -> o, c -> p` and so on.

A shifted text can be translated by using the command 
```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< "Text"
```

## Flag

<details><summary>Show flag</summary>

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}
```

</details>
