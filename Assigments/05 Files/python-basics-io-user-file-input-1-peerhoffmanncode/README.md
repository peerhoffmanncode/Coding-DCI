# User Input and Output

## Description

In this exercise, we will focus on performing user input and output operations.

##

## Tasks

###

### Task 1

Write a Python code that asks the command line user for his/her name. Then print the following list of words as sentences in a single line, but replacing the second word with the user input name:

```
message = ["Hello", "visitor!", "Welcome", "to", "our", "command", "line",
           "interface.", "Please,", "contact", "us", "if", "you", "have",
           "any", "questions."]
```

> You are not allowed to use the `join` method of the `str` objects.
>
> You are not allowed to use any of the `print` keyword arguments.
>
> You are not allowed to do any iterations.

- Your result should look like this (with your user name):

```
What is your name? Janis
Hello Janis! Welcome to our command line interface. Please, contact us if you have any questions.

```

###

### Task 2

Now take the same `message` list from the previous task and, in a new script, write a Python code that will do the same except:

- when the word ends with point `.`, in which case it will add a new line after the point.
- when the word ends with en exclamation mark `!`, in which case it will add two new lines.

> You are not allowed to use the `join` method of the `str` objects.
>
> You may use iterations in this task.

- Your result should look like this (with your user name):

```
What is your name? Janis
Hello Janis!

Welcome to our command line interface.
Please, contact us if you have any questions.

```

###

### Task 3

Now, define a function named `log` that will output the same as the previous task but this time into a log file. This function must use the `print` built-in function to write the text.

Like `print`, it will have as many positional arguments as required, which will be the content to print. It will have the same keyword arguments, but our `log` function will be using the file `messages.log` as default. So, if we don't specify the `file` argument in the call to the `log` function, the content will be printed in the previous file. Either way, the `log` function  will always print to a file.

> Remember to use the proper opening `mode` for appending data to a file.

- Once executed, you should have a file `messages.log` in your directory with the same content as before:

```
Hello Janis!

Welcome to our command line interface.
Please, contact us if you have any questions.

```
- If you execute the script a second time, your file should look like this:

```
Hello Janis!

Welcome to our command line interface.
Please, contact us if you have any questions.
Hello Janis!

Welcome to our command line interface.
Please, contact us if you have any questions.

```

###

### Task 4

Now we will take the exercise from the first unit in this submodule and will review the 3rd task.

In this task, we had a file [src/data/task4.txt](src/data/task4.txt) with the content mixed up:

```
_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
late and would start as near the correct time as possible. The
Vienna early next morning; should have arrived at 6:46, but train was an
impression I had was that we were leaving the West and entering the
hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
East; the most western of splendid bridges over the Danube, which is
got of it from the train and the little I could walk through the
here of noble width and depth, took us among the traditions of Turkish
streets. I feared to go very far from the station, as we had arrived
rule.
```

The aim of the task was to write a Python code to print first the odd lines and then the even lines, so that the text can be read easily. We came up with the following code (or something similar):

```
def print_line(line):
    """Print a line without the extra line break."""
    print(line.rstrip("\n"))


with open("../data/task4.txt") as file:
    even = []
    for num, line in enumerate(file):
        if num % 2:
            even.append(line)
        else:
            print_line(line)
    for line in even:
        print_line(line)
```

Now you will take this code, you will remove the `rstrip` (and the whole `print_line` function) and will be using only the `print` built-in function with the appropriate keyword arguments to output the exact same result.

- Your result should look like this:

```
_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
Vienna early next morning; should have arrived at 6:46, but train was an
hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
got of it from the train and the little I could walk through the
streets. I feared to go very far from the station, as we had arrived
late and would start as near the correct time as possible. The
impression I had was that we were leaving the West and entering the
East; the most western of splendid bridges over the Danube, which is
here of noble width and depth, took us among the traditions of Turkish
rule.
```

###

### Task 5

Write a script to do a countdown from 5 and use the `\r` character to overwrite the number at each second.

> Writing the `\r` character places the cursor at the beginning of the line, the same way that writing `\n` creates a new line. But if we use `\r` without adding `\n`, anything we write after it will overwrite what was previously there.
>
> Hint: use the `sleep` function from the `time` module to make the counter update every second.

- Your script should show the countdown at each second and show only one number at any given time.

```
$ python3 script.py
5...
```
```
$ python3 script.py
4...
```
```
$ python3 script.py
3...
```
```
$ python3 script.py
2...
```
```
$ python3 script.py
1...
```
```
$ python3 script.py
Go!
$
```

###

### Task 6

Now use a similar technique to mock an animated progress bar like this one:

```
[############                  ] 43%
```

> Hints:
>
> - Define a function that takes a percentage and a width to draw a static view of the bar.
> - You can use `str * int` to obtain the amount of hashes and empty spaces you should print according to the percentage passed.
> - Instead of concatenating strings, build an array with the different parts of the progress bar and then unpack them to pass them to the `print` function.
> - Once you have that, write an iteration from 0 to 100 (included) to call your previous function and remember to print the `\r` to overwrite each bar and produce the animation effect.
> - Use the `sleep` function from the `time` module to make the progress bar update every 10 milliseconds.

- Your result should look like this:

```
$ python3 script.py
[                              ] 0%
```
```
$ python3 script.py
[#######                       ] 24%
```
```
$ python3 script.py
[############                  ] 43%
```

```
$ python3 script.py
[#########################     ] 86%
```

```
$ python3 script.py
[##############################] 100%
$
```
