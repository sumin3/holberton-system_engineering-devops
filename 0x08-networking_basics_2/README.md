<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x08. Networking basics #1
System engineering & DevOps ― Networking

## Purpose
- To learn what's localhost/127.0.0.1
- To learn What is 0.0.0.0
- To learn What is /etc/hosts
- To learn How to display your machine’s active network interfaces

## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS. They all pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors.

## Usage
```
$ ./<filename>
```

### Usage Example
```
$ ./3-show_attached_IPs
10.0.2.15
127.0.0.1
```

## Files
|File| File Hierarchy  | Description 
|---|----|-----
| `0-localhost` | [0-localhost](0-localhost) | **Multiple choice question**:<br /> What is localhost? <br />1.A hostname that means this IP. <br />2.A hostname that means this computer. <br />3.An IP attached to a computer.
| `1-wildcard` | [1-wildcard](1-wildcard) | **Multiple choice question**: <br />What is 0.0.0.0?<br /> 1.All IPv4 addresses on the local machine.<br /> 2.All the IPs. 3.It means null in networking
| `2-change_your_home_IP` | [2-change_your_home_IP](2-change_your_home_IP) | Bash script that configures an Ubuntu server with the below requirements.
| `3-show_attached_IPs` | [3-show_attached_IPs](3-show_attached_IPs) | Bash script that displays all active IPv4 IPs on the machine it’s executed on
| `4-port_listening_on_localhost` | [4-port_listening_on_localhost](4-port_listening_on_localhost) | Bash script that listens on port 98 on localhost.

## Authors
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)