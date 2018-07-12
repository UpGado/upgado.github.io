---
layout: post
title:  "Teaching a neural net to tweet like Trump"
date:   2018-07-09 14:00:00
published: true
draft: true
---

> as of now, posts will be shorter. Enjoy. 😋

Neural nets. You might have heard of them being celebrated in the media lately. They are the reason many computer programs that can now understand images, drive a car around or even synthetize music. While they do have the word "neuron" in them, they are only vaguely inspired by the human brain. So don't be scared, you don't need to know biology in order to understand how they work. Here, we explain how neural nets work and apply them to a cool example.


Neural nets are a bit like *magic*. Let's consider the following example: you have an image of a handwritten digit. You can hypothesize a magic mathematical function that can take this image and then tell you what digit it thinks it is.

{% include figure.html file="/imgs/nn-1.png" description="Figure 1: A magic digit-classifier function" %}

Next, we split this function into more and more functions. It is still magic, but a composite of many magic functions instead of just one.


{% include figure.html file="/imgs/nn-2.png" description="Figure 2: A composite, magic digit-classifier function" %}

Now, we make a an important change: Our functions become real. They become numeric (i.e: they take in some numbers and output one -and only one- number). We also start denoting them using circles.

{% include figure.html file="/imgs/nn-3.png" description="Figure 3: A composite, REAL digit-classifier function" %}

At this point, we start referring to our whole structure as a **neural net**. Each small function is now called a neuron, referring to a super-duper abstraction of what a biological neuron does. But it's okay. It's just a name. 😌

Now the important question: how do we get this neural network to classify digits? We teach it. We show it what a 1 looks like, what a 2 looks like and so on. This is referred to as the *training step* and it is not necessarily an easy problem. Many people devout their lives to studying different "training algorithms" for neural nets. Luckily for us, we don't need to. We'll just use their stuff 😃.

## Tweet like Trump

{% include mailchimp.html source="nn1" %}