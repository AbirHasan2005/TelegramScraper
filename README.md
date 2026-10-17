<div align="center">

# Telegram Scraper v1.7

**A powerful, multi-account Telegram group &amp; channel scraper and adder** — with encrypted session storage, automatic account rotation, proxy + device anti-detection, message broadcasting, and a rich terminal UI.

<br/>

[![Buy Now](https://img.shields.io/badge/Buy%20Now-%2480%20USD-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/)
&nbsp;
[![Buy on Telegram](https://img.shields.io/badge/Buy%20on%20Telegram-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)
&nbsp;
[![Screenshots and Demo](https://img.shields.io/badge/Screenshots%20%26%20Demo-View%20Online-24292F?style=for-the-badge&logo=googlechrome&logoColor=white)](https://telegramscraper.shop/)

<br/>

![Source Code](https://img.shields.io/badge/Source%20Code-Full%20%26%20Editable-229ED9?style=flat-square)
![Access](https://img.shields.io/badge/Access-Lifetime-2CA5E4?style=flat-square)
![Updates](https://img.shields.io/badge/Updates-Free%20Forever-229ED9?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Platforms](https://img.shields.io/badge/Platforms-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20Termux-555?style=flat-square)

</div>

---

## <img src="assets/icons/whats-included.svg" width="24" height="24" alt="" /> What You Get

Telegram Scraper is a complete, production-ready toolkit for **scraping group members and channel audiences, adding them to your groups, and broadcasting messages** — all from a clean terminal interface, across as many accounts as you need, with built-in proxy + device anti-detection.

This is a paid product. Your **one-time purchase of $80 USD** includes:

- **Complete Python source code** — fully editable, no obfuscation
- **Lifetime access** — buy once, use it forever
- **Free future updates** — every new version at no extra cost
- **Setup support** — help getting it running on your machine
- **Cross-platform** — runs on Windows, macOS, Linux, and Termux (Android)

<div align="center">

[![Buy Now](https://img.shields.io/badge/Buy%20Now-%2480%20USD-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/)
&nbsp;
[![Buy on Telegram](https://img.shields.io/badge/Buy%20on%20Telegram-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)

</div>

---

## <img src="assets/icons/features.svg" width="24" height="24" alt="" /> Features

### Accounts &amp; Sessions
- **Multi-Account Support** — Log in multiple Telegram accounts and rotate between them automatically
- **3 Login Methods** — Phone number (OTP + 2FA), QR code scan, or Telegram Desktop TData import
- **Session Encryption** — All session strings (and proxy credentials) encrypted with Fernet (AES-128) using PBKDF2 key derivation
- **Session Management** — List all sessions, test connectivity, and clean up inactive accounts

### Scraping
- **2 Group Scraping Modes** — Scrape from the visible members list, or extract hidden members from message history, mentions, and "joined the group" service messages
- **Channel Scraper** — Extract a broadcast channel's audience via its linked discussion group's roster and the authors of comments on recent posts (the only viable approach, since Telegram blocks channel subscriber lists for non-admins)
- **Checkpoint Resume** — Interrupted hidden-member and channel scrapes can be resumed from where they left off

### Adding &amp; Broadcasting
- **2 Adding Modes** — Rush Adder (tracks progress by removing added members from CSV) or Calm Adder (keeps CSV intact)
- **Message Broadcast** — Send a formatted DM to all scraped members from a Markdown file, with 30–60s delays and account rotation

### Anti-Detection
- **Proxy Manager** — Maintain a pool of SOCKS5/SOCKS4/HTTP proxies and bind one *stickily* to each account (residential/mobile recommended; datacenter IPs are flagged by Telegram)
- **Device/Client Spoofing** — New logins get a realistic sticky mobile device fingerprint instead of the default "Pyrogram on Windows" signature
- **Centralized Rate-Limiting** — Human-like jitter and a single FloodWait policy (small waits absorbed in place, large ones cooldown + rotate account) across every scraper and adder

### Safety &amp; Reliability
- **FloodWait Handling** — Automatic wait with jitter for small delays; switches account on large delays (1hr+)
- **Account Cooldown Tracking** — Persistent cooldown tracking across sessions with automatic expiry
- **Atomic CSV Writes** — Data written to temp file first, then replaced — no corruption on crash
- **Structured Logging** — Rotating file logs (never logs sensitive data like session strings)
- **Rich Terminal UI** — Progress bars, spinners, styled tables, and color-coded output

---

## ⭐ Reviews from Clients

Rated **4.8 / 5** across **640+ buyers**. Here's what people say after putting Telegram Scraper to work:

<sub><b>Verified buyers</b> — DAE EUROPE, Light | Airaa, Cinz, NAKAMA, El, Ivan, Blood007, ABC - Droll, Sallem, Cryptowiz, and hundreds more. See their proof screenshots on the <a href="https://telegramscraper.shop/">website</a>.</sub>

> ⭐⭐⭐⭐⭐ &nbsp; "Best Telegram scraper I have used. Setup was straightforward and support was responsive." — **Cinz**

> ⭐⭐⭐⭐⭐ &nbsp; "Hidden member recovery is a game-changer. Nothing else on the market does this." — **El**

> ⭐⭐⭐⭐⭐ &nbsp; "Works exactly as described. Reliable tool for community migration." — **DAE EUROPE**

> ⭐⭐⭐⭐⭐ &nbsp; "Fast delivery and clean CSV output. Highly recommended for Telegram research." — **Light | Airaa**

> ⭐⭐⭐⭐⭐ &nbsp; "Reliable across multiple accounts. FloodWait handling works as advertised." — **NAKAMA**

> ⭐⭐⭐⭐⭐ &nbsp; "Runs cleanly on VPS and Android Termux. Great value at $80." — **Ivan**

> ⭐⭐⭐⭐⭐ &nbsp; "One-time price, lifetime value. Solid purchase with no recurring fees." — **Inereal**

> ⭐⭐⭐⭐⭐ &nbsp; "Saved hours of manual work. Great value, easy to integrate with existing CRM workflows." — **Jastin**

> ⭐⭐⭐⭐⭐ &nbsp; "AES session encryption and local-only operation made the security review easy. Clean product." — **Anton**

> ⭐⭐⭐⭐⭐ &nbsp; "Support was responsive and the tool delivered as promised. Five stars." — **Pittow**

<div align="center">

**[See more reviews and proof screenshots → telegramscraper.shop](https://telegramscraper.shop/)**

</div>

---

## <img src="assets/icons/buy.svg" width="24" height="24" alt="" /> How to Buy

Getting the full tool takes about two minutes:

1. **Open the store** — visit **[telegramscraper.shop](https://telegramscraper.shop/)**, or message **[@AkibHridoy on Telegram](https://t.me/AkibHridoy)** directly.
2. **Confirm your order** — the price is **$80 USD, one-time**. It includes the complete Python source code, lifetime access, and all future updates.
3. **Arrange payment** — payment is handled directly in the Telegram chat. Just say hello and you'll be guided through it.
4. **Receive everything** — you get the full source code plus setup help so you're up and running fast.

> **One-time payment. No subscription, no recurring fees** — pay once, own it for life.

<div align="center">

[![Buy Now](https://img.shields.io/badge/Buy%20Now-%2480%20USD-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/)
&nbsp;
[![Buy on Telegram](https://img.shields.io/badge/Buy%20on%20Telegram-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)

</div>

---

## <img src="assets/icons/demo.svg" width="24" height="24" alt="" /> See It in Action

Want to see the tool before you buy? Live screenshots and a full walkthrough are on the website:

**[View screenshots and live demo at telegramscraper.shop](https://telegramscraper.shop/)**

<!-- Embed screenshots here, e.g. <img src="assets/screenshots/main.png" width="80%" /> -->

---

## <img src="assets/icons/docs.svg" width="24" height="24" alt="" /> Documentation

A full overview of what the tool does and how to use it. Expand any section below.

<details>
<summary><b>Prerequisites &amp; Installation</b></summary>

### Prerequisites

- **Python 3.8+**
- **Git** (required to install the Pyrogram fork)
- **Telegram API Credentials** (API_ID and API_HASH)

### Installation

#### 1. Get the project

After purchase you'll receive the full source. If you have repo access:
```bash
git clone <repository-url>
cd TelegramScraper
```

If you received a ZIP, extract it to a folder and open a terminal there.

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** TgCrypto is mandatory. Without it, Pyrogram falls back to a pure-Python AES implementation that is extremely slow and will lock up scraping tasks. The app will refuse to start if TgCrypto is not installed.

> **Note:** `PySocks` is included in `requirements.txt` and is required to route accounts through a proxy (see **Option 06 — Proxy Manager**). Without it, proxies are ignored and the app connects directly.

If TgCrypto fails to install, make sure you have a C compiler available:
- **Windows:** Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **Linux/Termux:** `sudo apt install build-essential` (or `pkg install build-essential` on Termux)
- **macOS:** `xcode-select --install`

#### 3. Get Telegram API credentials

1. Visit [https://my.telegram.org/apps](https://my.telegram.org/apps)
2. Log in with your Telegram phone number
3. Click **"Create New Application"**
4. Fill in the app name (e.g., "MyApp") and any other required fields
5. Copy your **API_ID** (a number) and **API_HASH** (a string)

#### 4. Create the `.env` file

Create a file named `.env` in the project root:

```env
API_ID=12345678
API_HASH=your_api_hash_here
```

Replace the values with your actual credentials from step 3.

#### 5. Run

```bash
python main.py
```

</details>

<details>
<summary><b>Quick Start</b></summary>

When you launch the tool, you'll see the main menu:

```
TelegramScraper v1.7
ℹ 0 sessions loaded (check Manage Sessions for status)

┌─────────────────────┐
│      Main Menu      │
├─────────────────────┤
│  01  Login Telegram Account
│  02  Members Scraper
│  03  Channel Scraper
│  04  Members Adder
│  05  Message Broadcast
│  06  Proxy Manager
│  07  Manage Sessions
│
│  99  About
│  00  Exit
└─────────────────────┘
› Choose an option:
```

**Typical workflow:**
1. *(Optional but recommended)* Add residential/mobile proxies in **Proxy Manager** (Option 06) before logging in
2. **Login** one or more Telegram accounts (Option 01) — bind a proxy when prompted
3. **Scrape** members from a source group (Option 02) or a channel's audience (Option 03)
4. **Add** scraped members to a target group (Option 04)
5. **Broadcast** a message to all scraped members (Option 05)

</details>

<details>
<summary><b>Usage Guide — all menu options</b></summary>

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

Scrapes members from **message history, mentions, and join events** — useful when the members list is restricted.

1. Enter the group link or username
2. The tool iterates through all messages in the group, extracting users from:
   - Message authors
   - `@username` mentions
   - Text mentions (clickable names that link to profiles)
   - "X joined the group" service messages (catches hidden members who joined but never posted)
3. A checkpoint is saved every 50 unique members to `scrape_checkpoint.json`
4. If interrupted (Ctrl+C), progress is saved — next time you scrape the same group, you'll be asked to **resume from the checkpoint**
5. Results saved to `members.csv`

**Best for:** Private groups with hidden member lists, or when you want to capture active participants.

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
Name,ID,Username,Phone Number,Access Hash,Group Name,Group ID
John Doe,123456789,johndoe,,1234567890123456,MyGroup,-100987654321
Jane,987654321,,,9876543210987654,MyGroup,-100987654321
```

> The same `members.csv` is shared by the Channel Scraper, Members Adder, and Message Broadcast.

---

### Option 03 — Channel Scraper

Extract a broadcast **channel's** audience and save it to `members.csv`.

#### Why a channel can't be scraped directly

Telegram enforces, server-side, that only **admins** can list a broadcast channel's subscribers — any non-admin call to fetch the participant list returns `CHAT_ADMIN_REQUIRED`. No library, fork, or "letter-by-letter search" trick bypasses this. So instead of the (impossible) direct dump, this option harvests the channel's audience through two public **side-channels** via its linked discussion group:

- **Vector A — Discussion members:** the channel's linked discussion supergroup. The tool auto-joins it and scrapes the visible member roster. **If the roster is hidden by admins, it automatically falls back to the "hidden members" technique** — scanning the discussion group's message history for authors, joiners, and mentioned users (the same engine as Option 02's hidden scraper).
- **Vector B — Comment authors:** it walks **all** of the channel's posts and collects the user IDs/usernames of everyone who commented.

#### How It Works

1. Enter the channel link or username (e.g. `https://t.me/durov`, `@durov`, or `durov`)
2. Choose whether to use **Takeout mode** (insulates bulk reads from interactive flood limits; may add a short startup delay)
3. Vector A runs first (roster, or the hidden-history fallback), then Vector B scans **every** post for commenters; results are merged and de-duplicated by user ID. Because it scans all posts, a large channel can take a while — requests are paced and progress is checkpointed
4. A checkpoint is saved periodically to `scrape_channel_checkpoint.json` — if interrupted (Ctrl+C), progress is saved and you'll be offered to **resume** next time
5. Results are saved to `members.csv`, with the source tagged in the Group Name column (`<Channel> (discussion)` or `<Channel> (comments)`)

> If you point this at a normal group/supergroup it will tell you to use the **Members Scraper** instead.

**Best for:** building an audience list from a channel you are *not* an admin of.

---

### Option 04 — Members Adder

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

### Option 05 — Message Broadcast

Send a formatted direct message to all scraped members in `members.csv`.

#### How It Works

1. On first use, a sample template file (`message_template.md`) is created in the project root — you can edit it or use your own `.md` file
2. A **syntax guide** is displayed showing supported Markdown formatting and how it renders on Telegram
3. Enter the path to your `.md` message file
4. The message is converted to Telegram-compatible HTML and a **preview** is shown for confirmation
5. After confirming, messages are sent one-by-one to each user in `members.csv`
6. Each successfully messaged user is **removed from `members.csv`** (allows resuming on restart)

#### Supported Markdown Syntax

| Markdown | Telegram Result |
|---|---|
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `~~strikethrough~~` | ~~strikethrough~~ |
| `[link text](url)` | Clickable link |
| `` `inline code` `` | `monospace` |
| ```` ```code block``` ```` | Code block |
| `# Header` | **Bold header line** |
| `- list item` | Bullet point |

> **Note:** The maximum message length is 4096 characters (after HTML conversion). Messages exceeding this limit will be rejected before sending.

#### Delay &amp; Rate Limiting

- **30–60 seconds** random delay between each message (mimics human behavior)
- **Small FloodWait (< 1 hour):** Waits with jitter, then retries
- **Large FloodWait (>= 1 hour):** Switches to the next available account
- Account cooldowns are persisted in `account_cooldowns.json`

#### Error Handling

| Scenario | Action |
|---|---|
| User blocked the account | Skipped, removed from CSV |
| User account deactivated | Skipped, removed from CSV |
| User not found (invalid ID/username) | Skipped, removed from CSV |
| User has privacy restrictions | Skipped, **kept in CSV** (may change later) |
| Sending account deactivated/banned | Marked inactive, switches to next account |
| Ctrl+C interrupted | Stops gracefully, CSV reflects partial progress |

---

### Option 06 — Proxy Manager

Maintain a pool of proxies and bind them to accounts. Proxies are **optional** — an account with no bound proxy connects directly.

#### Sub-Menu

```
01 - Add Proxy
02 - List Proxies
03 - Test All Proxies
04 - Assign Proxy to Account
05 - Unassign Account Proxy
06 - Remove Proxy
00 - Go Back
```

#### IP reputation matters

Telegram scores the outbound IP/ASN of every session:

| IP type | Trust | Notes |
|---|---|---|
| **Datacenter** (AWS, DigitalOcean, Hetzner) | ❌ Flagged | Heavily restricted; fast bans |
| **Residential** (home ISP) | ✅ Good | Reliable for scraping |
| **Mobile** (4G/5G carrier) | ⭐ Best | Highest trust, most resilient |

#### Sticky binding

A proxy is bound to an account for its **entire lifecycle** — the tool never rotates a session's IP mid-flight (that looks like session hijacking and gets the account terminated). For best results, **bind a proxy at login**; assigning one to an already-established session is possible but changes its IP mid-life and carries some risk (the tool warns you).

- **Add Proxy:** enter scheme (`socks5`/`socks4`/`http`), host, port, optional username/password, and a type label. Credentials are encrypted at rest with your session password.
- **Test All Proxies:** opens an MTProto connection through each proxy and reports reachability + latency.
- **Assign / Unassign:** bind or unbind a pool proxy to a logged-in account.

---

### Option 07 — Manage Sessions

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

</details>

<details>
<summary><b>Project Structure</b></summary>

```
TelegramScraper/
├── main.py                  # Entry point, main menu loop
├── configs.py               # Config class, loads .env variables + tunable constants
├── crypto.py                # Fernet encryption/decryption for sessions & secrets
├── account_manager.py       # Multi-account rotation & cooldown tracking
├── client_factory.py        # Single Client builder (injects proxy + device)
├── proxy_store.py           # Proxy pool + per-account sticky binding store
├── device_profiles.py       # Realistic device fingerprints for spoofing
├── ratelimit.py             # Human-like jitter + central FloodWait policy
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
│       ├── login.py         # Phone, QR, TData login flows (+ device/proxy at login)
│       ├── scrape_members.py# Non-hidden & hidden group member scraping
│       ├── scrape_channel.py# Channel audience scraping (discussion roster + comments)
│       ├── add_members.py   # Rush & calm member adding
│       ├── broadcast_message.py # Message broadcast to scraped members
│       ├── proxy_manager.py # Add/test/assign proxies
│       ├── manage_sessions.py # List, test, cleanup sessions
│       └── about.py         # About screen
│
├── sessions/                # Encrypted session CSVs (not in repo)
├── logs/                    # Rotating log files (not in repo)
├── members.csv              # Scraped member data (not in repo)
├── proxies.csv              # Proxy pool, credentials encrypted (not in repo)
├── account_metadata.json    # Per-account device + proxy binding (not in repo)
├── scrape_checkpoint.json   # Group-scrape resume checkpoint (not in repo)
└── scrape_channel_checkpoint.json  # Channel-scrape resume checkpoint (not in repo)
```

</details>

<details>
<summary><b>Security</b></summary>

- **Session Encryption:** All Telegram session strings are encrypted using Fernet (AES-128-CBC + HMAC-SHA256). The encryption key is derived from your password using PBKDF2 with 480,000 iterations and a random 16-byte salt.
- **Local Storage Only:** All data (sessions, member lists, logs) is stored locally on your machine. The tool does not send data to any external server.
- **Phone Masking:** Phone numbers are always displayed masked in the UI and logs (e.g., `+1234***890`).
- **Credential Safety:** API credentials are loaded from `.env` which is excluded from version control via `.gitignore`.
- **No Session Logging:** Session strings are never written to log files.

</details>

<details>
<summary><b>Anti-Detection &amp; Safety</b></summary>

Telegram evaluates account "health" across three axes: the client/device signature, the network (IP/ASN) reputation, and request pacing. This tool addresses all three, but no tool can make abusive volume safe — pacing and account hygiene still matter most.

### Device/client spoofing (new logins)

Every account logged in through this version is assigned a realistic, **sticky** mobile device fingerprint (e.g. *Samsung Galaxy S24 Ultra / Android 14* or *iPhone 15 Pro Max / iOS 17.5.1*) instead of the default `CPython / Windows / Pyrogram` signature, and keeps it for the session's lifetime. The fingerprint is shown at login and stored in `account_metadata.json`. Existing sessions are left untouched (changing an established session's device fingerprint is itself suspicious).

### Proxies (network reputation)

Use **Option 06 — Proxy Manager** to bind residential or mobile proxies to your accounts. Datacenter IPs (AWS/DigitalOcean/Hetzner) are heavily flagged. Bindings are **sticky** — one IP per session, never rotated mid-session. Proxies are optional; without one, the account connects directly from your machine's IP.

### Rate limiting &amp; pacing

- **Jitter:** scrapers space out paced requests with a randomized human-like delay (≈2.5s ± 0.7s) rather than a mechanical fixed interval.
- **FloodWait policy (centralized):** a small wait is absorbed in place; a large one (≥1 hour) puts the account on a persistent cooldown and rotates to the next available account.
- **Adder/Broadcast delays:** members are added every 3–8s and broadcast DMs sent every 30–60s by default (tunable in `configs.py`).
- **Takeout mode (optional):** the Channel Scraper can route bulk reads through Telegram's Takeout API to insulate them from interactive flood limits.

### Account hygiene (manual, but important)

- Avoid brand-new accounts (registered within ~30 days) for heavy scraping — they're flagged fastest.
- "Warm up" a fresh account first: join a few public groups, send a few normal messages, use it like a human for a while before automating.
- Spread work across multiple accounts and keep volumes modest.

> **Legal/ToS:** Automated scraping and bulk adding/messaging can violate Telegram's Terms of Service and local laws. You are responsible for using this tool lawfully and with the consent required in your jurisdiction. Use it only against communities you are authorized to process.

</details>

<details>
<summary><b>Troubleshooting</b></summary>

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
- **Hidden scraping** extracts members from messages, mentions, and join service messages. Silent members are still caught via their "joined the group" message, but only as far back as the group's history goes (older joins whose service messages have aged out won't be found).
- Bots are automatically filtered out from results.

</details>

---

## <img src="assets/icons/faq.svg" width="24" height="24" alt="" /> FAQ

**What exactly do I get for $80?**
The complete Python source code (fully editable), lifetime access, every future update for free, and setup support — a one-time payment, not a subscription.

**How do I pay?**
Message [@AkibHridoy on Telegram](https://t.me/AkibHridoy) (or use [telegramscraper.shop](https://telegramscraper.shop/)) and payment is arranged directly in the chat. You'll be walked through it.

**Is it a one-time payment or a subscription?**
One-time. Pay once and the tool — plus all future updates — is yours for life.

**Do I get updates and support?**
Yes. Future versions are free, and you get help getting the tool set up on your machine.

**Can I run multiple instances at the same time?**
No. Session files and CSV data are shared, so running multiple instances can cause conflicts and data corruption.

**Is my session safe?**
Yes. Session strings are encrypted with Fernet using a password-derived key (PBKDF2, 480k iterations). Without your password, the encrypted session is unreadable.

**What if I forget my encryption password?**
Stored sessions cannot be recovered. You'll need to delete the `sessions/` directory and log in to your accounts again.

**Why does scraping miss some members?**
Non-hidden scraping only sees members in the public list. For groups that hide their member list, use the hidden scraping option which extracts members from message history, mentions, and "joined the group" service messages — the last of which captures silent members who never posted, as far back as the group's history reaches.

**Can I scrape a channel's subscribers?**
Not directly — Telegram only lets admins list a channel's subscribers. The Channel Scraper (Option 03) instead harvests the audience through the channel's linked discussion group (member roster, or a hidden-history fallback) and the authors of comments on its posts, then merges and de-duplicates them.

**Do I need proxies?**
No — proxies are optional and an account with none connects directly from your machine's IP. But for heavier use, binding a residential or mobile proxy (Option 06) significantly improves account longevity. Datacenter IPs are heavily flagged by Telegram.

**How many accounts do I need?**
Minimum 1. However, having multiple accounts helps with FloodWait rotation — when one account gets rate-limited, the tool automatically switches to the next available one.

**Does this work on mobile (Termux)?**
Yes. The tool runs on any platform with Python 3.8+: Windows, macOS, Linux, and Termux (Android). All dependencies are cross-platform.

**What happens if I interrupt a scrape with Ctrl+C?**
For hidden member scraping, progress is automatically saved to a checkpoint file. Next time you scrape the same group, you'll be offered to resume. For non-hidden scraping, members collected so far are still saved.

---

<div align="center">

### Ready to get started?

[![Buy Now](https://img.shields.io/badge/Buy%20Now-%2480%20USD-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/)
&nbsp;
[![Buy on Telegram](https://img.shields.io/badge/Buy%20on%20Telegram-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)

</div>

---

## License &amp; Legal

This software is proprietary and commercially licensed. By using this tool, you agree to the terms outlined in the [LICENSE](LICENSE) file, which includes the License Agreement, Terms of Service, Confidentiality &amp; Anti-Redistribution Policy, and Privacy Policy.

**Unauthorized redistribution of this software is strictly prohibited and will result in legal action.**

---

## Developer

**Abir Hasan**
- GitHub: [github.com/AbirHasan2005](https://github.com/AbirHasan2005)
- Telegram: [t.me/AbirHasan2005](https://t.me/AbirHasan2005)

> For purchases and support, contact **[@AkibHridoy](https://t.me/AkibHridoy)** or visit **[telegramscraper.shop](https://telegramscraper.shop/)**.
