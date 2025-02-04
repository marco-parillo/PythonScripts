#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    names = []
    boy_name_dict = {}
    girl_name_dict = {}
    with open(filename, 'rt', encoding='utf-8') as f:
        whole_file = f.read()
    year_match = re.search(r'Popularity\sin\s(\d+)', whole_file)
    if year_match:
        names.append (year_match.group(1))
    else:
        sys.stderr.write("no year found\n")
        sys.exit(1)
    name_tuples = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', whole_file)
#   name_tuples now holds ranknumber, boy's name, girl's name
#   Since we sort boys by rank and girls by name, we select the 0th element for boys, but the last element for girls
    for rank in name_tuples:
        boy_name_dict[rank[0]] = rank[1]
        girl_name_dict[rank[2]] = rank[0]
#   Print Boys and their ranks in Rank Order
    for rank in sorted(boy_name_dict.keys()):
        print (rank, boy_name_dict[rank])
#   Print Girls in Alphabetical Name Order
    for name in sorted(girl_name_dict.keys()):
        print (name, girl_name_dict[name])
    return
"""
Given a file name for baby.html, returns a list starting with the year string
followed by the name-rank strings in alphabetical order.
['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
"""
# +++your code here+++


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  extract_names(args[0])
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
  main()
