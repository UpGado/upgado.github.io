---
layout: post
title:  "The Tale of ASCII Racer"
date:   2019-08-31 07:44:35
published: true
draft: false
---

Run!

This summer, bored at work, and refusing to study properly for the GRE, I decided to embark on a new coding adventure. I wanted to make a racing game that runs in the terminal. For those who don't know, this is what a terminal looks like:

{% include figure.html file="/imgs/ascii-1.png" description="Figure 1: Terminals don't come with video games" width="80%"%}

You can't even show an image in terminal, and you can't draw anything. You can only show fixed-size characters, and if you're lucky, you can show text in at most 256 colors. However, even with those limitation, people who are into it can still make some beautiful [ASCII art](https://www.asciiart.eu)

And so, I decided to go for it. The game was to be called "ASCII Racer". Its design was inspired by this Atari racing game that I remember vaguely from my childhood:

{% include figure.html file="/imgs/ascii-3.jpg" description="Figure 2: A very high-tech, futuristic game compared to what I was ever going to make happen in Terminal" width="60%"%}

Except that ASCII Racer was a lot, a lot simpler. It was still a lot of interesting, fun work, and it evolved into something that I didn't quite expect. It turned into a game where you drive in your sports car and collect various alcoholic drinks and Martini glasses:

{% include figure.html file="/imgs/ascii-4.gif" description="Figure 3: ASCII Racer gameplay" width="90%"%}

I wrote the whole thing in Python, with no external dependencies. Everything about the game was made from scratch, and I was very proud. My expectations for the game was just that it's going to be something cool that I could maybe show to my coworkers and have a few laughs about.

But then, one night, my friend and coworker Chris suggested that I put the game up on the [r/python](https://reddit.com/r/python/), the subreddit for Python with 410K members. I thought about it, and I thought to myself: what is the worst that could happen? People on reddit tend to be negative. If I post the game, they are probably going to think that it sucks. But that's fine. I can take that. I posted it and went to bed that night.

The next morning, I thought I would check on the post. To my utter surprise, my [post](https://www.reddit.com/r/Python/comments/cpmll6/made_a_racing_game_that_runs_in_terminal_100/) has reached 1.5K upvotes (reddit talk for likes). People liked the game and a lot of the comments were very supportive. Not quite what I expected, but it's a happy surprise.

Soon enough, people found the source code on GitHub. Soon enough, they were reporting bugs and suggesting improvements. In fact, some person even made and submitted an improvement to the game! I suddenly found myself not anymore a programmer who is carelessly working on a fun side project. I am a *maintainer* of an open source project that people are interested in. There was a sense of responsibility towards the people who liked the game and actually worked on improving it. I can't fuck up anymore or introduce a bug to the game.

I quickly accepted the challenge and read up on best practices for maintaining an open source project. One issue that intrigued me was how to respond to people's code suggestions (which come in the form of Github pull requests). There was one person who wrote a new feature that the game needed. Clearly, this person spent time writing code to improve my game, I should thank them and show gratitude. However, I also had my thoughts about what the code should look like, and this person's code did not look exactly follow them. I didn't want to come across as an asshole, but I did request changes to their code before I included it into the game. I thought that it's okay to sacrifice some code quality in favor of making the contributors feel that their code and effort is being appreciated. I don't want them to come back to look at the project and find that their code has been completely rewritten.

At the time of writing this post, ASCII Racer has 78 stars on [Github](https://github.com/UpGado/ascii_racer), one of which is mine (sssshh). It truly was an awesome learning experience, and I am thankful to everyone who made it happen. While I don't intend on working on it more, I'll happily maintain the project and I welcome contributions.

Shoutout to Chris Reik for contributing to the game by implementing Budlight cans and dollar bills!


If you want to install ASCII Racer, run:

```bash
$ pip3 install asciiracer
```

If you want to contribute, check out the Github [repository](https://github.com/UpGado/ascii_racer).

Cya

{% include mailchimp.html source="ascii1" %}
