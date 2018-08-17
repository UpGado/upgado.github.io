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

I think the diagram is mostly self-explanatory, so I won't repeat information just for the sake of time. It is worth mentioning that the positions of the knobs are represented as numbers lying between 0 and 1. For example, an output knob that is open all the way is represented as 1, and a knob that is completely closed is 0. For the temperature knob, "hot" is 0, "cold" is 1 and any setting in between is a number between 0 and 1. As we will see, this simplifies the maths considerably later. Also not mentioned in the diagram are important constants that represent the system such as the physical dimensions of the bathtub, the water output rate of the tap, and the water drain rate. These numbers are indispensable for getting a good accuracy for the model, so I made sure to measure them as accurately as possible. Here is a comprehensive list of the variables and constants relevant for this model:

{% include figure.html file="/imgs/simulink-2.png" description="Figure 2: Variables of the system" width = "40%" %}

** Maths and Physics **

Next, we model the two processes through which the parts interact. Firstly, The water tap provides the bathtub with water at a specific rate. To determine this rate, we assume that the water tap works in a linear fashion: the water output varies linearly with the output knob rotation. Moreover, we assume that the maximum water output depends on the temperature the tap is set to (i.e: the tap has provide different amounts of "hot" and "cold" water). If this mixing happens in a linear fashion (which it should because it's just a valve), the maximum water output rate at the current temperature can be calculated by linear interpolation, which is the complex-looking part of the otherwise-simple formula:

$$ P.WO(t) = P.O(t) * [ (1 - P.TC(t)) * (P.HO) + (P.TC) * (P.CO)] $$

Second is the water drain problem, which is quite simple if we consider the bathtub as an open system. Total mass is conserved and total energy of the water is conserved. When an amount of water drains out of the bathtub, its gravitational potential energy is converted into kinetic energy.

$$ GPE = KE $$

$$ mgh = 0.5mv^2 $$

$$ 2gh = v^2 $$

$$ v = sqrt(2gh) $$

Interestingly, the velocity of the water leaving the bathtub is independent of the size of the water drain. Moreover, using this velocity, we can calculate the rate at which water leaves the container by taking the product of the velocity of water (m/s) and the cross sectional area of the drain (m2):

$$ D.WO = D.A * sqrt(2gh) $$

Then, we multiply this value by the position of the drain knob, which effectively reduces the area of the drain:

$$ D.WO = D.O * D.A * sqrt(2gh) $$

Finally, we use these two water volume rates to calculate the volume of the water in the bathtub. This is done by integrating the difference between the two values by time:

$$ B.V = \int_{t=0}^{t} P.WO(t) - D.WO(t)dt $$

Now, we have all the equations that describe the system and allow us to calculate the volume of water in the bathtub based on the water tap and water drain behaviours, even if they change over time. Additional equations were used to calculate the temperature of the water, but they won't be included here for time's sake.

# "Coding" in Simulink
I chose Simulink as the platform to define and simulate this system. I chose it mainly because I wanted to learn to use it. It also fits nicely with Matlab, which I use on a daily basis. If there is an alternative software you recommend me to use, let me know!

Simulink uses graphical block-based programming, which I used to hate judging from experience with LabVIEW. However, I have come to realize how powerful this technique is when developing complicated systems, where the connections between individual blocks are more important than what the individual blocks do. I went ahead and added three subsystems: the water tap, the bathtub, and the water drain. I implemented the equations above by connecting the right blocks together. This part was a bit lame because you can't enter Maths expressions directly; instead you have to build these expressions from the most basic Maths functions. Thankfully, integration was already a prebuilt block.

The following is the final product:

{% include figure.html file="/imgs/simulink-3.png" description="Figure 3: Simulink system model" %}

{% include mailchimp.html source="simulink1" %}
