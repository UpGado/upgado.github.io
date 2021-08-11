---
layout: post
title:  "What I learned after 1 year as a software engineer"
date:   2021-06-06 12:39:59
published: true
draft: true
---

It's time. I have officially spent more than one year working as a professional software engineer! I have learned a TON TON during my job. Like, soft stuff, hard stuff, code stuff, and cloud stuff. Before this job, I had only coded in hobby or academic settings, which are _so_ different from what a real world job as a software engineer demands. Here is what I learned:


### It's not just about code

You would think a software engineer's main job is to write code, but you're only 25% correct. In reality, writing code was the _easiest and least time-consuming_ part of my job. What actually took time and effort was the stuff that comes before writing code: thinking about the problem and designing a good solution. For example, if you are adding a new feature to some existing application, you have to ask yourself the following questions:

* Where in the application do you add it?
* How are responsibilities assigned to the different parts of the system such that this feature works? The days of monolithic software are gone. Now, most systems are distributed systems. This is part of so-called "modernization" and it is happening for a variety of reasons beyond the scope of this post. As a result of modernization, the software you write will rarely be completely isolated. Most of the time, your software will need to use another component to function correctly. To implement some feature, you will have to change multiple code bases of different services that together make that feature happen, in a divide-and-conquer manner. Correctly dividing the problem into small logical pieces is something that can make a HUGE difference in the quality of the overall product.
* How do you ensure this feature is flexible enough to accommodate future requirements? This one is more of an art. I have to admit: I haven't exactly mastered this. But it is important because requirements _will_ change in the future and depending on how you design your software, you will have to do either a great amount of work, or little-to-no work.
* 10 years from now, will your implementation continue to work? Believe it or not, but software is in fact very fragile. Anything that you can't control can and will change at some point, leaving your software in a broken state. This especially applies to web software! Are you using some third party API? well, it will be deprecated or completely removed at some point in the future. You might want to change this API provider later. Any software you write should be written with this in mind.
* Could we design this feature in a way that turns 3 months of work into just 2 weeks? You would be surprised by often this can be achieved. By simplifying a key component of your implementation strategy, you can halve the amount of work you have to do. This could also be done by reusing existing pieces of code, either in your organization's code base or by using third-party code.

These are all questions that have nothing to do with code, computer science, or your ability to figure out fast algorithms. But they are issues that I quickly realized that a good software engineer pays attention to, and learns to have a good intuition for. I didn't learn this in class, but this is the stuff that sets apart talented programmers from game-changing ones. Thinking about the high-level and the _why_ is key to innovation and simplification, while just looking closely at the code will get you nowhere. It might simply just earn you a paycheck.

### Nothing is well-defined


### There is no substitute for writing good tests


{% include mailchimp.html source="softeng1" %}
