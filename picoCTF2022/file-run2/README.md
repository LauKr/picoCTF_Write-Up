# picoCTF 2022: file-run2

Author: Will Hong

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program [here](https://artifacts.picoctf.net/c/356/run).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
Try running it and add the phrase "Hello!" with a space in front (i.e. "./run Hello!")</details>

## Summary

Download the file, make it exectuable and run with the argument "Hello!".

```bash
wget -N https://artifacts.picoctf.net/c/356/run
chmod u+x run
./run "Hello!"
```

## Flag

<details><summary>Show flag</summary>

```
picoCTF{F1r57_4rgum3n7_0097836e}
```

</details>
