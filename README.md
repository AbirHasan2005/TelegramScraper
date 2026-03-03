# Telegram Scraper v1.6 [Get Access to ALL FILES](https://github.com/AbirHasan2005/TelegramScraper?tab=readme-ov-file#support--pricing)

A powerful, multi-account Telegram group member scraper and adder with encrypted session storage, automatic account rotation, and a rich terminal UI.

---

## Features

- **Multi-Account Support** — Log in multiple Telegram accounts and rotate between them automatically
- **3 Login Methods** — Phone number (OTP + 2FA), QR code scan, or Telegram Desktop TData import
- **2 Scraping Modes** — Scrape from the visible members list, or extract hidden members from message history
- **2 Adding Modes** — Rush Adder (tracks progress by removing added members from CSV) or Calm Adder (keeps CSV intact)
- **Session Encryption** — All session strings encrypted with Fernet (AES-128) using PBKDF2 key derivation
- **FloodWait Handling** — Automatic wait with jitter for small delays; switches account on large delays (1hr+)
- **Checkpoint Resume** — Interrupted hidden-member scrapes can be resumed from where they left off
- **Account Cooldown Tracking** — Persistent cooldown tracking across sessions with automatic expiry
- **Rich Terminal UI** — Progress bars, spinners, styled tables, and color-coded output
- **Session Management** — List all sessions, test connectivity, and clean up inactive accounts
- **Structured Logging** — Rotating file logs (never logs sensitive data like session strings)
- **Atomic CSV Writes** — Data written to temp file first, then replaced — no corruption on crash

