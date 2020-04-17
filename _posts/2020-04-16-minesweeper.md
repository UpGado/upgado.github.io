---
layout: post
title:  "Minesweeper reinforcement learning written in Julia"
date:   2020-04-16 20:03:50
published: true
draft: true
---

Remember the legendary Minesweeper?

{% include figure.html file="/imgs/minesweeper-1.jpg" description="A classic" %}

Well, I thought that it would be cool to write a program that can play Minesweeper. And then I thought: I don't want to think hard about writing such program. This game usually requires a fair amount of thinking, including lots of probabilities and considering multiple scenarios at once. It is fairly complex, and even though I can sometimes do that subconsciously in my head, it is too much work to examine my thinking and replicate it in code. Instead, let's just leave it to the computer to figure out how to best play Minesweeper. In other words, this is not A Minesweeper solver, it is a program that generates solvers, with no prior human knowledge given to it. It is just easier for me this way..

{% include mailchimp.html source="minesweeper1" %}
