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

Now, we make a few changes. Our functions become real. They become numerical (i.e: they take in some numbers and output one -and only one- number). We also start denoting them using circles.

{% include mailchimp.html source="nn1" %}