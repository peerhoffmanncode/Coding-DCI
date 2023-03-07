# Lambda functions II

## Description

In this exercise, we will get used to creating and using lambda functions on decorators and other high-order functions.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1

Sort the following list of tuples using Lambda. The `sort()` method of list objects has a parameter named `key` that takes a function returning the value to use as a reference for the sorting.

Your task is to pass a lambda function as argument to the `key` parameter of the `sort()` method of `subject_marks` so that the tuples are sorted according to the marks.

```
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=**your_lambda_function**)
print(subject_marks)
```

- Your result should look like this:

```
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```

###

### Task 2

Use the built-in `filter()` function to filter a list of integers to get only those that are even using a lambda function.

The `filter()` function takes two arguments: a function and an iterable. The function should return a Boolean indicating if a particular value matches our query.

Use the following iterable on your call to `filter()`:

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- Your result should look like this:

```
[2, 4, 6, 8, 10]
```

###

### Task 3

Create a decorator named `protected` that will only allow a valid user to execute the function it decorates.

The decorator must return a lambda function that will ask the credentials (username and password) to the user (use `input()`) and validate them against hard coded values (for instance, `admin`|`admin`).

If the entered values match those in the code, the decorated function will be executed normally. Otherwise, it should return the message `You are not authorized`.

Use the following test cases:

```
def public():
    print("Hello World!")

@protected
def private():
    print("Welcome, admin!")

public()
private()
```

- Your result should look like this:

```
Hello World!
Username: admin
Password: admin
Welcome, admin!
```

And:

```
Hello World!
Username: Anonymous
Password: 1234
You are not authorized
```

###

### Task 4

Rewrite the decorator `wrap_with` from the last exercise about decorators and use a lambda function to replace the `inner()` function.

Use the following test case:

```
print(get_custom_html_greeting("James", "Brown"))
```

- Your result should look like this:

```
<p><em>Hello, <strong>James Brown</strong>!</em></p>
```
