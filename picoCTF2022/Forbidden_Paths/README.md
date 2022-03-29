# picoCTF 2022: Forbidden Paths

Author: LT 'syreal' Jones

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 200](https://img.shields.io/badge/Score-200-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you get the flag?  
> Here's the [website](http://saturn.picoctf.net:52472/).  
>
> We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

None

## Summary

Instead of the absolute file path enter a relative one. Enter
```
../../../../flag.txt
```
to the input field and read the flag.


## Flag

<details><summary>Show flag</summary>

```
 picoCTF{7h3_p47h_70_5ucc355_32e3a320}
 ```

</details>
