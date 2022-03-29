# picoCTF 2022: Safe Opener

Author: Mubarak Mikail

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you open this safe?  
I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?  
Put the password you recover into the picoCTF flag format like:  
`picoCTF{password}`

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

None

## Summary

The password is hardcoded in the java code. You'll just need to decode it from BASE64.
## Flag

<details><summary>Show flag</summary>

```
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```

</details>
