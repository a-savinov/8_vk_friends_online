# Watcher of Friends Online

Shows which of your friends are online now in VK

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to use

```bash
$ python vk_friends_online.py -h
usage: vk_friends_online.py [-h] [-p PASSWORD] -l LOGIN

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        User password for VK (optional)
  -l LOGIN, --login LOGIN
                        User login for VK
```

## Output example

all names are not real

**recommended**
```bash

python vk_friends_online.py -l example@example.com
Enter your VK password:
VK Online friends list:
    Lucas Black  https://vk.com/idXXXXXXXX
    Benjamin Kaur https://vk.com/idXXXXXXXX
    Oscar Hamilton https://vk.com/idXXXXXXXX
    Harry Matthews https://vk.com/idXXXXXXXX 
```
**or (not recommended**)

```bash

python vk_friends_online.py -l example@example.com -p very_hard_password
Online friends list:
    Lucas Black  https://vk.com/idXXXXXXXX
    Benjamin Kaur https://vk.com/idXXXXXXXX
    Oscar Hamilton https://vk.com/idXXXXXXXX
    Harry Matthews https://vk.com/idXXXXXXXX 
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
