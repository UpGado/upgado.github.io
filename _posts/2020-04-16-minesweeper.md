---
layout: post
title:  "Minesweeper reinforcement learning written in Julia"
date:   2020-04-16 20:03:50
published: true
draft: true
---

Remember the legendary Minesweeper?

{% include figure.html file="/imgs/minesweeper-1.jpg" description="A classic" width="60%" %}

Well, I thought that it would be cool to write a program that can play Minesweeper. And then I thought: I don't want to think hard about writing such program. This game usually requires a fair amount of thinking e.g.: lots of probabilities and considering multiple scenarios at once. It is fairly complex, and even though I can sometimes do that subconsciously in my head, it is too much work to examine my automatic thinking, let alone replicate it in code. Also if we do it that way, where is the fun? Instead, let's just leave it to the computer to figure out how to best play Minesweeper. In other words, this is not a Minesweeper solver. This is a program that generates a solver by playing the game on its own and figuring out how best to win. It is just easier this way.

## Why this is easier than many other games

This concept of programs playing games and learning on their own is called reinforcement learning. Great feats have been accomplished in this field including, for example, generating a [Dota 2 AI](https://openai.com/projects/five/) that beat the top human players. Now, I should make it clear that Minesweeper is, from a reinforcement learning perspective, a very simple game. For starters, there is only one player, and the logic of the game is very straightfoward: avoid clicking a bomb until you have clicked all non-bombs. In addition, when considering whether or not to click a certain square, you only need to consider its local neighbourhood, instead of the whole map. Finally, the game can safely be played in a "greedy" way. In general terms, this means that to solve a game, it is okay to favor short-term fullfillment, because short-term fullfillment leads to long-term fullfillment. This is not always the case (e.g.: life). But in Minesweeper, this is the case: clicking *any* square that you know is not a bomb will bring you closer to solving the puzzle, and cannot hurt you in the future. This will turn out to be a huge factor in how simple our reinforcement learning approach can be.

## Problem formulation

I am sure there are many algorithms out there that you can plug-and-chug into this game, but again, that would not be fun. Let's make our own reinforcement learning algorithm.

{% include mailchimp.html source="minesweeper1" %}
