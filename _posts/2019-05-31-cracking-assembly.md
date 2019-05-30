---
layout: post
title:  "Cracking software through Assembly code"
date:   2019-05-31 11:43:17
published: true
draft: true
---

*TLDR: I cracked a software by messing with its assembly code. Here is a story -including technical details- of how I did it.*

Last semester, the night of a COMP160 exam, instead of studying, I decided to take on a new fun challenge: I would try and develop a crack for some software! The idea is to alter the assembly code of a program in order to make it run without proper licensing. Assembly code is the code that is fed to the CPU that tells it what to do. In other words, it is the most low-level form of code that a human can look at and understand. Thankfully, I was familiar with Assembly thanks to COMP40, which is an awesome class at Tufts where students learn the details how computers work in the most low-level way. In one of the assignment, called the Bomb, students are handed an executable file, and no accompanying source code. The idea then is to use a disassembler program to read the binary instructions written in the executable and convert it to human-readable assembly. It just occured to me that what we did in that assignment is exactly what a person developing a crack would do: bypass and overcome checks instilled in a software in order to alter its behaviour. I was excited to start this projet mainly because I have no idea what I am doing, and I always looked at cracks as something magical that only geniuses can make. I also did not want to study for Comp160 exam but wanted to feel good about how I spent my time. Clearly, this project was the way to go!

The first step was choosing which software to crack. Personally, I would love to crack some super-famous software like Adobe Photoshop or Microsoft Word. However, these software were *probably* made to be hard to crack. I cannot expect myself to be able to crack them; I am just starting my career as a software cracker! I chose a more low-key yet useful software. I should not disclose its name, since it is *probably* illegal, and I don't want to go to jail yet. However, in this post, I will show everything about how I cracked it without showing any identifying information. In the following text, I will refer to the software as "X".

The next step was to find the executable associated with the software. Since I own a Mac, the structure of any application is more or less standard: the executable usually hides in `/Applications/X/X.app/Conents/MacOS/X`. This was exactly where I found the executable. Next, I ran the executable and took notes of its behaviour, looking for cues on how the software might have been written. When I run the software, it shows the following dialog:


{% include mailchimp.html source="cracking1" %}
