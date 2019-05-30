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

The next step was to find the executable associated with the software. Since I own a Mac, the structure of any application is more or less standard: the executable usually hides in `/Applications/X/X.app/Contents/MacOS/X`. This was exactly where I found the executable. Next, I ran the executable and took notes of its behaviour, looking for cues on how the software might have been written. When you first run the software, it shows the following dialog:

{% include figure.html width="30%" file="/imgs/cracking-1.png" %}

Ok. Dialogs probably mean an event loop that is exited once you click "Quit" or "OK". For example, after clicking "Quit", the code flows in the direction of exiting the program. Therefore, the other direction must be to continue the program (or at least that is what I would expect). Let's disassemble the executable and try and find if this hypothesis is true. I spent a couple of hours trying to find a good disassembler for MacOS. I tried Cutter mainly because it is open-source and community driven, but unfortunately it did not cut it. The executable was too big and the software was too laggy. I ended up using Hopper. Once I loaded the executable in Hopper, and let it run its analysis, I was faced with this:

{% include figure.html width="100%" file="/imgs/cracking-2.png" %}

Lots and lots of assembly code. Where do I start? At first, I was lost for hours trying to manually look into the assembly code, starting from the `main` function, which is where every UNIX program must start. However, even though the function was there, it was just too much to absorb. The amount of instuctions was so much that it was next to impossible to track the flow of the program up until itchecks for proper licensing. My next try was to use the search function by searching for words like "license" or "dialog". Fortunately, this yielded results:

{% include figure.html width="40%" file="/imgs/cracking-3.png" %}

In fact, I got so many results that I was surprised. All the labels were there, non-obfuscated, waiting for a patient hacker to read and figure out. One label was so obviously named `GetLicensedThisRun`. Contrast that to all the label names in the Bomb assignment, which were intentionally vague to not give away any information about the intent of the functions. Clearly the people who made this software did not make any effort to make it non-hackable. Nevertheless, it took me hours of searching, finagling and referring to assembly code cheat sheets until I figured out where the dialog code is:

```assembly
000adf25         call       __ZN3ADI17RunStandardDialogERKNS_6StringES2_S2_     ; ADI::RunStandardDialog(ADI::String const&, ADI::String const&, ADI::String const&)
000adf2a         movl       0xffffffc8(%ebp), %eax
000adf2d         addl       $0xfffffff4, %eax
000adf30         movl       %eax, 0x4(%esp)                                     ; argument "theValue" for method imp___symbol_stub__OSAtomicAdd32Barrier
000adf34         movl       $0xffffffff, (%esp)                                 ; argument "theAmount" for method imp___symbol_stub__OSAtomicAdd32Barrier
000adf3b         call       imp___symbol_stub__OSAtomicAdd32Barrier
000adf40         testl      %eax, %eax
000adf42         jne        $__ZN14CAFApplication5StartEv+16747
```

In retrospect, it is clear what this code might be doing. However, when I first looked at it, I was clueless. I can see that there is a `test` command followed by a conditional jump `jne`. However, I don't know what it is testing, or where it is jumping. In order to understand this, I decided to step into the code. I used `llvm` and placed a breakpoint at the address `000adf25`, which corresponds to `call`ing the dialog. After this, I would step into the code, instruction by instruction, and watch what the application does. It was a tedious process, but a straightforward one. I realized that the `call` to the dialog function is a blocking call that returns once the "Quit" button is clicked. Easy! This means that I do not need to look into what the dialog function does. Everything is happening at the top-level. The first few `mov`s I do not understand, but I expect them to fetch the result of the dialog and prepare it for some check. It turns out that the `jne` function jumps to an address that eventually closes the program. So in order to make that not happen, I could do multiple things. For example, inverting the condition (by changing `jne` to `je`) does the trick. I could also replace the `jne` with a `jmp` to the location that continues the program execution. Finally, I could also change the `jne` to a `nop`, which is the instruction for doing nothing.


{% include mailchimp.html source="cracking1" %}
