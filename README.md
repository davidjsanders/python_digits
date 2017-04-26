# python_digits
This is an open source project and you are welcome to reuse and/or fork :) The objective behind this
repo is to provide a Python function which provides an object (a Digit) to represent an integer between
0 (zero) and 9 (nine). This is further extended by providing an object (a DigitWord) which represents
a collection of Digits, in a set sequence (e.g. 0421 would be a DigitWord with a length of 4 and containing
4 digits of the values: 0, 4, 2, and 1.)

The reason I created this package is for a cowbull game I have been developing which allows a series of digits
to be randomly generated and then for a user to guess each digit. If the guessed digit is in the right place,
then it's a bull; if the guessed digit is in the wrong place, then it's a cow. To aid this, the DigitWord
actually allows comparisons of multiple DigitWords and returns a list of DigitWordAnalysis (DWA) objects.
The DWA objects state the index (the position of the guessed digit), the digit (the guess, not the actual
digit), a match (True or False) indicator, an in word (True or False) indicator, and a multiple (True or
False) indicator which shows whether the guessed number actually occurred more than once.

## Installation
After forking this repository (or cloning using https), the package can be installed typing

```pip install .```

and will then be available to your Python environment. Virtualenv is recommended to avoid polluting your
Python environment.
