# picoCTF 2022: RPS

Author: Will Hong

![Binary_Exploitation category](https://img.shields.io/badge/category-Binary_Exploitation-red.svg)
![Score: 200](https://img.shields.io/badge/Score-200-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.  
Connect to the program with netcat:
```sh
$ nc saturn.picoctf.net 53296
```
The program's source code with the flag redacted can be downloaded [here](https://artifacts.picoctf.net/c/447/game-redacted.c).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details><summary>Hint 1</summary>
How does the program check if you won?
</details>

## Summary

The program checks the win using the following code:

```C
if (strstr(player_turn, loses[computer_turn])) {
  puts("You win! Play again?");
  return true;
} else {
  puts("Seems like you didn't win this time. Play again?");
  return false;
}
```

We can see that it uses the function `strstr`, which finds the first occurrence of a substring in a sting. So if we enter `rockpaperscissors` it will always find the computers loosing command in our string.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{50M3_3X7R3M3_1UCK_8525F21D}
```

</details>
