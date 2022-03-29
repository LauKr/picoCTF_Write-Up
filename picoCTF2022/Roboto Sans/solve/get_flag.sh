#!/usr/bin/env bash
wget -N http://saturn.picoctf.net:57329/js/myfile.txt
mv myfile.txt flag.txt
cat flag.txt
