---
layout: post
title:  "Finding the Best Deal on Food using MATLAB"
date:   2018-06-22 23:00:00
published: true
---

Everybody has their own preferences when it comes to the food they eat. Yet, we (at least broke college students) agree that the food you eat daily shouldn't break the bank. Well.. If you eat nothing, you do a great job saving but not so-great one at staying alive. To stay healthy, you also have to get the nutrients you need in the optimal proportions or at least be close enough (aka you can't rely on just food X as the source of calories). I am no nutritionist but I can tell that **buying food is an optimization problem**: a problem that you, aware or not, engage with everytime you choose what to eat. So why not optimize your choice?

"Okay, but how do you do that?" is the question I will try to answer here in an accessible, enjoyable way! You can always use a pen and paper and write down numbers and calculations, but that is boring. What if you can write a program, have fun while doing so, and then just plug-and-chug later? In this post, I will explain one way such program might work. For the sake of the nontechies, I won't include code here, but it is available at the end if you want to take a look 😉.

As with any problem, we have to make some solid, non-redundant definitions. First, we start by defining `Daily Calories` as a number that represents the amount of calories that you need per day. Our bodies are different, so feel free to do some research to find what best suits your lifestyle. The U.S. Office of Disease Prevention and Health Promotion (aka the experts) have put together [guidelines](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/) that may help you determine the "right" number for you.

Next, we break down the daily calories into the main nutrients your body needs. Of course, the complete list is very long. So, we limit ourselves to only a handful: Fat, Carbs, and Protein. We also ignore variations among all the different kinds of these molecules. For example, Saturated fats and unsaturated fats are just counted as "Fats." You get the idea. We are not making up a diet for people. We are just trying to save money and stay alive here.. We will represent each nutrient type by the percent of `Daily Calories` that it represents. This is convenient because this percent is reported on the back of almost all products that you can buy. One catch is that, these percents are calculated for a 2000 Cals diet. So, our program will have to scale them up or down depending on what the user's `Daily Calories` is.

The last definition we have to make is a food product that you can buy. For each product, we represent its `name`, `fatpercent`, `carbpercent`, `proteinpercent`. Since the values listed on a box is usually 'per serving', we have to also account for a product's `number of servings`. Last but certainly not least, we represent a product's `price`.

Here is sample data that I collected from [Starmarket's website](https://shop.starmarket.com/store/star-markets/storefront):


Great. We got all this data. Now the interesting part: what do we do with it? 🤔 As all sentient beings, we want to maximize utility and minimizing expenditure. We know that utility is maximized if we consume exactly the right amount of calories in just the right nutrient proportion, 100%. We lose utility when we consume either more or less than the right amount. Using these two assumptions, we can express utility as a mathematical function of what the user consumes daily:

$$ U(m) = - \sum_{n=1}^{num. nutrients} \mid percent(m, i) - 100 \mid $$

where $ m $ is the daily meal (a bundle of food products), $ n $ is a nutrient among the ones we chose to consider, $ percent $ is a function that takes a meal and a nutrient and outputs the daily percent of a that nutrient that the meal contains. The way we defined $ U $ treats the maximum utility as $ 0 $ , and anything worse as just a negative number. Of course, $ U $ could be defined in other ways, but I let's keep it simple. Here is what U looks like:


{% include figure.html file="/imgs/meal-1.png" description="Figure 1: Utility function of two nutrients" %}