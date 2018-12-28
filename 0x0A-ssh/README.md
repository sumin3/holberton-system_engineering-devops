<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x0A. SSH
System engineering & DevOps ― Security

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#Coding-style)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#usage)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#installation)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0A-ssh#author)
---
## Purpose
- To learn What is server and SSH
---
## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS. They all pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors.
---
## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x0A-ssh
```
---
## Usage
```
$ ./<filename>
```
---
### Usage Example
```
$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in holberton.
Your public key has been saved in holberton.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
```
---
## Files
|File| File Hierarchy  | Description 
|---|----|-----
| `0-use_a_private_key` | [0-use_a_private_key](0-use_a_private_key) |  a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
| `1-create_ssh_key_pair` | [1-create_ssh_key_pair](1-create_ssh_key_pair) |  a Bash script that creates an RSA key pair.
| `2-ssh_config` | [2-ssh_config](2-ssh_config) | **configure the ssh configure file to the requirements below, so that you can connect to a server without typing a password:** <br />1. Your SSH client configuration must be configured to use the private key ~/.ssh/holberton <br />2. Your SSH client configuration must be configured to refuse to authenticate using a password
---
## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)