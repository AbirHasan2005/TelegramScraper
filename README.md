# TelegramScraper v1.4 ![GitHub repo size](https://img.shields.io/github/repo-size/AbirHasan2005/TelegramScraper?label=Repo%20Size)
Using this tool you can easily add so many members from any group to your group. Less than 2 minutes. Super easy. Time saver. But this tool is only for educational purpose. You could be banned from Telegram. So be careful. Recommanded to use this tool only on Termux.

## Telegram Group:
<a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>
#### Join Telegram group for help, feedback, details and chats.

## How to Setup API:
- Go to https://my.telegram.org and Login.
- Click on API development tools and fill the required fields.
- Put app name you want & select Other in Platform.
- After clicking Create App, Copy "api_id" & "api_hash" from there. (This will be used in `setup.py`)
<p><img src="https://i1.wp.com/python.gotrained.com/wp-content/uploads/2019/01/desc.png?resize=768%2C479&ssl=1"></p>

## How To Install? (Only for Termux!):

$ `pkg install git python -y`

$ `git clone https://github.com/AbirHasan2005/TelegramScraper`

$ `cd TelegramScraper`

$ `chmod +x * && python3 setup.py`

## To Genrate User Data:

$ `python3 scraper.py`

- (`members.csv` is default if you changed name use it)
- Send Bulk SMS To Collected Data

$ `python3 smsbot.py members.csv` [Optional]

- Add users to your group

$ `python3 adder.py `

#### Or,

$ `python3 add2group.py members.csv`

- If you need more help <a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>
---

## Follow Me on:
<a href="https://github.com/AbirHasan2005"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a> <a href="https://twitter.com/AbirHasan2005"><img src="https://img.shields.io/badge/Twitter-Follow%20on%20Twitter-informational.svg?logo=twitter"></a> <a href="https://facebook.com/AbirHasan2005"><img src="https://img.shields.io/badge/Facebook-Follow%20on%20Facebook-blue.svg?logo=facebook"></a> <a href="https://instagram.com/AbirHasan2005"><img src="https://img.shields.io/badge/Instagram-Follow%20on%20Instagram-important.svg?logo=instagram"></a>
