# picoGYM: MatryoshkaDoll

Author: Susie/Pandu

![Forensics category](https://img.shields.io/badge/category-Forensics-red.svg)
![Score: 30](https://img.shields.io/badge/Score-30-brightgreen.svg)

## Description
> Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Wait, you can hide files inside files? But how do you find them?
</details>

<details>
<summary>Hint 2</summary>
Make sure to submit the flag as picoCTF{XXXXX}
</details>

## Summary

The picture has actually a hidden file which is another picture with a hidden file and so on. In total there are four pictures and the last one contains a hidden txt with the flag.

To extract the hidden files a command like `unzip` can be used.

If your editor shows Unicode replacement characters you can also use `cat flag.txt` to get the flag without them.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{ac0072c423ee13bfc0b166af72e25b61}
```

</details>
