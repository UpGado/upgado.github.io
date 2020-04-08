---
layout: post
title:  "Dump C for Rust"
date:   2020-04-08 02:21:10
published: true
draft: true
---

[Rust](https://www.rust-lang.org/) is a programming language for better "systems programming", which is a loose term that pretty much just means "coding in C/C++". We have all been told that "C is how the machine works", which is true in some sense. C code is closer to the machine than, say, Python. But there is no reason C should be the only contender to being the language closest to the machine. There is nothing that limits anyone from creating a language that is not C, but still is close to the CPU, and offers the same control and speed as C. The time is ripe for such language, and I think Rust is the best bet out there.

## The need for the something better

C/C++ are great and all, but they are pretty old. ANSI C was made in 1990, which is a long time ago. There is a lot of things that we learned since then that we can incorporate in our programming languages. Unfortunately, for issues of backwards-compatibility, it is not really possible to change C code standards now without messing up older programs. Of course, this is not an option, and so there are real limits to how much C can be changed.

C is good and all, but it has many problems. There is no good, modern choice for packaging C code. There is no such thing as `pip` for C. Instead, you have deal with getting dependencies, making sure they are in the right place, and pulling your hair at compiler errors until your program finally compiles. Another issue that C does not do well is handling parallelism. There is well-known in computer science that getting multithreaded programs to work is quite hard, even for the smartest of us. The reason is that once you have many moving parts, you have to think so hard about preventing data races, which in many cases is hard to reason about and gives you a head ache.


Of course, C works, and is secure for many use cases when used by a careful programmer. But there is no reason a better system shouldn't exist. That system would not even let you compile unsafe code or code that has data races. That is the goal of Rust: a set of language rules and a compiler that makes sure code that compiles is code that is safe.
