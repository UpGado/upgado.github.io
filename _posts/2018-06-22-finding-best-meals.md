---
layout: post
title:  "Finding the Best Deal on Food using Data Science"
date:   2018-06-22 23:00:00
published: true
---

Everybody has their own preferences when it comes to the food they eat. Yet, we (at least broke college students) agree that the food you eat daily shouldn't break the bank. Well.. If you eat nothing, you do a great job saving but not so-great one at staying alive. To stay healthy, you also have to get the nutrients you need in the optimal proportions or at least be close enough (aka you can't rely on just food X as the source of calories). I am no nutritionist but I can tell that **buying food is an optimization problem**: a problem that you, aware or not, engage with everytime you choose what to eat. So why not optimize your choice?

"Okay, but how do you do that?" is the question I will try to answer here in an accessible, enjoyable way! You can always use a pen and paper and write down numbers and calculations, but that is boring. What if you can write a program, have fun while doing so, and then just plug-and-chug later? In this post, I will explain one way such program might work. For the sake of the nontechies, I won't include code here, but it is available at the end if you want to take a look 😉.

As with any problem, we have to make some solid, non-redundant definitions. First, we start by defining `Daily Calories` as a number that represents the amount of calories that you need per day. Our bodies are different, so feel free to do some research to find what best suits your lifestyle. The U.S. Office of Disease Prevention and Health Promotion (aka the experts) have put together [guidelines](https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/) that may help you determine the "right" number for you.

Next, we break down the daily calories into the main nutrients your body needs. Of course, the complete list is very long. So, we limit ourselves to only a handful: Fat, Carbs, and Protein. We also ignore variations among all the different kinds of these molecules. For example, Saturated fats and unsaturated fats are just counted as "Fats." You get the idea. We are not making up a diet for people. We are just trying to save money and stay alive here.. We will represent each nutrient type by the percent of `Daily Calories` that it represents. This is convenient because this percent is reported on the back of almost all products that you can buy. One catch is that, these percents are calculated for a 2000 Cals diet. So, our program will have to scale them up or down depending on what the user's `Daily Calories` is.

The last definition we have to make is a food product that you can buy. For each product, we represent its `name`, `fatpercent`, `carbpercent`, `proteinpercent`. Since the values listed on a box is usually 'per serving', we have to also account for a product's `number of servings`. Last but certainly not least, we represent a product's `price`.

Here is sample data that I collected from [Starmarket's website](https://shop.starmarket.com/store/star-markets/storefront):

| Name                                                | Fat % | Carbs % | Protein % | Number of servings | Price |
|-----------------------------------------------------|-------|---------|-----------|--------------------|-------|
| Hass avocado                                        | 32    | 4       | 5.3       | 1                  | $2    |
| Old El Paso Flour Tortilla Shells                   | 5     | 9       | 5.3       | 5                  | $2.89 |
| Signature Kitchen Diced Tomatoes With Green Chilies | 0     | 2       | 1.78      | 3.5                | $1.19 |
| Black beans (from Stop&Shop)                        | 0     | 7       | 14.3      | 3.5                | $.5   |

Great. We got all this data. Now the interesting part: what do we do with it? 🤔 As all sentient beings, we want to maximize utility and minimize expenditure. We know that utility is maximized if we consume exactly the right amount of calories in just the right nutrient proportion, 100%. We lose utility when we consume either more or less than the right amount. Using these two assumptions, we can express utility as a mathematical function of what the user consumes daily:

$$ U(m) = - \sum_{n=1}^{num. nutrients} \mid percent(m, i) - 100 \mid $$

where $ m $ is the daily meal (a bundle of food products), $ n $ is a nutrient among the ones we chose to consider, $ percent $ is a function that takes a meal and a nutrient and outputs the daily percent of a that nutrient that the meal contains. The way we defined $ U $ treats the maximum utility as $ 0 $ , and anything worse as just a negative number. Of course, $ U $ could be defined in other ways, but I let's keep it simple. Here is what $ U $ looks like:


{% include figure.html file="/imgs/meal-1.png" description="Figure 1: Utility function of two nutrients" %}

Now, we turn our attention to the daily expenditure function, $ E $. The price of a meal is the sum of the individual prices of its components (duh). This could be expressed mathematically as:

$$ E(m) = \sum_{i=1}^{num. components} price(i) * count(i) $$

Now, we can firmly assert our problem as: given a table of product information, we want to find a bundle of products that has as small $ E $ as possible and as maximized $ U $ as possible. It is not exactly an easy job, but the optimal solution could be approximated. I bet you can think of some way to find a decent appeoximation. Maybe just look at each nutrient and pick the product with the highest amount of that nutrient per dollar. You will more likely end up with a meal that is better than a random pick. It might even be the best meal possible, given the standards that we defined so far.

Well. Since we have come so far, why wouldn't we try to do better? In fact, can we do a perfect job? Can we really find that meal and be sure that it is the best meal given our choices? We can! and in fact, the algorithm for that is so easy to code: **Brute Force** (CS students: I see you laughing right now. Everybody else: don't worry I got you 🤠 ). Brute force means that we look at each and every single meal possible (within our budget), calculate its respective $ U $ and $ E $ and then just find that one that gave us the best result.

But let's wait a second just to mention one important limitation of this approach: it scales very badly. If we consider a little scenario: our store  sells only 5 products. Also, we can buy at most 4 units of any product. How many meal choices can we make? Well. Once we walk by a product, we decide to buy either 0, 1, 2, 3, or 4 of it. And we make 5 of such decisions (one for each product). We end up with $ 5^5=3125 $ possible cases! Not too bad. A computer from the 2000s or even an older one can definitely do this. But let's see what happens to the number of choices if we increase the number of products:

{% include figure.html file="/imgs/meal-2.png" description="Figure 2: I wish I could call this a slide, but unfortunately it's more like a steep mountain for us" %}

The number of cases gets higher faster and faster. So, we really can't use brute force for a big number of products unless we want to wait for eternity before picking a meal! For our case though, it is perfectly okay, even badass I think, to use brute force 😈. The program is now all figured out! just need to put it into code, which I did. If you'd like to test it (or better yet improve it), you can find it [here](www.google.com).

Here is what it thinks of a $4 / day meal:

```bash
$ python3 food.py
What is your max daily budget in dollars?
>>4
What is your desired daily calorie intake?
>>2000
31 cases to consider, okay!
Ayt Miss. Here is your $3.89 meal:
    - Old El Paso Flour Tortilla Shells: 1.0 units
    - Black beans: 2.0 units
It gives you 25 % fat 94 % carbs 127 % protein of your daily intake
```

Of course, the idea of eating 20 loaves of tortilla shells is .. not very popular 😃. In fact, the program so far misses several factors that humans normally take into account when choosing their food. These factors include the "satiety index", or just how filly different foods are. It could also use data to understand how much of one food is okay for a human to eat per meal. For example, while beans are generally great, eating too much of them could cause digestive problems. How much? We need more data. Generally speaking, more data $ = $ smarter program. I bet that you, the reader, can think of one more "datum" that can be considered when choosing meals and will this program smarter.

In the end, I am happy that you have read so far 😍. If you enjoyed reading, please share my website among your friends! I plan to continue writing articles in the future. If you have a topic you would like me to cover, I would be happy to hear it 😋.

See you soon!