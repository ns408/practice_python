# Python drill - 1

Credit: [Python Crash Course, 2nd Edition](https://nostarch.com/pythoncrashcourse2e/)

## Objective

- Setup environment
  - Suggestion
- Running snippets of Python Code
- Variables and Basic Data Types

### Setup environment

[pyenv installation](https://github.com/pyenv/pyenv#installation)
pyenv lets you easily switch between multiple versions of Python - without touching your primary python interpreter on you system.

```shell
pyenv install 3.6.5
pyenv versions

pyenv local 3.6.5 # will create a .python-version
python --version
```

If feeling adventurous:

```shell
pyenv install 3.7.6
```

#### Suggestion

[vscode](https://code.visualstudio.com/download)

### Running snippets of python code

- `python`
- `python -c 'print("ello wurld!")'`
- `echo 'print(5 + 5)' > /tmp/python.py; python /tmp/python.py`
- `python -i /tmp/python.py`
- `cd /tmp; python; import python`

### Variables and Basic Data Types

#### Variables

variable rules to keep in mind:

- Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.
- Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.
• Avoid using Python keywords and function names as variable names.
• Variable names should be short but descriptive.
• Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

Variables reference a certain value.

```python
myname = "<YOUR_NAME>"
print("My name is " + myname)
```

Multiple assignments

```python
a, b, c = 10, 100, 1000

for item in a, b, c:
    print(item)
```

#### Strings

A string is series of characters.
Quoted characters whether using single or double quotes are strings.

##### Methods

```python
"string".title()
"String".lower()
"string".upper()
' string '.strip()
```

Note:

Finding what methods can be used against objects:

```python
dir('string')
dir(str())
```

A much refined way. Courtesy of [stackoverflow](https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has)

```python
obj = ''
obj_methods = [method_name for method_name in dir(obj) if callable(getattr(obj, method_name))]
print(obj_methods)
```

Finding help:

```python
# what is this str()
help(str())
```

str() is a built-in function which instantiates string objects.

Question/todo: How do you reverse a string?

- Slicing

```python
'string'[::-1]
# length : end_position : step
```

- Loop
- Join

```python
''.join(reversed('this'))
str().join(reversed('this'))
```

##### Variables in Strings

In python, we get to use `f-strings` (format strings _before you think about fudge or fondue_). _Introduced in python3.6._

```python
first_name = "me"
last_name = "myself"
full_name = f"{first_name} {last_name}"

# or just
print(f"My name is {first_name.title()} {last_name.upper()}.")
```

This reminds me of dynamic variable names in bash which were so ugly: [stackoverflow](https://stackoverflow.com/questions/16553089/dynamic-variable-names-in-bash)

Assuming everyone knows about whitespace chars:

```python
print("Hi! My name is (what?)\n\tMy name is (who?)\n\tMy name is Slim Shady")
```

A bit about stripping (_whitespaces_):

```python
' this'.lstrip()
'that '.rstrip()
' what '.strip()
```

##### Numbers

_is z name of z game._

###### Integers

```python
2 + 3 * 15 / 25
2 ** 4

dir(1)
dir(int())

print(int(1.2))
```

BODMAS (Bracket, Of (power of), Division, Multiplication, Addition, Subtraction) may be the way in Maths but here we can enforce our rules using parentheses.

###### Floats

Decimal point thingies are floats.

```python
0.1 + 0.1
0.2 + 0.2
```

but wth is this:

```python
3 * 0.1
```

It has to do with how fractions get represented internally.

Snippet from python.org:

```code
Representation error refers to the fact that some (most, actually) decimal fractions cannot be represented exactly as binary (base 2) fractions. This is the chief reason why Python (or Perl, C, C++, Java, Fortran, and many others) often won’t display the exact decimal number you expect.
```

Reference:

- [docs.python.org](https://docs.python.org/3/tutorial/floatingpoint.html)
- [stackoverflow](https://stackoverflow.com/questions/39618943/why-does-the-floating-point-value-of-40-1-look-nice-in-python-3-but-30-1-doesn)

***Few more things***

division between any numbers (float or/and integers) will result in float.

```python
4 / 2
```

#### Constants

Python doesn't have built-in constant type but stick with using capital letters to show that value for that variable shouldn't change.

```python
I_AM="smart"

#or a more meaningful one:
MATH_PI=3.14
```

#### Comments

```python
# This is a single line comment.

"""
A multi-line
whackier
comment.
"""

print("""
Sometimes,
I do
this too,
just to be lazy with formatting
""")
```

#### Z Philosophy

```python
import this
```

**Now is better than never.**

#### Auxiliary

- Installing pyenv in zsh on macOS

```shell
brew install pyenv

# added the following to my ~/.zshrc file
export PATH=/usr/local/Cellar/pyenv/<version>/bin:$PATH
export PATH=$(pyenv root)/shims:$PATH

pyenv install 3.6.5
pyenv local 3.6.5
python --version # shows 3.6.5
pyenv local system
python --version # shows 2.7.10
```

- working with python3's venv for fun:

```shell
python3 -m venv .env
```

- making python shell interact better (preserve history and act kinda like bash)

```shell
pip install gnureadline

cat > ${HOME}/.pythonstartup.py <<EOF
try:
  #import readline
  import gnureadline
except ImportError:
  print("Module readline unavailable.")
else:
  import rlcompleter
  gnureadline.parse_and_bind("tab: complete")
EOF

echo "PYTHONSTARTUP=\"${HOME}/.pythonstartup.py\"" >> ${HOME}/.bash_profile
```
