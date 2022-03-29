# picoCTF 2022: Search source

Author: Mubarak Mikail

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is [here](http://saturn.picoctf.net:56849/)

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
How could you mirror the website on your local machine so you could use more powerful tools for searching?
</details>

## Summary

The idea is to find the flag that's probably hidden somewhere on the source code.

- One approach is to just look manually. This way it can be found in `css/style.css`.
- The second one (especially convenient for larger websites) is to mirror the site to your machine and search for the flag using `grep`. An automated [script](./solve/get_flag.sh) doing that is attached, feel free to have a look.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{1nsp3ti0n_0f_w3bpag3s_74784981}
```

</details>
