# picoCTF 2022: SQLiLite

Author: Mubarak Mikail

![Web_Exploitation category](https://img.shields.io/badge/category-Web_Exploitation-red.svg)
![Score: 300](https://img.shields.io/badge/Score-300-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you login to this website?
> > You'll need to start an instance.

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
admin is the user you want to login as.
</details>

## Summary

This challegne can be solved using a SQLinjection. To log in we use some username and password to see what happens.  
The login fails and we get a look at the SQL query. Now we can think of a way to get a SQL command injection. Something like
`' OR 1=1--`.  

Explanation: `'` ends the input, `1=1` adds an additional statement that is always true and `--` starts a comment, so everything behind that will be ignored.

As soon as you see the text _Logged in! But can you see the flag, it is in plainsight._ you've got it. To see the flag just have a look at the html source, it's hidden there.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{L00k5_l1k3_y0u_solv3d_it_147ec287}
```

</details>
