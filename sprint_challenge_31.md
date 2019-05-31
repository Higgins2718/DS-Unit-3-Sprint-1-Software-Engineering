# Data Science Unit 3 Sprint Challenge 1

## Software Engineering - the Acme Way

In this sprint challenge you will write code and answer questions related to
object-oriented programming, code style/reviews, containers, and testing. You
may use any tools and references you wish, but your final code should reflect
*your* work and be saved in `.py` files (*not* notebooks), and (along with this
file including your written answers) added to your
`DS-Unit-3-Sprint-1-Software-Engineering` repository.

For all your code, you may only import/use the following:
- Other modules you write
- `unittest` (from the standard library)
- `random` (from the standard library)

As always, make sure to manage your time - get a section/question to "good
enough" and then move on to make sure you do everything. You can always revisit
and polish at the end if time allows.

This file is Markdown, so it may be helpful to add/commit/push it first so you
can view it all nice and rendered on GitHub.

Good luck!

### Part 1 - Keeping it Classy

As an employee of Acme Corporation, you're always looking for ways to better
organize the vast quantities and variety of goods your company manages and
sells. Everything Acme sells is considered a `Product`, and must have the
following fields (variables that live "inside" the class):

- `name` (string with no default)
- `price` (integer with default value 10)
- `weight` (integer with default value 20)
- `flammability` (float with default value 0.5)
- `identifier` (integer, automatically genererated as a random (uniform) number
  anywhere from 1000000 to 9999999, includisve)(inclusive).

Write a Python `class` to model the above data. Make sure you are *precise* in
your field names and types, and that your class has an `__init__` constructor
method with appropriate defaults (or lack thereof).

*Hint* - `random.randint` should be able to serve your random number needs.

Save the class in `acme.py`, and you can test your code in a Python repl as
follows:

```python
>>> from acme import Product
>>> prod = Product('A Cool Toy')
>>> prod.name
'A Cool Toy'
>>> prod.price
10
>>> prod.weight
20
>>> prod.flammability
0.5
>>> prod.identifier
2812086  # your value will vary
```

### Part 2 - Objects that Go!

The class you wrote in part 1 is nice, but it doesn't *do* anything - that is,
it doesn't have any *methods*. So let's add some! Specifically, add two methods:

- `stealability(self)` - calculates the price divided by the weight, and then
  returns a message: if the ratio is less than 0.5 return "Not so stealable...",
  if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
  and otherwise return "Very stealable!"
- `explode(self)` - calculates the flammability times the weight, and then
  returns a message: if the product is less than 10 return "...fizzle.", if it is
  greater or equal to 10 but less than 50 return "...boom!", and otherwise
  return "...BABOOM!!"

Save your code, and you can test as follows:

```python
>>> from acme import Product
>>> prod = Product('A Cool Toy')
>>> prod.stealability()
'Kinda stealable.'
>>> prod.explode()
'...boom!'
```

### Part 3 - A Proper Inheritance

Of course, Acme doesn't just sell generic products - it sells all sorts of
special specific things!

Make a subclass of `Product` named `BoxingGlove` that does the following:

- Change the default `weight` to 10 (but leave other defaults unchanged)
- Override the `explode` method to always return "...it's a glove."
- Add a `punch` method that returns "That tickles." if the weight is below 5,
  "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
  "OUCH!" otherwise
  
Example test run:

```python
>>> from acme import BoxingGlove
>>> glove = BoxingGlove('Punchy the Third')
>>> glove.price
10
>>> glove.weight
10
>>> glove.punch()
'Hey that hurt!'
>>> glove.explode()
"...it's a glove."
```

### Part 4 - Class Report

Now you can represent your inventory - let's use these classes and write an
`acme_report.py` module to generate random products and print a summary of them.
For the purposes of these functions we will only use the `Product` class.

Your module should include two functions:

