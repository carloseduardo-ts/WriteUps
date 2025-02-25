# Verify

This challenge provides very files and a script to decrypt your content. I made a shell script to go through all the files.

```shell
$ for file in files/*; do ./decript.sh $file; done
```

# Scan Surprise

This challenges provides an image with a qrcode, i used zbarimg to decode and see the string

```shell
$ zbarimg flag.png
```

# Binary Search

This challenge gave us a shell script that chose a random number between 1 and 1000 and gave us 10 chances to guess it. I made a Python script to find the number using binary search.

You can access the script [here](./binarySearch.py)


