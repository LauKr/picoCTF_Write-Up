# picoCTF 2022: substitution0

Author: Will Hong

![Cryptography category](https://img.shields.io/badge/category-Cryptography-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?  
Download the message [here](https://artifacts.picoctf.net/c/384/message.txt).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Try a frequency attack. An online tool might help.
</details>

## Summary

The key is given at the top:

```
iadnmlpfyejswbzvxuhkgrocqt
abcdefghijklmnopqrstuvwxyz
```

You can use an online tool like [CyberChef](https://gchq.github.io/CyberChef/#recipe=To_Upper_case('All')Substitute('IADNMLPFYEJSWBZVXUHKGROCQT','ABCDEFGHIJKLMNOPQRSTUVWXYZ')&input=SUFETk1MUEZZRUpTV0JaVlhVSEtHUk9DUVQgCgpGbXVtZ3Z6YiBTbXB1aWJuIGl1emhtLCBveWtmIGkgcHVpcm0gaWJuIGhraWttc3EgaXl1LCBpYm4gYXV6Z3BmayB3bSBrZm0gYW1ta3NtCmx1encgaSBwc2loaCBkaWhtIHliIG9meWRmIHlrIG9paCBtYmRzemhtbi4gWWsgb2loIGkgYW1pZ2t5bGdzIGhkaXVpYWltZ2gsIGlibiwgaWsKa2ZpayBreXdtLCBnYmpiem9iIGt6IGJpa2d1aXN5aGto4oCUemwgZHpndWhtIGkgcHVtaWsgdnV5dG0geWIgaSBoZHltYmt5bHlkIHZ6eWJrCnpsIHJ5bW8uIEtmbXVtIG9tdW0ga296IHV6Z2JuIGFzaWRqIGh2emtoIGJtaXUgemJtIG1ja3Vtd3lrcSB6bCBrZm0gYWlkaiwgaWJuIGkKc3picCB6Ym0gYm1pdSBrZm0gemtmbXUuIEtmbSBoZGlzbWggb211bSBtY2RtbW55YnBzcSBmaXVuIGlibiBwc3poaHEsIG95a2YgaXNzIGtmbQppdnZtaXVpYmRtIHpsIGFndWJ5aGZtbiBwenNuLiBLZm0gb215cGZrIHpsIGtmbSB5YmhtZGsgb2loIHJtdXEgdW13aXVqaWFzbSwgaWJuLApraWp5YnAgaXNzIGtmeWJwaCB5Ymt6IGR6Ymh5bm11aWt5emIsIFkgZHpnc24gZml1bnNxIGFzaXdtIEVndnlrbXUgbHp1IGZ5aCB6dnlieXpiCnVtaHZtZGt5YnAgeWsuCgpLZm0gbHNpcCB5aDogdnlkekRLTHs1R0E1NzE3RzcxMEJfM1IwU0c3MTBCX0ExTjM2NzcyfQ) to decode it.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{5UB5717U710N_3V0LU710N_B1D36772}
```

</details>
