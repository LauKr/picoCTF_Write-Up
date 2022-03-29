#!/bin/bash
wget -N https://artifacts.picoctf.net/c/313/run
chmod u+x run
./run | tee flag.txt
