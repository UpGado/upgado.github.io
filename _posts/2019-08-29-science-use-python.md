---
layout: post
title:  "Why the science community should write better code"
date:   2019-08-29 11:29:19
published: true
draft: true
---
For the past 2 years now, I have been working at an academic research lab at Tufts University. Since my lab specializes, among other things, in microscopic biomedical imaging, we generate *many* images. Those images are then analyzed to conclude some medically-relevant information. Of course, data analysis of microscopic images is impossible to do by hand, so it is all programmed (yay!). What is not so yay, however, is that the code used for this analysis is very badly written. It is very much what you would describe as "spaghetti code", except it's more of a spaghetti-meatball-dish-smushed-and-splattered-on-the-floor. Moreover, the problem of bad code does not just affect my lab, it actually plagues the whole scientific community.

Who cares? you might ask. After all, the focus of the scientific community should be to advance the actual science, not the quality of the code that they write. In other words, the data analysis code is just a means to an end. As long as you correctly analyze the data, does it matter what pile of code you accumulate to achieve that?

The answer is a bold **YES**. After all, let's not forget that the main reason programmers try to write good code is simply to improve productivity. Of course, scientists care about their productivity too (results, results, results!). However, since they are so focused on the science, they don't realize the benefits they could get if they invest in writing good code for their data analysis. The benefits that I promise include the traditional benefits that affect any programmer: a code base that is more pleasing to the eye, and a clear code behaviour that does not make you want to pull your hair. It also includes saving literal tens of hundreds of hours of human time: time that could be spent on something more productive that a computer couldn't do by itself, such as advancing science!

## The scientist's mindset
Scientists are busy people: they already have to deal with literature search, designing their experiments in order to obtain sound results and figuring out why the cells they have been culturing for weeks are suddenly dying. To them, they go through all that trouble just to obtain some measurements, which are colloquality called results. Results are the holy grail of science. Once you have acquired the results, a scientist rushes through the data analysis and hope that it tell them what they wish to hear, the sought-after conclusion. To the scientist, data analysis might in fact be the least important piece of the puzzle.

However, in my experience, scientists spend *a lot* of their time just trying to get the data analysis to work. This time could in fact be longer than the time it takes to complete all the other steps combined. It is also associated with a lot of frustration and shoutings such as "this is not working!", "aaargh", and "i should get an undergrad to do this for me". The reason the scientists don't have a good time writing code is that they often shoot themselves in the foot doing all sorts of bad coding habits. Since they are so focused on the science, they don't realize that, spending a little bit of time writing good, reusable code *will* save them hours in the future. This is my rule of thumb: write good code often enough that it becomes a habit, and soon enough, it will be harder to write bad code than to write good one. If some code is giving you trouble, sit back and rethink how you might write it in a better way. This little and incremental investment will compound over time, and soon enough you will be much quicker at writing good code than if you did not stop and rethink your bad code.

## How exactly might we improve code

So far, we have been broad and theoritical. Let's get technical and get our hands dirty with some code tips.
## Let's use Python instead

{% include mailchimp.html source="scienceusepython1" %}
