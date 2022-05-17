# Custom Combos Wordlist Generator in Python

It generates custom combos (like "username:password") wordlist from two text files.  

Generated wordlist example:

```
admin:bird
admin:pass1
admin:password
chris:bird
chris:pass1
chris:password
michael:bird
michael:pass1
....
```

<br />

## Install & Run

```sh
git clone https://github.com/hideckies/gencombos.git
cd gencombos
pip3 install -r requirements.txt
python3 gencombos.py <wordlist1> <wordlist2> <output>
```

<br />

## Usage

```sh
python3 gencombos.py usernames.txt passwords.txt combos.txt
# or
python3 gencombos.py -w1 usernames.txt -w2 passwords.txt -o combos.txt
```

<br />

## Help

```sh
python3 gencombos.py --help

# --------------------------------------------

NAME
    gencombos.py - Custom Combos Wordlist Generator

SYNOPSIS
    gencombos.py W1 W2 O

DESCRIPTION
    Custom Combos Wordlist Generator

POSITIONAL ARGUMENTS
    W1
        Type: str
        Wordlist 1 - A wordlist file for the left side.
    W2
        Type: str
        Wordlist 2 - A wordlist file for the right side.
    O
        Type: str
        Output File - Specify the name of the output file.

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

<br />