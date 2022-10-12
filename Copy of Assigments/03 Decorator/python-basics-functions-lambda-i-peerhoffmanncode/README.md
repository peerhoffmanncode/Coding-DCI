# Lambda functions

## Description

In this exercise, we will get used to creating and using lambda functions.

##

## Tasks

###

### Task 1

Create a lambda function that adds 15 to a given number passed in as an argument. Assign the lambda function to a variable name called `add15`.

Use these test cases:

```
print(add15(1))
print(add15(-2))
```

- Your result should look like this:

```
16
13
```

###

### Task 2

Define the functions `isOdd`, `isEven` and `getParity` from previous exercises, but now as lambda functions assigned to variables.

Use these test cases:

```
print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))
```

- Your result should look like this:

```
False True
True False
False True
True False
```

###

### Task 3

Define a lambda function assigned to a variable named `starts_with_p` that takes a single argument as a string. Returns True if this string starts with P (case insensitive) and False if it does not.

```
print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))
```

- Your result should look like this:

```
True
False
True
```

###

### Task 4

For a given list of numbers, use a lambda function to return the result of multiplying each number by a given number stored in a variable named `factor` in the global scope.

Use these test cases:

```
numbers = [2, 4, 5, 7, 9, 14]
factor = 2
```

- Your result should look like this:

```
[4, 8, 10, 14, 18, 28]
```
