<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x0B. Web server
System engineering & DevOps ― Web stack

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#Coding-style)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#usage)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#installation)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0B-web_server#author)

## Purpose
- To learn What DNS stands for
- To learn What is DNS main role
- To learn What are DNS record types for: `A`, `CNAME`, `TXT`, `MX` 
- To learn What What is the main role of a web server
- To learn What is a child process and Why web server usually have a parent process and child processes
- To learn What are the main HTTP requests

## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS. They all pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors.

## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x0B-web_server
```

## Usage
```
$ ./<filename>
```

### Usage Example
```
$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```

## Files
|File| File Hierarchy  | Description 
|---|----|-----
| `0-transfer_file` | [0-transfer_file](0-transfer_file) |  a Bash script that transfers a file from our client to a server
| `1-install_nginx_web_server` | [1-install_nginx_web_server](1-install_nginx_web_server) |  a Bash script that configures a new Ubuntu machine 
| `2-setup_a_domain_name` | [2-setup_a_domain_name](2-setup_a_domain_name) | Setup a domain name
| `3-redirection` | [3-redirection](3-redirection) | Configure your Nginx server so that /redirect_me is redirecting to another page.
| `4-not_found_page_404` | [4-not_found_page_404](4-not_found_page_404) | Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.


## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)