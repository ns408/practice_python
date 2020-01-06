#!/usr/bin/env python3
# All of this cause I wanna be lazy.
# That lil change down there will allow me to interact better with python
# interpreter.
# It will allow tab completion, history etc.

print("""
brew install pyenv readline

#List python versions
pyenv install -l
pyenv install 3.6.5 # Using this version as an example
""")

print("""
# Specify this in your ~/.bashrc
# Not coding this as a function cause I use a different directory structure
[[ -f ${HOME}/.pythonstartup.py ]] && \
    export PYTHONSTARTUP=${HOME}/.pythonstartup.py
""")

print("""
# Create "${HOME}/.pythonstartup.py" with:

try:
  import gnureadline
except ImportError:
  print("Module readline unavailable.")
else:
  import rlcompleter
  gnureadline.parse_and_bind("tab: complete")
""")
