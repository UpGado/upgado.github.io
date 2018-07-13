---
layout: post
title:  "Teaching a neural net to tweet like Trump"
date:   2018-07-09 14:00:00
published: true
draft: true
---

Here, I show what a neural network is, and how we can use one to make a program that can generate Trump tweets 🤓

## What is a neural net?

You might have heard of them being celebrated in the media lately. They are the reason many computer programs that can now understand images, drive a car around or even synthetize music. While they do have the word "neuron" in them, they are only vaguely inspired by the human brain. So don't be scared, you don't need to know biology in order to understand how they work.


Neural nets are a bit like *magic*. Let's consider the following example: you have an image of a handwritten digit. You hypothesize that a magic mathematical function $ M() $ can take this image and then tell you what digit it thinks it is.

{% include figure.html file="/imgs/nn-1.png" description="Figure 1: A magic digit-classifier function" %}

Next, we split this function into more and more functions. It is still magic, but a composite of many magic functions instead of just one.


{% include figure.html file="/imgs/nn-2.png" description="Figure 2: A composite, magic digit-classifier function" %}

Now, we make a an important change: Our functions become real. They become numeric (i.e: they take in some numbers and output one -and only one- number). We also start denoting them using circles.

{% include figure.html file="/imgs/nn-3.png" description="Figure 3: A composite, REAL digit-classifier function" %}

At this point, we start referring to our whole structure as a **neural net**. Each small function is now called a neuron, referring to a super-duper abstraction of what a biological neuron does. But it's okay. It's just a name 😌.

The important question: how do we get this neural network (bunch of functions working together) to classify digits? **We teach it** 🤯. To do so, we need many, many examples (aka a **dataset**) of handwritten digit images. Then, we "show" the neural network those images and "tell" it to create and develop its understanding of what digits look like. "Telling the neural net" is part of the magic I referred to earlier. But interestingly, as hard as it may sound, it is actually possible using simple Calculus rules. I won't get to the details; most people use readymade functions to train their neural networks. It's the power (and necessity) of abstraction 😜.

Now that we have an idea of what a neural network is, let's apply it to a cool example: a neural net that can learn how President Trump tweets!

## Tweets like Trump

We use a flavor of neural nets called a Recurrent Neural Network (RNN). The main feature of RNNs is that they are stateful (aka, they have a memory). You can imagine that, if you engage in some kind of speech, you need memory. Otherwise, speech wouldn't make sense.

(If you wish to further understand what RNNs are, here is a simple but long [post](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) about RNNs by Andrej Karpathy, the director of AI at Tesla.)

Like we do for a digit-classifier, we need data to train the neural network. Donald Trump's tweets are widely [available](https://data.world/datacrunch/every-donald-trump-tweet) on the internet (apparently, many people are studying his tweets 🤠). Once we obtain the tweets, we use them to train the neural network. For the sake of simplicity, I won't include code here, but it is available if you contact me.

Here is some sample results:
```
@magilennares I his puther stalted he cant waiting for the pathetic last night. In what when we will mees a more saying opponice today! #ImWithYou #MAGA
#MakeAmericaGreatAgain https://t.co/T51raFaabJTha
```
```
Mexico the show! #AmericaFirst #Trump2016 https://t.co/sTaCTRnIMA""@Trump2016Menines: @realDonaldTrump I am going to the real one in all of insiches on at things, hearts for honestide for you!
```

In my opinion, this is both fast and pretty cool 😃. We notice a couple of interesting results. The neural net learns to produce syntactically correct URLs, even though they point to nowhere. They also learn to use hashtags almost perfectly. One reason for this might be that hashtags show up more consistently than other words. This reflects one main drawback of neural nets: any biases in the training data will show up in the neural network behaviour. In our case, it is a small, non-consequential issue. But in other cases, neural nets can acquire all the detrimental biases of humanity, including racism, sexism and other bad stuff. ☹️

All in all, neural networks are a big deal. They come with their caveats, as we have seen. But, when used wisely, they can achieve awesome feats. So stay hopeful and excited, friends 😉.

Peace out.

{% include figure.html file="/imgs/nn-4.png" description="Figure 4: A picture with Andrej Karpathy, the director of AI at Tesla (he is probably friends with Elon Musk). I just thought that the picture is relevant. 🌝" %}


{% include mailchimp.html source="nn1" %}