#!/bin/bash
wget -N https://artifacts.picoctf.net/c/356/run
chmod u+x run
./run "Hello!"| tee flag.txt
