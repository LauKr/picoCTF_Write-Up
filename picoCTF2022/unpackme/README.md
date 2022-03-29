# picoCTF 2022: unpackme

Author: LT 'syreal' Jones

![Reverse_Engineering category](https://img.shields.io/badge/category-Reverse_Engineering-red.svg)
![Score: 300](https://img.shields.io/badge/Score-300-brightgreen.svg)
![Solved](https://img.shields.io/badge/Solved-During_Competition-brightgreen.svg)

## Description
> Can you get the flag?  
> Reverse engineer this [binary](https://artifacts.picoctf.net/c/370/unpackme-upx).

<!--Artifact Files:
* [Artifact1]()
* [Artifact2]()
-->

### Hints

<details>
<summary>Hint 1</summary>
What is UPX?
</details>

## Summary

If we execute the program it asks for the authors favorite number.  
First we need to find out what [UPX](https://github.com/upx/upx) is. It is a executable file compressor, so we use it to decompress the original file.
This can be done via

```bash
upx -d -ounpacked unpackme-upx
```

where `-d` stands for _decompress_ and `-oFILE` sets the output to _FILE_. These commands can be found using `upx --help`.

As an output we get another executable. Here we start using a debugger, e.g. the _GNU Debugger_ [gdb](https://www.sourceware.org/gdb/).
We can start it via

```bash
gdb
```

and then load the extracted binary via the `FILE` command. Then we disassemble the main function:

<!--![usage of gdb](solve/use_gdb.gif)-->

```sh  <!--it's not sh, but for the color :)-->
$ FILE unpacked
$ disassemble main
```

As a result we get something like:


```
Dump of assembler code for function main:

   0x0000000000401e73 <+0>:      endbr64
   0x0000000000401e77 <+4>:      push     rbp
   0x0000000000401e78 <+5>:	  mov      rbp,rsp
   0x0000000000401e7b <+8>:	  sub      rsp,0x50
   0x0000000000401e7f <+12>:	 mov      DWORD PTR [rbp-0x44],edi
   0x0000000000401e82 <+15>:	 mov      QWORD PTR [rbp-0x50],rsi
   0x0000000000401e86 <+19>:	 mov      rax,QWORD PTR fs:0x28
   0x0000000000401e8f <+28>:	 mov      QWORD PTR [rbp-0x8],rax
   0x0000000000401e93 <+32>:	 xor      eax,eax
   0x0000000000401e95 <+34>:	 movabs   rax,0x4c75257240343a41
   0x0000000000401e9f <+44>:	 movabs   rdx,0x30623e306b6d4146
   0x0000000000401ea9 <+54>:	 mov      QWORD PTR [rbp-0x30],rax
   0x0000000000401ead <+58>:	 mov      QWORD PTR [rbp-0x28],rdx
   0x0000000000401eb1 <+62>:	 movabs   rax,0x3634376130486637
   0x0000000000401ebb <+72>:	 mov      QWORD PTR [rbp-0x20],rax
   0x0000000000401ebf <+76>:	 mov      DWORD PTR [rbp-0x18],0x67366563
   0x0000000000401ec6 <+83>:	 mov      WORD PTR [rbp-0x14],0x4e
   0x0000000000401ecc <+89>:	 lea      rdi,[rip+0xb1131]        # 0x4b3004
   0x0000000000401ed3 <+96>:	 mov      eax,0x0
   0x0000000000401ed8 <+101>:	call     0x410df0 <printf>
   0x0000000000401edd <+106>:	lea      rax,[rbp-0x3c]
   0x0000000000401ee1 <+110>:	mov      rsi,rax
   0x0000000000401ee4 <+113>:	lea      rdi,[rip+0xb1135]        # 0x4b3020
   0x0000000000401eeb <+120>:	mov      eax,0x0
   0x0000000000401ef0 <+125>:	call     0x410f80 <__isoc99_scanf>
   0x0000000000401ef5 <+130>:	mov      eax,DWORD PTR [rbp-0x3c]
   0x0000000000401ef8 <+133>:	cmp      eax,0xb83cb
   0x0000000000401efd <+138>:	jne      0x401f42 <main+207>
   0x0000000000401eff <+140>:	lea      rax,[rbp-0x30]
   0x0000000000401f03 <+144>:	mov      rsi,rax
   0x0000000000401f06 <+147>:	mov      edi,0x0
   0x0000000000401f0b <+152>:	call     0x401db5 <rotate_encrypt>
   0x0000000000401f10 <+157>:	mov      QWORD PTR [rbp-0x38],rax
   0x0000000000401f14 <+161>:	mov      rdx,QWORD PTR [rip+0xdd7b5]        # 0x4df6d0 <stdout>
   0x0000000000401f1b <+168>:	mov      rax,QWORD PTR [rbp-0x38]
   0x0000000000401f1f <+172>:	mov      rsi,rdx
   0x0000000000401f22 <+175>:	mov      rdi,rax
   0x0000000000401f25 <+178>:	call     0x420bd0 <fputs>
   0x0000000000401f2a <+183>:	mov      edi,0xa
   0x0000000000401f2f <+188>:	call     0x421070 <putchar>
   0x0000000000401f34 <+193>:	mov      rax,QWORD PTR [rbp-0x38]
   0x0000000000401f38 <+197>:	mov      rdi,rax
   0x0000000000401f3b <+200>:	call     0x42eec0 <free>
   0x0000000000401f40 <+205>:	jmp      0x401f4e <main+219>
   0x0000000000401f42 <+207>:	lea      rdi,[rip+0xb10da]        # 0x4b3023
   0x0000000000401f49 <+214>:	call     0x420e90 <puts>
   0x0000000000401f4e <+219>:	mov      eax,0x0
   0x0000000000401f53 <+224>:	mov      rcx,QWORD PTR [rbp-0x8]
   0x0000000000401f57 <+228>:	xor      rcx,QWORD PTR fs:0x28
   0x0000000000401f60 <+237>:	je       0x401f67 <main+244>
   0x0000000000401f62 <+239>:	call     0x45cdf0 <__stack_chk_fail_local>
   0x0000000000401f67 <+244>:	leave  
   0x0000000000401f68 <+245>:	ret    
End of assembler dump.
```

If we read through that assembler code we see the line
```   
0x0000000000401ed8 <+101>:	call   0x410df0 <printf>
```
which is used to call the `printf` function, the then the block
```
0x0000000000401ef0 <+125>:	call   0x410f80 <__isoc99_scanf>
0x0000000000401ef5 <+130>:	mov    eax,DWORD PTR [rbp-0x3c]
0x0000000000401ef8 <+133>:	cmp    eax,0xb83cb
0x0000000000401efd <+138>:	jne    0x401f42 <main+207>
```
which calls `scanf`, an input, and afterwards compares the register _eax_ to _0xb83cb_. If the two are not identical the program jumps to another section, omitting half of the program. This looks a lot like the _What is my favorite number?_ thing we get if we execute the program.  
If we look what _0xb83cb_ is in decimal, we get _754635_ as the result. Now we insert this number when executing the program and get the flag.

## Flag

<details><summary>Show flag</summary>

```
picoCTF{up><_m3_f7w_2fce46e8}
```

</details>
