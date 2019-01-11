<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

0x0D Configuration management
System engineering & DevOps ― CI/CD

## Contents
* [Purpose](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#Purpose)
* [Coding style](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#Coding-style)
* [Usage](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#usage)
* [Installation](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#installation)
* [Usage Example](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#Usage-Example)
* [Files](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#Files)
* [Author](https://github.com/sumin3/holberton-system_engineering-devops/tree/master/0x0D-configuration_management#author)


## Purpose
To learn how to use configuration management tools - Puppet

## Coding style
- All puppet manifests files end with the `.pp` are interpreted on Ubuntu 14.04 LTS. All Puppet manifests pass `puppet-lint` without any errors.

## Installation
```
git clone https://github.com/sumin3/holberton-system_engineering-devops.git
```
```
cd 0x0D-configuration_management
```

## Usage
The command is run as root
```
$ puppet apply <filename>
```

### Usage Example
```
$ puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[holberton]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
```

## Files
|File| File Hierarchy  | Description 
|---|----|-----
| `0-create_a_file.pp` | [0-create_a_file.pp](0-create_a_file.pp) |  Using Puppet, create a file in /tmp.
| `1-install_a_package.pp` | [1-install_a_package.pp](1-install_a_package.pp) |  Using Puppet, install puppet-lint.
| `2-execute_a_command.pp` | [2-execute_a_command.pp](2-execute_a_command.pp) |  Using Puppet, create a manifest that kills a process named killmenow.
## Author
Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)