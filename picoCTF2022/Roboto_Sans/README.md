# picoCTF 2022: Roboto Sans

Author: Mubarak Mikail

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 200](https://img.shields.io/badge/Score-200-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> The flag is somewhere on this web application not necessarily on the website. Find it.  
> Check [this](http://saturn.picoctf.net:57329/) out.

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

None

## Summary

If we visit the website we can have a look through all the stuff. A first point should be the /robots.txt file.

Here we see some symbols at the bottom directly above _Disallow: /wp-admin/_.
The middle part seems like it's Base64 encoded and if we decode it it says _js/myfile.txt_.

If we visit that file we have the flag.
The interesting part in this challenge is that the flag is not really on the web application, so a website mirror and
```bash
grep -rw 'path' -e 'picoCTF'
```
does not work here, as the /js/myfile.txt is not mirrored.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{Who_D03sN7_L1k5_90B0T5_87ccf72a}
```

</details>
