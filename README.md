# Data_Privacy
## for random library
### The key difference between the Python functions random.sample() and random.choices() is how they handle element selection with regards to replacement:

* random.sample(population, k) selects k unique elements from the population without replacement, meaning once an element is picked, it cannot be picked again. It will produce a list of distinct items, and therefore, k cannot be greater than the size of the population, or it raises an error.

* random.choices(population, k) selects k elements with replacement, meaning the same element can be picked multiple times. This allows duplicates in the output and k can be greater than the population size.

* We’re using itertools.product() to generate all possible combinations of digits for a given length.