- `generate_products()` should generate a given number of products (default
  30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary

For the purposes of generation, "random" means uniform - all possible values
should vary uniformly across the following possibilities:

- `name` should be a random adjective from `['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']` followed by a space and then a random noun from
  `['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']`, e.g. `'Awesome Anvil'`
  and `Portable Catapult'` are both possible
- `price` and `weight` should both be from 5 to 100 (inclusive and independent,
  and remember - they're integers!)
- `flammability` should be from 0.0 to 2.5 (floats)

You should implement only depending on `random` from the standard library, your
`Product` class from `acme.py`, and built-in Python functionality.

For the report, you should calculate and print the following values:

- Number of unique product names in the product list
- Average (mean) price, weight, and flammability of listed products

At the bottom of `acme_report.py` you should put the following code:

Following is useful starting code for `acme_repory.py`:

```python
#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
```

The last lines let you test by running `python acme_report.py`. You should see
output like:

```
$ python acme_report.py 
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: 19
Average price: 56.8
Average weight: 54.166666666666664
Average flammability: 1.258097155966675
```

It's OK for the specifics to vary (how you message/format), but it should output
and clearly identify all four relevant numbers.

### Part 5 - Measure twice, Test once

Make a file `acme_test.py` starting from the following code:

```python
#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


if __name__ == '__main__':
    unittest.main()
```

If you run the tests you should see output like:
```
$ python acme_test.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Complete the following:

- Add at least *2* more test methods to `AcmeProductTests` for the base
  `Product` class: at least 1 that tests default values (as shown), and one that
  builds an object with different values and ensures their `stealability()` and
  `explode()` methods function as they should
- Write a new test class `AcmeReportTests` with at least 2 test methods:
  `test_default_num_products` which checks that it really does receive a list of
  length 30, and `test_legal_names` which checks that the generated names for a
  default batch of products are all valid possible names to generate (adjective,
  space, noun, from the lists of possible words)
  
*Hint* - `test_legal_names` is the trickiest of these, but may not be as bad as
you think. Check out `assertIn` from `unittest`, and remember that Python is
pretty handy at string processing. But if you get stuck, move on and revisit.

Note that `inventory_report()` is pretty tricky to test, because it doesn't
*return* anything - it just prints (a "side-effect"). For the purposes of this
challenge, don't worry about testing it - but as a stretch goal/something to
think about, it's a good ponderer.

### Part 6 - Style it Up

If you did the earlier parts in an editor that was linting your code (warning
you about violations of [PEP8 style](https://pep8.org/)) and you listened to it,
you're already done!

If not, go back and fix things! If you don't have a built-in tool for checking,
you can use [PEP8 online](http://pep8online.com/).

Go for lint-free! If there's a stubborn warning or two you can't fix though,
it's okay to leave a comment explaining it and move on.

### Part 7 - Questions (and your Answers)

Acme Corporation isn't just a few `.py` files. If you want to grow in your
career here, you'll have to answer the following:

- What, in your opinion, is an important part of code reviews? That is, what is
  something you pay attention to when you review code, and that you appreciate
  when others do the same for your code?
 
  One key element of a good code review is specificity. Not being specific with criticism comes with a risk of misinterpretation. For example, imagine this vague bit of criticism, "Commas used incorrectly" for this code block:
 ```
 list = ['alpha', 'beta', 'gamma']
 for item, in list:
    print(list, item)
 ```
 It would be easy for an inexperienced programmer to misinterpret this and think any one of the following:
 1. The comma following `item` doesn't belong
 2. The comma following `list` doesn't belong
 3. The commas in my list are used incorrectly
 4. The comma following `item` doesn't belong and the commas in my list are used incorrectly
 5. The comma following `list` doesn't belong and the commas in my list are used incorrectly
 6. The commas following `item` **and** `list` don't belong
 7. The commas following `item` **and** `list` don't belong *and* the commas in my list are used incorrectly
 
 The proper critique would have been more along the lines of "There is a comma following `item`, the second character in line `271`. A comma is unnecessary in this case, as you are only looping through one kind of object (it's a list, not a dictionary),  and must be removed."
 
Good criticism should specify the line area (or general location of the mistake), some reasoning behind the criticism, and it should be actionable.  

My improved example critique might be a bit much in this particular case, but in general I think it holds true.
  
- We have an awful lot of computers here, and it gets pretty confusing with
  slightly different things running on all of them. How could containers help us
  improve this situation?
  
  Before I learned about containers, my programming environment had trouble with certain libraries or packages because one or more dependences might be installed in my environment and at a lower or higher version than was  accepted by the library or package. The quick fix would be to uninstall and specify the desired version in the new pip installation or to simply update the package. However, it is often more complicated than this. 
  
  Frequently, you'll find yourself working with one library or package that has a certain dependency of a lower version number and another library or package that has that same dependency, but of a higher version number. If this is production code, you just can't have the two libraries/packages in the same environment. 
  
  Since it is complicated to have two or more python versions on the same OS, containers are the ideal solution in this scenario. They require less storage space than virtual machines, but can run their own environment—separate and isolated from the others on your machine—and the libraries and packages in this container are kept within the container, separate from all the others on your machine.
  
  The main benefit is that there are no more problems when your work in the morning requires, say, Pandas 1 and your work in the afternoon requires Pandas >= 2. Simply "containerize" your projects, and you'll have a far easier time keeping projects from squabbling with each other.
  
  A secondary benefit is that containerrs can run on Linux, Windows, Mac, and more. However, since I am not working for a company that has employees working on multiple operating systems, this benefit is not directly applicable to my work.
  

Answer both of these questions (baseline ~5 sentences) here in text.

### Part 8 - Turn it in!

Add all the files you wrote (`acme.py`, `acme_report.py`, and `acme_test.py`),
as well as *this* file with your answers to part 7, to your weekly repo
(`DS-Unit-3-Sprint-1-Software-Engineering`). Commit, push, and await feedback
from Acme Corporation management. Thanks for your hard work!

*Bonus!* Got this far? Read up on the [history of the fine Acme
Corporation](https://en.wikipedia.org/wiki/Acme_Corporation), with decades of
quality products and many satisfied customers (mostly coyotes).
