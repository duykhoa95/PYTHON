def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Print the first word after  popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Take in a full sentence and return the sorted words"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# from ex25 import * ==> print_last_word(...)
# import ex25 ==> ex25.print_last_word(...)

# re-import module
# Py3.4
## >>> import importlib
## >>> importlib.reload(ex25)
## 
# Py3
## >>> import imp
## >>> imp.reload(ex25)
## 
