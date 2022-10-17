# Input and Output

## Description

In this exercise, we will put together all the features introduced in this submodule: File I/O, File System Manipulation and User I/O.

##

## Task

We have a pool of files in text format and we want you to build a command line tool that **lets a user search all files** for a specific word in their content **and logs its usage**.

In the directory [src/data](src/data) you will find the resources this script will be using:

- A directory named `articles`. This is where the text files will be located. It currently has 4 samples so that you can test your code. It also has a subdirectory called `removed`. To remove an article from the search feature, instead of deleting the article we will move it there. Your script should only search in the files directly in `articles`.
- A directory named `log`. This directory is now empty. It will contain a directory for each user of the system. Inside the user directory you will create a new file for each search executed by that user. Inside the file, there will be the term searched and the results obtained.

The initial directory tree should look like this:

```
+ src
  + data
    + articles
      - Web development course.txt
      - Orientation course.txt
      - Aws re start program.txt
      - Digital marketing e commerce.txt
    + log (empty directory)
```

The flow of the process must be the following:

1. The user starts the tool by running the script `python3 script.py`.
1. The script asks the user for a name. If the name is empty, it should stop execution with a proper message. If it is not empty, it should greet the user.
1. The script asks for a term of search. If the term is empty, it should stop execution with a proper message. If it is not empty, it will perform the search.
1. The script will search the term indicated by the user in the content of all of the files present in the `articles` directory.
1. Once completed, it will show on the terminal a list of matching resources.
  1. The first line should indicate how many matches were found.
  1. The next lines will start with a tab (`\t`) and will be followed by the name of each file matching. *It will not show the extension of the file*.
1. After printing the result, the script will log the query in the `log` directory. It will go through these steps:
  1. If there is no directory in `log` with the name of the user, it will create it.
  1. It will add a new file in that directory. The name of the file will be random (use `uuid.uuid4()` to generate file names) and the content will include:
    1. A first line with a label `Search term: ` and the user input.
    1. A second line with the label `Matches: ` and the name of the matching files found, in a single line, separated by commas and with a final dot `.`, and without the extension.
1. When everything else is done, the script will ask the user if s/he wants to search another word. If the answer is `yes` (or `y`), then the script will go back to point 3, and repeat the process.

**Example of command line usage**
```
What is your name? Patty
Welcome Patty!
What word would you like to search for? web
** Found 4 matching articles: **
        Web development course
        Orientation course
        Aws re start program
        Digital marketing e commerce
Would you like to search something else?(Y/N) n

```

**Example of log file**
9bd00ec4-07f4-4cb7-80d2-dc2033f690d4.txt
```
Search term: web.
Matches: Web development course, Orientation course, Aws re start program, Digital marketing e commerce.

```

> Hints:
>
> - Start by defining various *ROOT* constants to make the code safer and easier to read.
>
> - Ask the command line user for a name. This name will be the one used to create the directory under `log`. Then, ask the user for the term of search.
>
> - Define your own custom functions (at least for executing the search and for logging).
>
> - Create the `log/{user}` directory only when the script is about to create the log file, not earlier.
>
> - You can use the module `sys` and the function `sys.exit(1)` (or different error codes) to exit the script if the user inputs no data in either of the two variables before.
>
> - Use the module `uuid` and the function `uuid.uuid4()` to obtain unique file names when writing on the log.
>
> - Use the `print` keyword arguments (`sep`, `end` and `file`) to produce the exact result required.

Try the following input values and compare your result with these:
**Test case 1**
```
$ python3 script.py
What is your name? Patty
Welcome Patty!
What word would you like to search for? web
** Found 4 matching articles: **
        Web development course
        Orientation course
        Aws re start program
        Digital marketing e commerce
Would you like to search something else?(Y/N) n
$
```
Directory tree:
```
+ src
  + data
    + articles
      - Web development course.txt
      - Orientation course.txt
      - Aws re start program.txt
      - Digital marketing e commerce.txt
    + log
      + Patty
        - 9bd00ec4-07f4-4cb7-80d2-dc2033f690d4.txt
```
Log file created:
```
Search term: web
Matches: Web development course, Orientation course, Aws re start program, Digital marketing e commerce.
```

**Test case 2**
```
$ python3 script.py
What is your name?
Please, provide a name.
$
```
Nothing will be created.

**Test case 3**
```
$ python3 script.py
What is your name? Peter
Welcome Peter!
What word would you like to search for?
Please, provide a term of search.
$
```
Nothing will be created.

**Test case 4**
```
What is your name? Peter
Welcome Peter!
What word would you like to search for? google
** Found 4 matching articles: **
        Web development course
        Orientation course
        Aws re start program
        Digital marketing e commerce
Would you like to search something else?(Y/N) y   
****************************************************************************************************
What word would you like to search for? amazon
** Found 1 matching articles: **
        Aws re start program
Would you like to search something else?(Y/N) y
****************************************************************************************************
What word would you like to search for? career
** Found 4 matching articles: **
        Web development course
        Orientation course
        Aws re start program
        Digital marketing e commerce
Would you like to search something else?(Y/N) n
```
The directory tree should look like this:
```
+ src
  + data
    + articles
      - Web development course.txt
      - Orientation course.txt
      - Aws re start program.txt
      - Digital marketing e commerce.txt
    + log
      + Patty
        - 9bd00ec4-07f4-4cb7-80d2-dc2033f690d4.txt
      + Peter
        - 3eb6ca7e-124d-4047-bb2a-69c847797d42.txt
        - 7fbe8f94-4bb0-4cbc-9ae9-f1fbea8ee5c0.txt
        - ae27c009-8023-4fea-9fe3-e31224e49e8e.txt
```
And the last three files created should look like this:

```
Search term: google.
Matches: Web development course, Orientation course, Aws re start program, Digital marketing e commerce.

```
```
Search term: amazon.
Matches: Aws re start program.

```

```
Search term: career.
Matches: Web development course, Orientation course, Aws re start program, Digital marketing e commerce.

```
