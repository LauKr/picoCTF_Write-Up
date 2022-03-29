# picoCTF 2022: Power Cookie

Author: LT 'syreal' Jones

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 200](https://img.shields.io/badge/Score-200-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you get the flag?  
> Go to this [website](http://saturn.picoctf.net:63397/) and see what you can discover.

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Do you know how to modify cookies?
</details>

## Summary

Visit the website, _Continue as guest_, you'll get an information printed that "_We apologize, but we have no guest services at the moment._"

If you view* the cookies for this website you'll find a cookie called _isAdmin_ with the value 0. change that value to use, reload the page and you have the flag.  
*To view the cookies you can just use a cookie manager for your browser or get them from your browser if it's capable to show them.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{gr4d3_A_c00k13_87608ba8}
```

</details>
