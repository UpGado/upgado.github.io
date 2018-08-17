---
layout: post
title:  "Shower thoughts: Simulink model for a bathtub (1)"
date:   2018-08-16 14:44:00
published: true
draft: true
---

# Intro
This summer I had a new, relaxing hobby. I lie in the bathtub for hours with my eyes closed. To relax, I don't think about anything: complete silence in my mind. Well, still my senses were working, and they were telling me that the water is getting colder. I wondered if there is something that could be done about it? It's a classic bathtub and there is no fancy heating elements, just a water tap with adjustable temperature and a valve to drain the water out. The problem was quite interesting for my curious mind and I thought it'd be fun to solve it. Here, I show my thought process and how I ended up making an accurate, well-behaved simulation for a bathtub.

# Bathtub as a system

** Defining goals **

The first and foremost step for defining a model is to determine its goals as concisely as possible. From my experience working on diverse projects, goals are valuable because they help you avoid any kind of existential crisis while working on a project. Therefore, when defining goals it is important to state what you're really after, the essence and true value of your product. The more concise and focused the goals are, the more smooth your experience will be developing a project. Moreover, when you get faced with design choices (and you will), goals can serve as guidelines that aid decision-making.

The goals of this project are:

- Define an accurate, well-behaving model for the relevant features of a bathtub. (this gets tackled in this post)
- Use the model to test and develop a strategy to:
	- Keep temperature of the water as close as possible to a specified desired value.
	- Maximize water freshness.
	- Keep water level at a specified desired level.

** A diagram **

I started by drawing a diagram that shows the key parts of the bathtub system, the important variables that describe their state and their behaviour, and the processes through which they interact.


{% include figure.html file="/imgs/simulink-1.png" description="Figure 1: Diagram of the system" %}

I think the diagram is mostly self-explanatory, so I won't repeat information just for the sake of time. It is worth mentioning that the knob positions are represented as numbers lying between 0 and 1. For example, an output knob that is open all the way is represented as 1, and a knob that is completely closed is 0. For the temperature knob, "hot" is 0 and "cold" is 1. As we will see, this simplifies the maths considerably later. Also not mentioned in the diagram are important constants that represent the system such as the physical dimensions of the bathtub, the water output rate of the tap, and the water drain rate. These numbers are indispensable for getting a good accuracy for the model, so I made sure to measure them as accurately as possible. Here is a comprehensive list of the variables and constants relevant for this model:

{% include figure.html file="/imgs/simulink-2.png" description="Figure 2: Variables of the system" width = "40%" %}

Next, we model the processes through which the key parts interact. The water tap provides the bathtub with water at a specific rate. To determine this rate, we assume that the water tap works in a linear fashion: the water output varies linearly with the output knob rotation. Moreover, we assume that the maximum water output depends on the temperature the tap is set to (i.e: the tap has provide different amounts of "hot" and "cold" water). If this mixing happens in a linear fashion (which it should because it's just a valve), the maximum water output rate at the current temperature can be calculated by linear interpolation. $ WO $ can then be mathematically determined as:

$$ WO(t) = P.O(t) * [ (1 - P.TC(t)) * (P.HO) + (P.TC) * (P.CO)] $$

# "Coding" in Simulink
First, I chose Simulink as the platform to define and simulate this system. I chose it mainly because I wanted to learn to use it. It also fits nicely with Matlab, which I use on a daily basis. So, it is kind of an arbitary choice. If there is another software you recommend me to use, let me know!


{% include mailchimp.html source="simulink1" %}
