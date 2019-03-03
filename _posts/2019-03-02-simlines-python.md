---
layout: post
title:  "Comp40 Simlines implemented in Python"
date:   2019-03-02 11:57:47
published: true
draft: true
---

For those of you who had of the experience of being a Tufts CS student, Comp 40 is a class that is hard to forget. This is the class where Tufts CS student learn to code in C, which is a very unforgiving, needy, and grumpy language. But somehow, it's fun! In Comp40, students work on weekly assignments, which are usually full-blown, command-line program that achieve something that is *actually* useful. One such program, called Simlines, is a program that detects similar lines in an arbitrary number of files. Most solutions to this problem involve reading files line by line and indexing them in some sort of a data structure. My partner, Roberto, and I spent at least 10 hours to write 280 lines of C code to achieve that task.

However, a few weeks after, our lecturer, Megan, stated that it is possible to code the same program in "2 lines of Python". I was intrigued by this statement. How many lines does it *actually* take to code Simlines in Python?

Luckily, on one abomination of a day, where I spent ten hours on a Biomedical Engineering lab report, I decided to take a break. My break was, aptly, to write Simlines in Python and see for myself the answer to my question.

# Python makes things really easy, at a cost

It took me 15 minutes to write Simlines in Python while in bed past 2am with an exhausted mind. Compared to writing in C, this is a piece of cake! No headaches, no pen and paper, no memory free, and no Hanson (oh yeah). This is 15 minutes in Python, compared to 10 hours in C ! Wow..

Well that is only part of the story; I won't do C justice unless I tell you that the Simlines C program was literally ten times faster than the Python one. Since, Python is an interpreted language, it is impossible for it to be faster than a compiled language such as C, at least in a simple I/O program such as Simlines. Anyhow, this one experience taught me that programming "comp sci programs" in Python is actually easier than it seemed. What is scary, in fact, is that you can do it with almost no preparation or prior thought, as opposed to hours of thinking and writing diagrams if you are writing in a low-level such as C or C++. Therefore, I do intend to write Comp40 assignments in Python as the semester progresses. I think it is gonna be a fun learning experience!

# Code

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
