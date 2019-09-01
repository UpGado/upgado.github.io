---
layout: post
title:  "A Tale of ASCII Racer"
date:   2019-08-31 07:44:35
published: true
draft: true
---

Run!

This summer, bored at work, and refusing to study properly for the GRE, I decided to embark on a new coding adventure. I wanted to make a racing game that runs in the terminal. For those who don't know, this is what a terminal looks like:

{% include figure.html file="/imgs/ascii-1.png" description="Figure 1: Terminals don't come with video games" width="90%"%}

You can't even show an image in terminal, and you can't draw anything. You can only show fixed-size characters, and if you're lucky, you can show text in at most 256 colors. However, even with those limitation, people who are into it can still make some beautiful [ASCII art](https://www.asciiart.eu)

And so I decided to go for it. The game was to be called "ASCII Racer". Its design was inspired by this Atari racing game that I remember vaguely from my childhood:

{% include figure.html file="/imgs/ascii-3.jpg" description="Figure 2: A very high-tech, futuristic game compared to what I was ever gonna make happen in Terminal" width="60%"%}

Except that ASCII Racer was a lot, a lot simpler. It was still a lot of interesting, fun work, and it evolved into something that I didn't quite expect. It turned into a game where you drive in a your sports car and collect various alcoholic drinks and Martini glasses:

{% include figure.html file="/imgs/ascii-4.gif" description="Figure 3: ASCII Racer gameplay" width="100%"%}

I wrote the whole thing in Python, with no external dependencies. Everything about the game was made from scratch, and I was very proud. My expectations for the game was just that it's gonna be something cool that I could maybe show to my coworkers.

But then, one night, my friend and coworker Chris suggested that I put the game up on the [r/python](https://reddit.com/r/python/), the subreddit for Python with 410K members. I thought about it, and I thought what is the worst that could happen? People on reddit tend to be negative. If I post the game, some people are probably going to think that it sucks. But that's fine. I can take that. I posted it and went to bed that night.

The next morning, I thought I would check on the post. To my utter surprise, my [post](https://www.reddit.com/r/Python/comments/cpmll6/made_a_racing_game_that_runs_in_terminal_100/) has reached 1.5K upvotes (reddit talk for likes). People liked the game and a lot of the comments were very supportive. Not quite what I expected, but it's a happy surprise.

Soon enough, people who found the source code on GitHub. Soon enough, they were reporting bugs and suggesting improvements. In fact, some person even made and submitted an improvement to the game! I suddently found myself not anymore a rookie programmer carelessly working on a fun project. I am a *maintainer* of an open source project that people are interested in. There was a sense of responsibility towards the people who liked the game and actually worked on improving it. I can't fuck up anymore or introduce a bug to the game.

I quickly accepted the challenge and read up on best practices for maintaining an open source project. One issue that intrigued me was how to respond to people's code suggestions (pull requests). There was one person who wrote a new feature that the game needed. Clearly, this person spent time writing code to improve my game, I should thank them and show gratitude. However, I also had my thoughts about what the code should look like on a high-level, and I thought that this person's changes did not adhere to my *undocumented* code architecture. I didn't want to come across as an asshole, but I did request changes to their code before I include it into the game. I did my best to try and hit a balance, and I thought that it's okay to sacrifice some code quality in favor of making the contributors feel that their code is being appreciated. I don't want them to come back to look at the project and find that their code has been completely rewritten. I think I did well there.

Currently, ASCII Racer has 77 stars on [Github](https://github.com/UpGado/ascii_racer), one of which is mine (sssshh). It truely was an awesome learning experience, and I am thankful to everyone who made it happen.

Shoutout to Chris Reik for implementing Budlight cans and dollar bills!


If you want to play ASCII Racer, run:

```bash
$ pip3 install asciiracer
```

{% include mailchimp.html source="ascii1" %}
