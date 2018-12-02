<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x01. Shell, permissions
System engineering & DevOps ― Bash

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#Coding-style)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#installation)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#usage)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x01-shell_permissions#author)

## Purpose
- To learn What do the commands chmod, sudo, su, chown, chgrp do, and how to use them
- To learn Linux file permissions
- To learn How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- To learn How to run a command with root privileges
- To learn How to change user ID or become superuser
- To learn How to print real and effective user and group IDs

## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS.

## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x01-shell_permissions
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
0 | [0-iam_betty](0-iam_betty) |  Create a script that changes your user ID to betty.
1 | [1-who_am_i](1-who_am_i) |  Write a script that prints the effective userid of the current user
2 | [2-groups](2-groups) |  Write a script that prints all the groups the current user is part of.
3 | [3-new_owner](3-new_owner) |  Write a script that changes the owner of the file hello to the user betty.
4 | [4-empty](4-empty) |  Write a script that creates an empty file called hello.
5 | [5-execute](5-execute) |  Write a script that adds execute permission to the owner of the file hello
6 | [6-multiple_permissions](6-multiple_permissions) |  Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7 | [7-everybody](7-everybody) |  Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
8 | [8-James_Bond](8-James_Bond) |  Write a script that sets the permission to the file hello.
9 | [9-John_Doe](9-John_Doe) |   Write a script that sets the mode of the file hello
10 | [10-mirror_permissions](10-mirror_permissions) |  Write a script that sets the mode of the file hello the same as olleh’s mode.
11 | [11-directories_permissions](11-directories_permissions) |  Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
12 | [12-directory_permissions](12-directory_permissions) |  Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.
13 | [13-change_group](13-change_group) |  Write a script that changes the group owner to holberton for the file hello
14 | [14-change_owner_and_group](14-change_owner_and_group) |  Write a script that changes the owner to betty and the group owner to holberton for all the files and directories 
15 | [15-symbolic_link_permission](15-symbolic_link_permissions) |  Write a script that changes the owner and the group owner of the file _hello to betty and holberton
16 | [16-if_only](16-if_only) |  Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
17 | [100-Star_Wars](100-Star_Wars) |  Write a script that will play the StarWars IV episode in the terminal.
18 | [101-man_holberton](101-man_holberton) |  Create a man that looks exactly like this one and passes all checks.

## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin) 