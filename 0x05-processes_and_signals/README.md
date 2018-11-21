<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x05. Processes and signals
System engineering & DevOps ― Bash

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#Coding-style)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#installation)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#usage)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x05-processes_and_signals#author)

## Purpose
- To learn what is a PID, process. and signal.
- To learn how to find process PID
- To learn how to kill a process
- To learn What are the 2 signals that cannot be ignored

## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS. They all pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors.

## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x05-processes_and_signals
```

## Usage
```
$ ./<filename>
```

## Usage Example
```
$ ./0-what-is-my-pid
4120
```

## Files
|File| File Hierarchy  | Description 
|---|----|-----
| `0-what-is-my-pid`| [0-what-is-my-pid](0-what-is-my-pid) | Bash script that displays its PID.
| `1-list_your_processes`| [1-list_your_processes](1-list_your_processes) | Bash script that displays a list of currently running processes.
| `2-show_your_bash_pid` | [2-show_your_bash_pid](2-show_your_bash_pid) | Using your previous exercise command, write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process
| `3-show_your_bash_pid_made_easy` | [3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy) | Bash script that displays the PID, along with the process name, of processes which name contains the word bash.
| `4-to_infinity_and_beyond` | [4-to_infinity_and_beyond](4-to_infinity_and_beyond) | displays To infinity and beyond indefinitely.
| `5-kill_me_now` | [5-kill_me_now](5-kill_me_now) | Bash script that kills 4-to_infinity_and_beyond process.
| `6-kill_me_now_made_easy` | [6-kill_me_now_made_easy](6-kill_me_now_made_easy) | Bash script that kills 4-to_infinity_and_beyond process.
| `7-highlander` | [7-highlander](7-highlander) | **Bash script that displays:**<br />To infinity and beyond indefinitely<br />With a sleep 2 in between each iteration<br />I am invincible!!! when receiving a SIGTERM signal
| `8-beheaded_process` | [8-beheaded_process](8-beheaded_process) | Bash script that kills the process 7-highlander.

## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)