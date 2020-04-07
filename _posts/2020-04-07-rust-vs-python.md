---
layout: post
title:  "Tips for learning a new programming language"
date:   2020-04-07 03:03:20
published: true
draft: true
---

Recently I finally got to give Rust, a relatively new programming language, a shot. My previous, naive approach to learning new programming languages was to just read the syntax and mimic it. After all, all programming languages are the same thing. They all have variables.. 

However, that is just a terrible way to learn a new language, because if you follow that way, you are most likely to learn nothing new, and you are likely to use the new language in the wrong way, although your code runs. Here is how I approached learning rust: the first step is to understand the "philosophy" of the language. What is it trying to do differently? What makes Rust Rusty, or Python Pythonic? These concepts might be hard to grasp at first, but they are most important to know. Learning a new language is not just learning new syntax, it is learning new ways to think and formulate solutions to any given problem. I watched tens of talks about Rust. Thankfully, since it is a relatively new language, many recent talks are given by the very people who wrote the language and have the best understanding of what Rust is all about.


The next step is to look at how the community likes to use the language and what kind of code patterns they recommend. For example, in Python, you should avoid using indices to loop over iterables. It is not Pythonic, and that is for a good reason because Python provides an alternative that is so much better and more readable. If you writing in C/C++/Java, however, using indices is the norm and is the only way of getting things done. This is why it is important to learn what code in the new language looks like. This can be done by watching talks that show code samples or best practices for a certain language.


Once you have done the past two steps, you can start writing your own projects. I highly recommend being suspicious of any code you write at first, and always trying to find code online (in the language documentation or Stackoverflow) that is trying to do something similar to what you are doing. You are likely to find new ways of doing things, and picking them up will be much easier. You can also refer to the general philosophy of the language and keep it in mind when you are designing both high-level or low-level aspects of your code. If something doesn't feel right and you feel that you are straining the language too much, this is a sign that there must be a better way. Go learn it!


{% include mailchimp.html source="rust1" %}
