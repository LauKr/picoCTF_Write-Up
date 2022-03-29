# picoCTF 2022: file-run1

Author: Will Hong

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 100](https://img.shields.io/badge/Score-100-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> A program has been provided to you, what happens if you try to run it on the command line? Download the program [here](https://artifacts.picoctf.net/c/313/run).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
To run the program at all, you must make it executable (i.e. `$ chmod +x run`)
</details>
<details>
<summary>Hint 2</summary>
Try running it by adding a '.' in front of the path to the file (i.e. `$ ./run`)
</details>

## Summary

Download the file, make it exectuable and run.

```bash
wget -N https://artifacts.picoctf.net/c/313/run
chmod u+x run
./run
```

## Flag

<details><summary>Show flag</summary>

```
picoCTF{U51N6_Y0Ur_F1r57_F113_2a4dec6a}
```

</details>
