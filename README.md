# linkedin_bot
LinkedIn bot to perform automatic tasks

## Setup

```bash
$ git clone https://github.com/emichester/linkedin_bot.git
$ cd linkedin_bot
$ mkdir config && touch config/data.py
$ mkdir -p config/session && touch config/session/session.ini && touch config/credentials.ini

$ echo "
[SESSION]
session_id = ''
executor_url = ''
" > config/session/session.ini


$ echo "
[LOGIN]
name = 'username@server.com'
password = 'L1nk3d1n_passw0rd'
" > config/session/credentials.ini
 
$ chmod +x bot_firefox_init.py
$ chmod +x bot_firefox_instance.py
```

Go to your favorite web browser and find the user data folder, [here](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data) you have the firefox default directory. Once you have it:

```bash
$ echo "USER_DATA_PATH = 'path/to/your/user/data/folder'" > config/data.py
```

### If you use Firefox

Download _"geckodriver"_ from [here](https://github.com/mozilla/geckodriver/releases). Then:

```bash
$ tar -xvzf geckodriver*
$ chmod +x geckodriver
$ sudo mv geckodriver /usr/bin/
```

[//]: # "https://github.com/mozilla/geckodriver/releases"
[//]: # "https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu"
[//]: # "https://tarunlalwani.com/post/reusing-existing-browser-session-selenium/"


## Install dependencies
```bash
$ pip install -r requirements.txt
```

## Usage

Open a terminal to run the following script to launch an instance of the webdriver

```bash
$ ./bot_firefox_init.py
```

Then run the instance of the process you want to follow

```bash
$ ./bot_firefox_instance.py
```

Note: One single functionality for the moment.

## Functionalities
### connect to people related to a specific subject i.e. `artificial intelligence`

Type a subject

```bash
$ ---> Introduce a subject (default='computer visions'): DevOps
```

Then press enter.

## ToDo
- Some other functions