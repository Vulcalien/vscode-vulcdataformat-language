# python version: 2.7

import re
import os

def compact(regex):
    regex = regex.replace(' ', '')
    regex = re.sub('#.*\n', '', regex)
    regex = regex.replace('\n', '')
    return regex

file_path = os.path.join(os.path.dirname(__file__), 'everything_after_toplevel_is_closed.txt')

with open(file_path, 'r') as file:
    regex = file.read()
    print(compact(regex))
