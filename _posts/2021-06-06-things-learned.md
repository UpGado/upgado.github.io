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

* **Where in the application do you add it?**
* **How are responsibilities assigned to the different parts of the system such that this feature works?** The days of monolithic software are gone. Now, most systems are distributed systems. This is a part of so-called "modernization" and it is happening for a variety of reasons beyond the scope of this post. As a result of modernization, the software you write will rarely be completely isolated. Most of the time, your software will need to use another component to function correctly. To implement some feature, you will have to change multiple code bases of different services that together make that feature happen in a divide-and-conquer manner. Correctly dividing the problem into small logical pieces is something that can make a HUGE difference in the quality of the overall product.
* **How do you ensure this feature is flexible enough to accommodate future requirements?** This one is more of an art. It is important because business requirements _will_ change in the future and depending on how you design your software, you will have to do either a great amount of work, or little-to-no work.
* **10 years from now, will your implementation continue to work?** Software is very fragile. Anything that you can't control can and will change at some point, leaving your software in a broken state. This especially applies to web software! Are you using some third party API? well, it will be deprecated or completely removed at some point in the future. You might want to change this API provider later. Any software you write should be made with this in mind.
* **Could we design this feature in a way that turns 3 months of work into just 2 weeks?** You would be surprised by often this can be achieved. By simplifying a key component of your implementation strategy or even the business requirements, you can halve the amount of work you have to do. This could also be done by reusing existing pieces of code, either in your organization's code base or by using third-party code.

These are all questions that have nothing to do with code, computer science, or your ability to figure out fast algorithms. But they are issues that I quickly realized that a good software engineer pays attention to and learns to have a good intuition for. I didn't learn this in class, but this is the stuff that sets apart talented programmers from game-changing ones. Thinking about the high-level and the _why_ is key to innovation and simplification, while just looking closely at the code will get you nowhere. It might simply just earn you a paycheck.

### No problem is well-defined

During my Computer Science classes in college, all project requirements were very clear. We had "specs" that completely described everything to be expected from the program, including even how it reacts to bad or unexpected input. During a job, you will never receive a project that is as clear. In fact, in my job, the requirements being asked were very, very vague. This was great for me, because it gave me lots of freedom and space to apply my creative process and design things the way I want. Being comfortable with a vague requirement is something that takes time, but is necessary if you are to grow as an engineer and assume higher, more impactful positions. A good work environment will provide you with varying degrees of vagueness in the problems you work on. Strict requirements were also helpful because they allowed me to write pedantic software that adhere to a standard. But if I have to choose, I would always take vague, exciting problems over mundane, clear ones.

### There is no substitute for writing good tests

 I have to admit: I wasn't exactly passionate about writing tests. I always thought they were a distraction from the "fun stuff". Well, it is okay to think that way because that's the naive thinking. In reality, once something you wrote breaks, you will understand that test are **essential**! To understand why that is, here are a few lessons I learned:
 
* If you are making a new feature, tests are literally the proof that the feature works. Without that proof, you will leave it to your customers to find out if the feature works or not, which is not what you want.

* Thorough testing will always help you gain a deeper understanding of your solution, and it often even reveals blind spots in your thinking. I hated how my college made me test so many edge cases in my project code. But in hindsight, they couldn't have been more correct.

* Tests live *forever*! They can run until the end of time, ensuring that something will always work in the future. This is huge! People will come and go. Software will be written, modified, re-written, and deleted. But tests are there to stay. They will alert whenever your feature stops working even after you had left that organization for years. This point is hard to grasp until you work on something for more than six months and you realize that indeed, your memory cannot hold all the details of a certain problem. But tests can.


With this, I am happy to end the first chapter of my professional life and share what I learned with you all. My next job will be somewhere very exciting, and I hope to keep posting here with things I learn along the way.

{% include mailchimp.html source="softeng1" %}
