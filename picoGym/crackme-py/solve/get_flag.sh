wget -N https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py
sed -i '$ d' crackme.py  # delete last line in python code which is useless and clutters the output
echo "decode_secret(bezos_cc_secret)" >> crackme.py  # add new line to python code to decode the secret
python3 crackme.py | tee flag.txt
