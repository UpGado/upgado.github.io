---
layout: post
title:  "Abstractions may not be so good"
date:   2020-06-27 03:10:00
published: true
draft: false
tags: opinion
---

This summer, I came across an opportunity to try and make impossible things happen as part of a software project. I said bring it on: I thrive on challenges! What I was trying to achieve is certainly possible in theory. In a world with no walls, it would be trivial to do. In practice, however, it is very hard and for the most part was thought to be an impossible task. The reason it is hard is because the way we write software has always not been perfect. It is a compromise between wanting to make progress and write complex software while also coming to terms with the limitations of the human brain. We invented programming languages not because they are useful for the computer, but because they help us humans a great deal with conceptualizing our thoughts and expressing them. However, what cost did we pay when we created programming languages?


Here is one: consider the fact that many programming languages exist and are in use today. Usually, If you write a program that uses one programming language, things are straightforward, and hopefully you have a good experience coding. However, the moment you write and connect multiple programming languages, things suddenly start looking ugly (and they do, no matter how hard you try). We spent thousands of hours building languages and erecting walls around them, and then we realize that what we built inside the walls is not sufficient, so we spend thousands of hours building bridges to other languages. Those bridges are usually brittle and require constant maintenance. In many cases, using those bridges introduces complexity that makes the developer sad.

Why is this the case?

Is this the best situation that we could hope for?

I find it strange. At the end of the day, all programming languages, high-level or low-level, boil down to the host machine's binary instructions. Why then can they not work together *just out of the box*? Did we shoot ourselves in the foot by making all those abstractions without keeping in mind having an inherent, cost less, way to keep them all connected?

We all heard the joke that "in computer science, all problems are solved by adding another layer of abstraction". Indeed, one big part of my CS education was to get students to think about writing good abstractions. Abstractions are powerful, because with good abstractions, solving complex problems can become a piece of cake. But the truth is abstractions only help us humans, not the machine. We are too stupid to keep hundreds of thousands of lines of code in mind simultaneously and thus we need abstractions in order to make anything useful. The machine does not care. Can we get the machine to tear down abstractions and just sort its way through a mush of code?

If only there was a magical way to confer universality and interoperability on all existing languages. In theory, it is possible. In practice, it may be too late.


{% include mailchimp.html source="abstractions1" %}
