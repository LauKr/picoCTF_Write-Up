# picoCTF 2022: Local Authority

Author: LT 'syreal' Jones

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you get the flag? Go to this [website](http://saturn.picoctf.net:50959/) and see what you can discover.

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
How is the password checked on this website?
</details>

## Summary

Go to website, try to log in with Inspector, see Login Failed and in inspctor <script src="secure.js"> </script>. Go to secure.js ->
```js
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}

```
-> login -> flag

## Flag

<details><summary>Show flag</summary>

```
picoCTF{j5_15_7r4n5p4r3n7_b964a657}
```

</details>
