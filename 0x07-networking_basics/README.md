<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# 0x07. Networking basics #0
System engineering & DevOps ― Networking

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#Coding-style)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#usage)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#installation)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x07-networking_basics#author)
---
## Purpose
- To learn what's OSI model
- To learn What is a LAN and WAN
- To learn What is the Internet
- To learn What is IP address
- To learn What is TCP/UDP
- To learn What are TCP/UDP Ports
- To learn What tool/protocol is often used to check if a device is connected to a network
---
## Coding style
- All Bash script text files are executable and are interpreted on Ubuntu 14.04 LTS. They all pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors.
---
## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x07-networking_basics
```
---
## Usage
```
$ ./<filename>
```
---
### Usage Example
```
$ ./3-UDP_and_TCP
10.0.2.15
127.0.0.1
```
---
## Files
|File| File Hierarchy  | Description 
|---|----|-----
| `0-OSI_model` | [0-OSI_model](0-OSI_model) | **Multiple choice question**:<br /> **Q1. What is the OSI model?**<br />1.Set of specifications that network hardware manufacturers must respect. <br />2.The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology. <br />3.The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology.  <br />**Q2. How is the OSI model organized?**  <br />1.Alphabetically  <br /> 2.From the lowest to the highest level <br />3.Randomly
| `1-types_of_network` | [1-types_of_network](1-types_of_network) | **Multiple choice question**: <br />**Q1.What type of network are Holberton iMacs connected to?**<br /> 1.Internet.<br /> 2.WAN. <br /> 3.LAN <br />**Q2.What type of network could connect the Holberton HQ office with the Holberton-Gandi office?**<br /> 1.Internet.<br /> 2.WAN. <br />3.LAN <br />**Q3.What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?**<br /> 1.Internet.<br /> 2.WAN. <br />3.LAN
| `2-MAC_and_IP_address` | [2-MAC_and_IP_address](2-MAC_and_IP_address) | **Multiple choice question**: <br />**Q1.What is a MAC address?**<br /> 1.The name of a network interface.<br /> 2.The unique identifier of a network interface. <br /> 3.A network interface <br />**Q2.What is an IP address?**<br /> 1.Is to devices connected to a network what postal address is to houses.<br /> 2.The unique identifier of a network interface. <br />3.Is a number that network devices use to connect to networks
| `3-UDP_and_TCP` | [3-UDP_and_TCP](3-UDP_and_TCP) | **Multiple choice question**: <br />**Q1.Which statement is correct for the TCP box?**<br /> 1.Is a protocol that is transferring data in a slow way but surely.<br /> 2.Is a protocol that is transferring data in a fast way and might loss data along in the process. <br />**Q2.Which statement is correct for the UDP box?**<br /> 1.Is a protocol that is transferring data in a slow way but surely.<br /> 2.Is a protocol that is transferring data in a fast way and might loss data along in the process. <br /> **Q3.Which statement is correct for the TCP worker?**<br /> 1.Have you received boxes x, y, z?.<br /> 2.May I increase the rate at which I am sending you boxes?
| `4-TCP_and_UDP_ports` | [4-TCP_and_UDP_ports](4-TCP_and_UDP_ports) | **Bash script that displays listening ports:** <br /> That only shows listening sockets<br />That shows the PID and name of the program to which each socket belongs
| `5-is_the_host_on_the_network` | [5-is_the_host_on_the_network](5-is_the_host_on_the_network) | **Bash script that pings an IP address passed as an argument:** <br /> Accepts a string as an argument<br />Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed <br />Ping the IP 5 times
## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)