[Get Access to ALL FILES](https://github.com/AbirHasan2005/TelegramScraper?tab=readme-ov-file#support--pricing)
---

## Prerequisites

- **Python 3.8+**
- **Git** (required to install the Pyrogram fork)
- **Telegram API Credentials** (API_ID and API_HASH)

---

## Installation

### 1. Get the project

**If you have repo access:**
```bash
git clone <repository-url>
cd TelegramScraper
```

**If you received a ZIP:**
```
Extract the ZIP to a folder and open a terminal there.
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** TgCrypto is mandatory. Without it, Pyrogram falls back to a pure-Python AES implementation that is extremely slow and will lock up scraping tasks. The app will refuse to start if TgCrypto is not installed.

If TgCrypto fails to install, make sure you have a C compiler available:
- **Windows:** Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **Linux/Termux:** `sudo apt install build-essential` (or `pkg install build-essential` on Termux)
- **macOS:** `xcode-select --install`

### 3. Get Telegram API credentials

1. Visit [https://my.telegram.org/apps](https://my.telegram.org/apps)
2. Log in with your Telegram phone number
3. Click **"Create New Application"**
4. Fill in the app name (e.g., "MyApp") and any other required fields
5. Copy your **API_ID** (a number) and **API_HASH** (a string)

### 4. Create the `.env` file

Create a file named `.env` in the project root:

```env
API_ID=12345678
API_HASH=your_api_hash_here
```

Replace the values with your actual credentials from step 3.

### 5. Run

```bash
python main.py
```

---

## Quick Start

When you launch the tool, you'll see the main menu:

```
TelegramScraper v1.5
ℹ 0 sessions loaded (check Manage Sessions for status)

┌─────────────────────┐
│      Main Menu      │
├─────────────────────┤
│  01  Login Telegram Account
│  02  Members Scraper
│  03  Members Adder
│  04  Manage Sessions
│
│  99  About
│  00  Exit
└─────────────────────┘
› Choose an option:
```

**Typical workflow:**
1. **Login** one or more Telegram accounts (Option 01)
2. **Scrape** members from a source group (Option 02)
3. **Add** scraped members to a target group (Option 03)

---

## Usage Guide

### Option 01 — Login Telegram Account

This option lets you authenticate Telegram accounts. Sessions are encrypted and stored locally in the `sessions/` directory.

#### First-Time Encryption Setup

On your first login, you'll be asked to create an encryption password (minimum 4 characters). This password protects all your stored session strings using Fernet encryption with PBKDF2 key derivation (480,000 iterations). On subsequent logins, you'll enter this same password to decrypt existing sessions and encrypt new ones.

> **Important:** If you forget your encryption password, stored sessions cannot be recovered. You'll need to log in again.

#### Sub-Menu

```
01 - Login with Phone Number
02 - Login from TData
03 - Login with QR Code
00 - Go Back
```

#### Login with Phone Number

1. Enter your phone number in international format (e.g., `+1234567890`)
2. Telegram sends an OTP code to your phone/app
3. Enter the OTP code (spaces are automatically stripped)
4. If your account has 2FA enabled, enter your 2FA password (input is masked)
5. Session is encrypted and saved

#### Login with QR Code

1. A QR code is displayed in your terminal
2. Open Telegram on your phone → Settings → Devices → Scan QR Code
3. The tool automatically detects the scan (polls every 5 seconds)
4. If 2FA is enabled, enter your password
5. Session is encrypted and saved

#### Login from TData

1. Provide the path to your Telegram Desktop `tdata` folder
   - **Windows:** `%APPDATA%\Telegram Desktop\tdata`
   - **Linux:** `~/.local/share/TelegramDesktop/tdata`
   - **macOS:** `~/Library/Application Support/Telegram Desktop/tdata`
2. The tool extracts the auth key and converts it to a Pyrogram session
3. Connectivity is verified by calling `get_me()`
4. Session is encrypted and saved

---

### Option 02 — Members Scraper

Scrape members from a Telegram group and save them to `members.csv`.

#### Sub-Menu

```
01 - Scrape Non-Hidden Members (from Group's Members List)
02 - Scrape Hidden Members (from Group's Messages/Mentions)
00 - Go Back
```

#### Scrape Hidden Members

Scrapes members from **message history and mentions** — useful when the members list is restricted.

1. Enter the group link or username
2. The tool iterates through all messages in the group, extracting users from:
   - Message authors
   - `@username` mentions
   - Text mentions (clickable names that link to profiles)
3. A checkpoint is saved every 50 unique members to `scrape_checkpoint.json`
4. If interrupted (Ctrl+C), progress is saved — next time you scrape the same group, you'll be asked to **resume from the checkpoint**
5. Results saved to `members.csv`

**Best for:** Private groups with hidden member lists, or when you want to capture active participants.

[Get Access to ALL FILES](https://github.com/AbirHasan2005/TelegramScraper?tab=readme-ov-file#support--pricing)

#### Scrape Non-Hidden Members

Scrapes from the group's **official members list** (visible when you tap "Members" in group info).

1. Enter the group link or username (e.g., `https://t.me/mygroup`, `@mygroup`, or `mygroup`)
2. The tool selects an available account (skips accounts on cooldown)
3. Iterates through the members list, filtering out bots and deduplicating by user ID
4. A spinner shows real-time progress: member count, group name, and which account is being used
5. Results saved to `members.csv`

**Best for:** Public groups or groups where the members list is visible.

#### Output Format (`members.csv`)

```csv
Name,ID,Username,Access Hash,Group Name,Group ID
John Doe,123456789,johndoe,1234567890123456,MyGroup,-100987654321
Jane,987654321,,9876543210987654,MyGroup,-100987654321
```

---

### Option 03 — Members Adder

Add scraped members from `members.csv` to a target group.

#### Sub-Menu

```
01 - Rush Adder (Remove user from 'members.csv' after adding)
02 - Calm Adder (Keep user in 'members.csv' after adding)
00 - Go Back
```

#### Rush Adder vs Calm Adder

| | Rush Adder | Calm Adder |
|---|---|---|
| **After adding a member** | Removes them from `members.csv` | Keeps `members.csv` unchanged |
| **Best for** | Production runs — tracks progress, no duplicate adds on restart | Testing or intentional re-adds |

#### How Adding Works

1. Enter the target group link or username
2. A progress bar appears showing: percentage, added count, skipped count, elapsed time, and ETA
3. For each member in `members.csv`:
   - Attempts to add them to the group
   - On success: waits a **random 3–8 seconds** before the next add (jitter to avoid detection)
   - If already a member: skips (no delay)
   - If privacy-restricted, kicked, or invalid: skips with reason logged
4. Completion summary shows total processed, added, skipped, and remaining

#### FloodWait Handling

- **Small FloodWait (< 1 hour):** Waits in place with added jitter, then retries with the same account
- **Large FloodWait (>= 1 hour):** Puts the account on cooldown and **switches to the next available account**
- **PeerFlood (spam flag):** Automatically tries a workaround (add as contact → add to group → remove contact)

#### Account Rotation

If you have multiple accounts logged in, the adder cycles through them automatically. When one account hits a large FloodWait, it moves to the next. Cooldown times are persisted in `account_cooldowns.json` so they survive restarts.

---

### Option 04 — Manage Sessions

View, test, and clean up your stored Telegram sessions.

#### Sub-Menu

```
01 - List All Sessions
02 - Test All Sessions
03 - Remove Inactive Sessions
00 - Go Back
```

#### List All Sessions

Displays a table of all stored sessions:

```
┌───┬─────────────────┬──────────┬───────────┐
│ # │ Phone           │ Status   │ Encrypted │
├───┼─────────────────┼──────────┼───────────┤
│ 1 │ +1234***890     │ Active   │ Yes       │
│ 2 │ +9876***321     │ Cooldown │ Yes       │
└───┴─────────────────┴──────────┴───────────┘
```

- Phone numbers are masked for security
- Status shows Active, Cooldown (with remaining time), or error reason
- Encrypted column shows whether the session string is Fernet-encrypted

#### Test All Sessions

Connects each session to Telegram and verifies it's still valid:

1. Enter your encryption password (to decrypt sessions)
2. Each session is tested by calling `get_me()`
3. Results shown in a table: OK (with user ID) or FAILED (with error reason)

#### Remove Inactive Sessions

Finds sessions with a non-Active status (banned, deactivated, auth key invalid, etc.) and offers to delete them:

1. Shows a table of inactive sessions with their status
2. Asks for confirmation: `Remove all inactive sessions? (y/n)`
3. On confirm: deletes the session CSV files from disk

---

### Option 99 — About

Displays tool information: name, version, developer, and contact details.

---

## Project Structure

```
TelegramScraper/
├── main.py                  # Entry point, main menu loop
├── configs.py               # Config class, loads .env variables
├── crypto.py                # Fernet encryption/decryption for sessions
├── account_manager.py       # Multi-account rotation & cooldown tracking
├── retry.py                 # @async_retry decorator with exponential backoff
├── logger.py                # Rotating file logger setup
├── utils.py                 # CSV I/O, input helpers, phone validation
├── requirements.txt         # Pinned dependencies
├── .env                     # Your API credentials (not in repo)
├── LICENSE                  # License & Terms of Service
│
├── funcs/
│   ├── ui.py                # Rich console styling, prompts, spinners
│   ├── helpers.py           # Session loading, member saving helpers
│   └── options_handlers/
│       ├── login.py         # Phone, QR, TData login flows
│       ├── scrape_members.py# Non-hidden & hidden member scraping
│       ├── add_members.py   # Rush & calm member adding
│       ├── manage_sessions.py # List, test, cleanup sessions
│       └── about.py         # About screen
│
├── sessions/                # Encrypted session CSVs (not in repo)
├── logs/                    # Rotating log files (not in repo)
├── members.csv              # Scraped member data (not in repo)
└── scrape_checkpoint.json   # Resume checkpoint (not in repo)
```

[Get Access to ALL FILES](https://github.com/AbirHasan2005/TelegramScraper?tab=readme-ov-file#support--pricing)
---

## Security

- **Session Encryption:** All Telegram session strings are encrypted using Fernet (AES-128-CBC + HMAC-SHA256). The encryption key is derived from your password using PBKDF2 with 480,000 iterations and a random 16-byte salt.
- **Local Storage Only:** All data (sessions, member lists, logs) is stored locally on your machine. The tool does not send data to any external server.
- **Phone Masking:** Phone numbers are always displayed masked in the UI and logs (e.g., `+1234***890`).
- **Credential Safety:** API credentials are loaded from `.env` which is excluded from version control via `.gitignore`.
- **No Session Logging:** Session strings are never written to log files.

---

## Troubleshooting

### TgCrypto won't install

TgCrypto is a C extension that requires a compiler:
- **Windows:** Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/), then retry `pip install TgCrypto`
- **Linux:** Run `sudo apt install build-essential python3-dev`, then retry
- **Termux:** Run `pkg install build-essential`, then retry
- **macOS:** Run `xcode-select --install`, then retry

### "API_ID and API_HASH must be set"

You're missing the `.env` file or it has incorrect values:
1. Create a `.env` file in the project root
2. Add your credentials: `API_ID=12345678` and `API_HASH=your_hash`
3. Make sure there are no spaces around the `=` sign

### FloodWait / PeerFlood errors

These are Telegram rate limits, not bugs:
- **FloodWait:** Telegram is asking you to slow down. The tool handles this automatically — small waits are waited out, large waits trigger account switching.
- **PeerFlood:** Your account has been flagged for adding too many users. Switch to a different account or wait a few hours/days.

### Session decryption failure

If you see decryption errors when testing sessions:
- Make sure you're entering the correct encryption password
- If you've forgotten your password, delete the affected session files from `sessions/` and log in again

### Scraping returns fewer members than expected

- **Non-hidden scraping** only works if the group's members list is visible. Some groups restrict this.
- **Hidden scraping** extracts members from messages, so inactive members who never post or get mentioned won't be found.
- Bots are automatically filtered out from results.

---

## FAQ

**Can I run multiple instances at the same time?**
No. Session files and CSV data are shared, so running multiple instances can cause conflicts and data corruption.

**Is my session safe?**
Yes. Session strings are encrypted with Fernet using a password-derived key (PBKDF2, 480k iterations). Without your password, the encrypted session is unreadable.

**What if I forget my encryption password?**
Stored sessions cannot be recovered. You'll need to delete the `sessions/` directory and log in to your accounts again.

**Why does scraping miss some members?**
Non-hidden scraping only sees members in the public list. For groups that hide their member list, use the hidden scraping option which extracts members from message history. Members who never posted or were mentioned won't be captured by either method.

**How many accounts do I need?**
Minimum 1. However, having multiple accounts helps with FloodWait rotation — when one account gets rate-limited, the tool automatically switches to the next available one.

**Does this work on mobile (Termux)?**
Yes. The tool runs on any platform with Python 3.8+: Windows, macOS, Linux, and Termux (Android). All dependencies are cross-platform.

**What happens if I interrupt a scrape with Ctrl+C?**
For hidden member scraping, progress is automatically saved to a checkpoint file. Next time you scrape the same group, you'll be offered to resume. For non-hidden scraping, members collected so far are still saved.

---

## Support & Pricing

| | |
|---|---|
| **Price** | 80 USD |
| **Purchase & Support** | [Contact on Telegram](https://t.me/AkibHridoy) |

### Developer

**Abir Hasan**
- GitHub: [github.com/AbirHasan2005](https://github.com/AbirHasan2005)
- Telegram: [t.me/AbirHasan2005](https://t.me/AbirHasan2005)
