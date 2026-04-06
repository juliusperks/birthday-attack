This is an implementation of a classic birthday attack with a real and fake confession file. 

1) Copy a real confession file and a fake confession file into the confessions/ directory.

2) Run the program with:

```bash
python3 main.py
```

3) Check the CLI output that it shows that there are similar digits, the default is 10 lines and 2 digits.

4) Use cli flags to check for longer matches:

```bash
python3 main.py --digits=7 --lines=20
```