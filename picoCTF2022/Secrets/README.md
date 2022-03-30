# picoCTF 2022: Secrets

Author: Geoffrey Njogu

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 200](https://img.shields.io/badge/Score-200-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> We have several pages hidden. Can you find the one with the flag?   
> The website is running [here](http://saturn.picoctf.net:49810/).  

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details><summary>Hint 1</summary>
folders folders folders
</details>

## Summary

If we view the source code for the website we find an interesting stylesheet in the header: `secret/assets/index.css`  
While the file itself is not containing any secret information we can view `/secret/` instead and get a hint that we indeed are on the right track.  
Analogous we can find a `/secret/hidden/` folder and even a `/secret/hidden/superhidden/` containing stylesheets for the previous sites.

Go to `/secret/hidden/superhidden/` and there is a white h3 you can either select and copy or just view in the source.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{succ3ss_@h3n1c@10n_08de81e4}
 ```

</details>
