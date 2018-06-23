---
layout: post
title:  "Finding the Best Deal on Food using MATLAB"
date:   2018-06-22 23:00:00
published: true
---

Truth is, everybody has their preferences when it comes to the food they eat. Yet, we (at least broke college students) agree that the food you eat daily shouldn't break the bank. Well.. If you eat nothing, you do a great job saving but not so-great one at staying alive. To stay healthy, you also have to get the nutrients you need in the optimal proportions or at least be close enough (aka you can't rely on just food X as the source of calories). I am no nutritionist but I can tell that **buying food is an optimization problem**: a problem that you, aware or not, engage with everytime you choose what to eat. So why not optimize your choice?

"Okay, but how do you do that?" is the question I will try to answer here in an accessible, enjoyable way! You can always use a pen and paper and write down numbers and calculations, but that is boring. What if you can write a program, have fun while doing so, and then just plug-and-chug later? In this post, I will explain one way such program might work. For the sake of the nontechies, I won't include code here, but it is available at the end if you want to take a look 😉.

As with any problem, we have to make some solid, non-redundant definitions. First, we start by defining amount of calories that you need per day (*Daily Calories*). **Our bodies are different**, so feel free to do some research to find what best suits your lifestyle. The U.S. Office of Disease Prevention and Health Promotion (aka the experts) have put together [guidelines](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/) that may help you determine the "right" number for you.

Next, we break down the daily calories into the main nutrients your body needs

{% include figure.html file="https://scontent.fnyc1-1.fna.fbcdn.net/v/t1.0-9/35972709_1964749230244402_345047270149849088_o.jpg?_nc_cat=0&oh=68c2f15de526a094e605d36c7bc3f8a7&oe=5BEB3B2F" description="Cool Figure 1: a decree by the might king" %}