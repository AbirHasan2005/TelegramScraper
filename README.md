# TelegramScraper v1.3
Using this tool you can easily add so many members from any group to your group. Less than 2 minutes. Super easy. Time saver. But this tool is only for educational purpose. You could be banned from Telegram. So be careful. Recommanded to use this tool only on Termux.

![GitHub repo size](https://img.shields.io/github/repo-size/AbirHasan2005/TelegramScraper?label=Repo%20Size) ![GitHub followers](https://img.shields.io/github/followers/AbirHasan2005?style=social)(https://github.com/AbirHasan2005)

## Telegram Group:
<a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>
### Join Telegram group for help, feedback, details and chats. Group Owner: @AbirHasan2005

## How to Setup API:
- Go to https://my.telegram.org and Login.
- Click on API development tools and fill the required fields.
- Put app name you want & select Other in Platform.
- After clicking Create App, Copy "api_id" & "api_hash" from there. (This will be used in `setup.py`)
<p><img src="https://i1.wp.com/python.gotrained.com/wp-content/uploads/2019/01/desc.png?resize=768%2C479&ssl=1"></p>

## How To Install:

$ `pkg install git python -y`

$ `git clone https://github.com/AbirHasan2005/TelegramScraper`

$ `cd TelegramScraper`

$ `chmod +x * && python3 setup.py`

## To Genrate User Data:

$ `python3 scraper.py`

- (`members.csv` is default if you changed name use it)
- Send Bulk SMS To Collected Data

$ `python3 smsbot.py members.csv`

- Add users to your group

$ `python3 add2group.py members.csv`
### Or,
$ `python3 Adder.py`

---

## Follow Me on:
### GitHub: https://github.com/AbirHasan2005
### Twitter: https://twitter.com/AbirHasan2005  ![Twitter Follow](https://img.shields.io/twitter/follow/AbirHasan2005?style=social)
### Facebook: https://facebook.com/AbirHasan2005
### Instagram: https://instagram.com/AbirHasan2005
