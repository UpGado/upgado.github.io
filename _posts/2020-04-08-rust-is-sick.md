---
layout: post
title:  "Dump C for Rust"
date:   2020-04-08 02:21:10
published: true
draft: false
---

[Rust](https://www.rust-lang.org/) is a programming language for better "systems programming", which is a loose term that pretty much just means "coding in C/C++". We have all been told that "C is how the machine works", which is true in some sense. C code is closer to the machine than, say, Python. But there is no reason C should be the only contender to being the language closest to the machine. There is nothing that limits anyone from creating a language that is not C, but still is close to the CPU, and offers the same control and speed as C. The time is ripe for such language, and I think Rust is the best bet out there.

## The need for the something better

C/C++ are great and all, but they are pretty old. ANSI C was made in 1990, which is a long time ago. There is a lot of things that we learned since then that we can incorporate in our programming languages. Unfortunately, for issues of backwards-compatibility, it is not really possible to change C code standards now without messing up older programs. Of course, this is not an option, and so there are real limits to how much C can be changed.

C has a number of problems. There is no good, modern choice for packaging C code. There is no such thing as `pip` for C. Instead, you have deal with getting dependencies, making sure they are in the right place, and pulling your hair at compiler errors until your program finally compiles. Another issue that C does not do well is handling parallelism. It is well-known in computer science that getting multithreaded programs to work is quite hard, even for the smartest of us. The reason is that once you have many moving parts, you have to think so hard about preventing data races, which in many cases is hard to reason about and gives you a head ache.


Of course, C works, and is secure for many use cases when used by a careful programmer. But there is no reason a better system shouldn't exist. 


## What Rust offers

That system would not even let you compile unsafe code or code that has data races. That is the goal of Rust: a set of language rules and a compiler that makes sure code that compiles is code that is safe and doesn't have surprises at runtime.

In addition to offering the same level of control as C, Rust also offers some *really good* abstractions that boost productivity. In fact, in my experience, Rust productivity is much closer to Python's than to C. This is because of the amazing `crates.io` and `cargo` (which are analogs to Python's `pypi` and `pip`. So really, for many use cases, if you are a Python programmer and you switch to Rust, you are giving up a little bit of productivity, but you gain *so much* in performance and in control.

The only downside I noticed for Rust is the lack of online questions and answers. We all know that programmers like to search questions and find ready-to-copy code on Stackoverflow, or at least to find some hits that lead them in the right direction. In my experience, Rust's online QA is far from, say, Python's, or C's. However, that is to be expected, and will only get better with time. On the other hand, Rust's documentation is perfect. Sometimes, you just have to work a little hard to find the right page to read.

To conclude, I really do not see anymore why I would pick C over Rust for systems programming use cases. C just feels very ancient compared to Rust. If you like to use a language that has type inference, a great package manger, and a great compiler that offers native speed runtime, give Rust a shot.


Cheers.

{% include mailchimp.html source="rust2" %}
