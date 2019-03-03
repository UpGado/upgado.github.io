---
layout: post
title:  "Comp40 Simlines implemented in Python"
date:   2019-03-02 11:57:47
published: true
draft: true
---

For those of you who had of the experience of being a Tufts CS student, Comp 40 is a class that is hard to forget. This is the class where Tufts CS student learn to code in C, which is a very unforgiving, needy, and grumpy language. But somehow, it's fun! In Comp40, students work in weekly assignments, which are usually full-blown, command-line program that achieve something that is *actually* useful. One such program, called Simlines, is a program that detects *similar* lines in an arbitrary number of files. Most solutions to this problem involve reading files line by line and indexing them in some sort of a data structure. My partern, Roberto, and I spent at least 10 hours to write 280 lines of C code to achieve that task.

However, a few weeks after, our lecturer, Prof. Megan, stated that it is possible to code the same program in "2 lines of Python". I was intrigued by that statement. How many lines does it *actually* take to code Simlines in Python?

Luckily, on one abomination of a day, where I just spent ten hours on a lab report, I decided to take a break. My break was, aptly, to write Simlines in Python and see for myself the answer to my question.

# Python really makes things easy, at a cost

Here is Simlines implemented in Python:

```python
#!/usr/bin/env python3

# Simlines in Python
# Ahmed Gado
# Created in <15 minutes
# 03/01/2019 2:43 AM

import sys
from collections import defaultdict

INDEX = defaultdict(list)

def main():
    files = sys.argv[1:]
    files.reverse()
    for filename in files:
            index(filename)

    first = True
    for line, occurences in INDEX.items():
        if len(occurences) == 1:
            continue
        if first:
            first = False
        else:
            print()
        print(line)
        for filename, linenum in occurences:
            print("%-20s %7d" % (filename, linenum))

def index(filename):
    linenum = 1
    with open(filename, "r") as f:
        for line in f.readlines():
            cleaned = clean_line(line)
            if cleaned != '':
                INDEX[cleaned].append((filename, linenum))
            linenum = linenum + 1

def clean_line(line):
    cleaned = ''
    add_a_space = False
    for char in line:
        if ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
            if add_a_space:
                cleaned += ' '
                add_a_space = False
            cleaned += char
        else:
            add_a_space = True
    return cleaned

if __name__ == "__main__":
    main()
```
{% include mailchimp.html source="python1" %}
