# picoGYM: 2Warm

Author: Sanjay C/Danny Tunitis

![General_Skills category](https://img.shields.io/badge/category-General_Skills-red.svg)
![Score: 50](https://img.shields.io/badge/Score-50-brightgreen.svg)

## Description
> Can you convert the number 42 (base 10) to binary (base 2)?

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Submit your answer in our competition's flag format. For example, if your answer was '11111', you would submit 'picoCTF{11111}' as the flag.
</details>

## Summary

You can either just use an online converter or take that as an oppurtunity to recap binary numbers.

I wrote a [script](https://github.com/LauKr/PythonStuff/blob/master/change2binary.py) to change the base of a number some time ago so I used that.

### How to change decimal to binary?

There are a lot of tutorials how to do that online. However a short summary:

Binary numbers can be represented in decimal as
![formula](https://render.githubusercontent.com/render/math?math=10010=0\cdot2^0) + ![formula](https://render.githubusercontent.com/render/math?math=1\cdot2^1) + ![formula](https://render.githubusercontent.com/render/math?math=0\cdot2^2) + ![formula](https://render.githubusercontent.com/render/math?math=0\cdot2^3) + ![formula](https://render.githubusercontent.com/render/math?math=1\cdot2^4)

Analogous the change from decimal to binary can be done by calculating the prefactors. This can be done using the logarithm to base two.

> Some prerequisites for the calculation:
>
> ![formula](https://render.githubusercontent.com/render/math?math=\log_b(a)=\frac{\log(a)}{\log(b)}) with ![formula](https://render.githubusercontent.com/render/math?math=\log(a)) and ![formula](https://render.githubusercontent.com/render/math?math=\log(b)) being logarithms to **any** base.
>
> &lfloor;x&rfloor; denotes the floor function: E.g. &lfloor;2.8&rfloor;=2, &lfloor;2.1&rfloor;=2;

![formula](https://render.githubusercontent.com/render/math?math=\lfloor\log_2(42)\rfloor=\left\lfloor\frac{\log(42)}{\log(2)}\right\rfloor=\lfloor\log_2(5.3923...)\rfloor=5)

![formula](https://render.githubusercontent.com/render/math?math=remains=42-2^5=42-32=10)

![formula](https://render.githubusercontent.com/render/math?math=\lfloor\log_2(10)\rfloor=\lfloor3.3219...\rfloor=3)

![formula](https://render.githubusercontent.com/render/math?math=remains=10-2^3=10-8=2)

![formula](https://render.githubusercontent.com/render/math?math=\log_2(2)=1\Rightarrow\text{remains}=0)

So the 1st, 3rd and 5th bit are one, the remaining bits are all zero:
> 101010\
> Note: Bits are counted from right to left and include the 0th bit

## Flag

<details><summary>Show flag</summary>

```
picoCTF{101010}
```

</details>
