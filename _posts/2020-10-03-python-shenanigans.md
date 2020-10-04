---
layout: post
title:  "What is a function in Python and can we mess with it?"
date:   2020-10-03 10:44:00
published: true
draft: false
---

I was talking with a friend who is new to programming. He asked me a simple, innocent question. The kind of question that a father would hear from his daughter or son and make him feel a certain kind of happy feeling.

Thq question is: why if I `print` a function in Python, it shows me where it lives in memory, instead of its contents?

This is a beautiful question that I am going to answer in a long way. Along our way, we are going to cover some of the most misunderstood things about Python. We are also going to do some bad things that are for the general good.

A function in Python is simply a variable that you can call. Well, what is a variable? It's actually not exactly obvious what a Python variable is. For instance, take a look at this code and what it outputs:

```python
>>> x = ['chad']
>>> y =  x
>>> x.append('virgin')
>>> y
['chad', 'virgin']
```

however:

```python
>>> x = 'chad'
>>> y =  x
>>> x = 'virgin'
>>> y
'chad'
```

Hmm, why the difference? Why did changing `x` change `y` in the first case but not in the second case?

The answer lies in the idea of `value mutability`, which is tied to what a variable is. In Python a variable is a *pointer* to a value that lives somewhere in memory. Updating a variable in Python could mean two things: either the value that the variable points to is updated, OR a new value is created somewhere in memory and the variable is updated to point at the new value. So what decides which way it is going to be? The answer is in the mutability of that value. Immutable values are values that once created in memory, that cannot be changed

Immutable values includes things like integers, booleans, strings, and tuples. That is right. Integer values cannot be changed in Python. That means that in a simple for loop like the following:
```python
for i in range(3):
   print(i)
```

A new value containing the numbers 0, 1, or 2 is created during each loop interation and then the variable `i` is updated to point at the new value. If you don't believe it, you can get and print the memory address of the value of `i` using the `id` function:

```python
>>> for i in range(3):
...    address = id(i)
...    print(f"{address} -> {i}")
4522253008 -> 0
4522253040 -> 1
4522253072 -> 2
```

So, a variable in Python is a pointer to a value. Functions are no exception. The value of a function is an object that contains information about the function's arguments and the instructions that are followed to execute it. Can we mess with that object? Of course.

We define a function called `add_one`:

```python
>>> def add_one(x):
...    return x + 1
```

Currently, when we print this function, we get:

```python
>>> print(add_one)
<function add_one at 0x10db26af0>
```

That is not too helpful. Can we mess with the function to make it print its instructions? Let's try.

The first step in messing with any object in Python is checking its `dir`, which returns the names of *all* of its attributes that are in existence. This usually reveals a lot of useful information about any object, regardless of whether or not you should be able to edit those information.

Let's `dir` it:

```python
>>> for attribute_name in dir(add_one):
...     attribute_value = getattr(add_one, attribute_name)
...     print(f"{attribute_name}: {attribute_value}")
```

Usually by trial and erroe, you can quickly investigate how those attributes affect the behaviour that you are trying to change. In this case, I found that by changing `__qualname__`, I can get the function to print any string I want, instead of its name:

```python
>>> add_one.__qualname__ = 'HEY I WAS MESSED WITH':
>>> print(add_one)
<function HEY I WAS MESSED WITH at 0x10db26af0>
```

Interesting. The last step is to change the printed into something useful, the source code of that function. Python makes it possible to get the source code of any function using the `getsource` function in the `inspect` module:

```python
>>> import inspect
>>> print(inspect.getsource(add_one)):
def add_one(x):
    return x + 1
```

So finally, if we set `add_one.__qualname__` to `inspect.getsource(add_one)` we get the desired effect:

```python
>>> add_one.__qualname__ = inspect.getsource(add_one)
>>> print(add_one)
<function def add_one(x):
    return x + 1
 at 0x1025d94c0>
```

Neat.

{% include mailchimp.html source="shenanigans1" %}
