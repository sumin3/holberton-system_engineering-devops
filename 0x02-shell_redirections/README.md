<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x02. Shell, I/O Redirections and filters
System engineering & DevOps ― Bash

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#Coding-style)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#installation)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#usage)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x02-shell_redirections#author)

## Purpose
- To learn what do the commands head, tail, find, wc, sort, uniq, grep, tr do
- To learn How to redirect standard output to a file
- To learn How to get standard input from a file instead of the keyboard
- To learn How to send the output from one program to the input of another program
- To learn How to combine commands and filters with redirections
- To Understand what do the special characters (white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde) and how and when to use them

## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS.

## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x02-shell_redirections
```

## Usage
```
$ ./<filename>
```

### Usage Example
```
$ ./1-hello_you 
hello julien
```
## Files
Task number | File | Desc
---|--|---
0 |  [0-hello_world](0-hello_world) |Write a script that prints “Hello, World”, followed by a new line to the standard output.
1 |  [1-confused_smiley](1-confused_smiley) |Write a script that displays a confused smiley \"(Ôo)'.
2 |  [2-hellofile](2-hellofile) |Display the content of the /etc/passwd file.
3 |  [3-twofiles](3-twofiles) |Display the content of /etc/passwd and /etc/hosts
4 |  [4-lastlines](4-lastlines) |Display the last 10 lines of /etc/passwd
5 |  [5-firstlines](5-firstlines) |Display the first 10 lines of /etc/passwd
6 |  [6-third_line](6-third_line) |Write a script that displays the third line of the file iacta.
7 |  [7-file](7-file) |Write a shell script that creates a file containing the text Holberton School ending by a new line.
8 |  [8-cwd_state](8-cwd_state) |Write a script that writes into the file ls_cwd_content the result of the command ls -la
9 |  [9-duplicate_last_line](9-duplicate_last_line) |Write a script that duplicates the last line of the file iacta
10 |  [10-no_more_js](10-no_more_js) |Write a script that deletes all the regular files (not the directories) with a .js extension
11 |  [11-directories](11-directories) |Write a script that counts the number of directories and sub-directories in the current directory.
12 |  [12-newest_files](12-newest_files) |Create a script that displays the 10 newest files in the current directory
13 |  [13-unique](13-unique) |Create a script that takes a list of words as input and prints only words that appear exactly once.
14 |  [14-findthatword](14-findthatword) |Display lines containing the pattern “root” from the file /etc/passwd
15 |  [15-countthatword](15-countthatword) |Display the number of lines that contain the pattern “bin” in the file /etc/passwd
16 |  [16-whatsnext](16-whatsnext) |Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd
17 |  [17-hidethisword](17-hidethisword) |Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
18 |  [18-letteronly](18-letteronly) |Display all lines of the file /etc/ssh/sshd_config starting with a letter.
19 |  [19-AZ](19-AZ) |Replace all characters A and c from input to Z and e respectively.
20 |  [20-hiago](20-hiago) |Create a script that removes all letters c and C from input.
21 |  [21-reverse](21-reverse) |Write a script that reverse its input.
22 |  [22-users_and_homes](22-users_and_homes) |Write a script that displays all users and their home directories, sorted by users.
23 |  [100-empty_casks](100-empty_casks) |Write a command that finds all empty files and directories in the current directory and all sub-directories.
24 |  [101-gifs](101-gifs) |Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
25 |  [102-acrostic](102-acrostic) |Create a script that decodes acrostics that use the first letter of each line.
26 |  [103-the_biggest_fan](103-the_biggest_fan) |Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin) 