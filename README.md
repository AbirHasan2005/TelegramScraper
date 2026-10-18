<div align="center">

# Telegram Scraper v1.8 – Python Telegram Member Scraper, Hidden Group Extractor, Channel Comment Scraper &amp; AI Lead Finder

**A production-ready, multi-account Telegram scraping and automation toolkit built on the MTProto User API** – extract visible and hidden group members, harvest broadcast channel audiences via linked discussions and post comments, discover niche groups with AI Lead Finder, add members with automatic `FloodWait` account rotation, and broadcast Markdown DMs from a rich terminal UI.

<br/>

[![Buy Now](https://img.shields.io/badge/Buy%20Now-%2480%20USD%20(Complete%20Toolkit)-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/pricing)
&nbsp;
[![Buy on Telegram](https://img.shields.io/badge/Live%20Demo%20%26%20Buy-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)
&nbsp;
[![Screenshots and Demo](https://img.shields.io/badge/Website%20%26%20Docs-telegramscraper.shop-24292F?style=for-the-badge&logo=googlechrome&logoColor=white)](https://telegramscraper.shop/)

<br/>

![Version](https://img.shields.io/badge/Version-v1.8-229ED9?style=flat-square)
![Source Code](https://img.shields.io/badge/Source%20Code-Full%20%26%20Editable-229ED9?style=flat-square)
![Access](https://img.shields.io/badge/License-One--Time%20Payment-2CA5E4?style=flat-square)
![Updates](https://img.shields.io/badge/Updates-Free%20Forever-229ED9?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Platforms](https://img.shields.io/badge/Platforms-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20Termux-555?style=flat-square)

</div>

---

## <img src="assets/icons/whats-included.svg" width="24" height="24" alt="" /> What You Get ($80 One-Time – Complete Toolkit)

[**Telegram Scraper v1.8**](https://telegramscraper.shop/) is a self-hosted Python CLI suite for **scraping Telegram group members (including hidden member lists), extracting channel comment &amp; discussion audiences, discovering niche communities across multiple accounts, adding members to target groups, and sending targeted DM broadcasts** – with sticky proxy binding, mobile device fingerprint spoofing, and Fernet-encrypted local sessions.

This is a commercial software toolkit. Your **one-time payment of $80 USD** ([view pricing details](https://telegramscraper.shop/pricing)) includes **every module** – never sold per-module and never billed as a subscription:

- **[Group Member Scraper (`Option 02`)](https://telegramscraper.shop/scraper)** – Visible participant roster scraper + hidden member extractor (message history, `@mentions`, and join events) + external `.txt`/`.csv` lead list importer
- **[Channel Audience Scraper (`Option 03`)](https://telegramscraper.shop/channel-scraper)** – Two-phase OSINT scraper for broadcast channels via post comment authors + linked discussion group roster &amp; history
- **[Members Adder (`Option 04`)](https://telegramscraper.shop/adder)** – Rush &amp; Calm group member adder with `PeerFlood` contact-workaround, configurable human jitter, and automatic multi-account rotation
- **[Message Broadcast / Mass DM (`Option 05`)](https://telegramscraper.shop/sender)** – Markdown-to-Telegram HTML DM sender with live preview, dry-run estimator, and auto-resume
- **[AI Lead Finder &amp; Niche Discovery (`Option 08`)](https://telegramscraper.shop/ai-telegram-scraper)** – Multi-account Telegram keyword search, spelling expansion, similar-channel graph traversal, and optional Gemini/Vertex AI discovery
- **[Live Monitors (`Option 10`)](https://telegramscraper.shop/lead-generation)** – Real-time **New-Member Join Monitor** and **Live Keyword Listener** that stream newly joined users or buying-intent message senders directly into `members.csv`
- **Full, Unobfuscated Python Source Code** – Inspect, audit, and customize every `.py` file for your own workflows
- **Lifetime Free Updates &amp; 1-on-1 Setup Support** – Run on Windows, macOS, Linux VPS, or [Android Termux](https://telegramscraper.shop/blog/telegram-scraper-termux-android)

<div align="center">

[![Get the Complete Toolkit – $80 USD](https://img.shields.io/badge/Get%20Complete%20Toolkit-%2480%20One--Time-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/pricing)
&nbsp;
[![Ask for a Free Live Demo on Telegram](https://img.shields.io/badge/Request%20Live%20Demo-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)

</div>

---

## <img src="assets/icons/features.svg" width="24" height="24" alt="" /> Core Modules &amp; What's New in v1.8

### 1. [Telegram Group Member Scraper (Visible &amp; Hidden Rosters)](https://telegramscraper.shop/scraper)
- **Visible Roster Mode (`01`):** Extracts the public member list of any group or supergroup, filtering out bots and deduplicating by User ID.
- **Hidden Member Recovery Mode (`02`):** When group admins hide the participant list ([`CHAT_ADMIN_REQUIRED`](https://telegramscraper.shop/blog/telegram-chat-admin-required-error-fix)), the scraper walks message history, `@username` mentions, clickable text mentions, and `"X joined the group"` service messages to recover active participants and recent joiners ([learn how hidden member extraction works](https://telegramscraper.shop/blog/telegram-hidden-members)).
- **Dry-Run Group Preview (`03`):** Inspect a target group's member count, check whether its roster is visible or hidden, get a mode recommendation, and preview 5 sample members (`@username`, User ID, last-seen status) before running a full scrape.
- **On-the-Fly Scrape Filters, Multi-Format Export (`04`) &amp; External Import (`05`):** Filter scrapes by activity window (`online`/`recently`/`last_week`, or exclude `long_time_ago`) and `@username` presence, export to **[CSV, `@username` `.txt` lists, or structured `.json`](https://telegramscraper.shop/export-to-csv)**, or import external `.txt`/`.csv` username and ID lists directly into `members.csv`.

### 2. [Telegram Channel Scraper (Post Comments + Linked Discussion)](https://telegramscraper.shop/channel-scraper)
- Telegram's servers block non-admins from reading a broadcast channel's direct subscriber list (`CHAT_ADMIN_REQUIRED`). No library or fork can bypass that server-side check.
- **Phase 1 – Post Comment Authors:** Scans channel posts and extracts every user who commented on discussion threads.
- **Phase 2 – Linked Discussion Supergroup:** Auto-joins the channel's linked discussion group and merges **both** its visible roster and full message history scan to capture members beyond the ~10k roster cap.
- **Dry-Run Channel Preview &amp; Takeout Mode:** Verify whether a target channel has a linked discussion group before scraping, and optionally route bulk reads through Telegram's Takeout API.

### 3. [AI Telegram Lead Finder &amp; Multi-Account Search (`Option 08`)](https://telegramscraper.shop/ai-telegram-scraper)
- **Start from a niche, not a link:** Enter a market concept (e.g., `copy trading` or `prop firm`) and the tool expands it into search spellings (`copy trading`, `copytrading`, `copy_trading`, etc.).
- **Multi-Account Global Search:** Searches every keyword across **all logged-in Telegram accounts** and merges results – solving [why Telegram global search shows so few groups on a single account](https://telegramscraper.shop/blog/why-telegram-search-shows-few-groups).
- **4 Discovery Vectors:** Native multi-account Telegram search, Telegram's *"Similar Channels"* graph, seed links, and optional Google Gemini / Vertex AI web search.
- **Smart Gate &amp; Keyword Memory:** Automatically swaps broadcast channels for their linked discussion groups (dropping channels that have none), tracks how many real members each keyword earned, and retires dead search terms after 3 empty runs. Works **with or without AI configured**.

### 4. [Telegram Member Adder (`Option 04`)](https://telegramscraper.shop/adder) &amp; [Mass DM Broadcaster (`Option 05`)](https://telegramscraper.shop/sender)
- **Rush &amp; Calm Adder Modes:** Remove processed users from `members.csv` automatically (Rush) for clean resume, or keep `members.csv` intact (Calm). Includes a `PeerFlood` temporary-contact workaround, external `.txt`/`.csv` list import (`04`), and **Dry-Run Adder Preview (`03`)** to verify target group invite permissions and estimate completion time.
- **Markdown Message Broadcast:** Write your DM in Markdown (`message_template.md`), preview the converted Telegram HTML in your terminal, run a **Dry-Run Broadcast Preview (`[d]`)** to check active accounts and estimated duration, and send with customizable human delays (`30–60s` default, tunable in `Option 09 -> 08`).

### 5. [Real-Time Live Monitors (`Option 10`)](https://telegramscraper.shop/lead-generation)
- **New-Member Join Monitor (`01`):** Watches one or more target groups in real time and captures newly joined users (plus newly active posters when join service notices are hidden) directly into `members.csv`.
- **Live Keyword Listener (`02`):** Watches target groups for buying-intent keywords (e.g., `looking for, need dev, price, dm me`) and saves matching message authors immediately to `members.csv` tagged with the matched keyword.

### 6. Setup Automation, Account Health Dashboard, Post-Run Reports &amp; Error Translator
- **One-Command Setup (`setup.bat` &amp; `setup.sh`):** Checks Python `>= 3.8`, installs dependencies and `TgCrypto`, creates `.env` from `.env.example` (prompting for `API_ID` / `API_HASH`), runs `check_setup.py`, and launches `main.py`.
- **Built-In Healthcheck (`python check_setup.py` / `Option 09 -> 07`):** Verifies Python, `TgCrypto` C-extension, required packages, and `.env` credentials with a clear pass/fail table without logging secrets.
- **Account Health &amp; Session Dashboard (`Option 07`):** Shows summary counts (`Total` | `Active Ready` | `Cooling Down` | `Inactive / Restricted`), live `FloodWait` cooldown timers, sticky proxy IDs, mobile device profiles, and a 1-click cooldown timer reset (`04`).
- **Post-Run Summary Reports (`logs/last_run_summary.txt`):** Every scrape, add, broadcast, or live monitor run renders a detailed terminal summary (including skip reasons, accounts used, and `FloodWait` hits) and saves it to `logs/last_run_summary.txt`.
- **Plain-English Telegram Error Translator:** Translates cryptographic/RPC exceptions (`CHAT_ADMIN_REQUIRED`, `PEER_FLOOD`, `USER_PRIVACY_RESTRICTED`, `FLOOD_WAIT_X`, `AUTH_KEY_UNREGISTERED`, etc.) into clear **"What happened"** and **"Tip: What to do"** guidance directly in the terminal.

### 7. Anti-Detection, Proxies &amp; Local Security
- **Sticky Mobile Device Spoofing:** Assigns each new login a realistic mobile device profile (*Samsung Galaxy S24 Ultra / Android 14*, *iPhone 15 Pro Max / iOS 17.5.1*) persisted in `account_metadata.json`.
- **Sticky Proxy Manager (`Option 06`):** Bind SOCKS5, SOCKS4, or HTTP residential/mobile proxies stickily per account so an account never switches IP mid-session.
- **Fernet AES-128 Session Encryption:** All session strings and proxy credentials are encrypted at rest using PBKDF2-HMAC-SHA256 (`480,000` iterations). Nothing ever leaves your machine.

---

## 📊 Why MTProto User API vs. Telegram Bot API &amp; Cloud Scrapers

Many free scripts and SaaS scrapers rely on the [Telegram Bot API](https://telegramscraper.shop/blog/telegram-scraper-vs-bot-api) or browser DOM scraping. Here is how **Telegram Scraper v1.8** compares:

| Capability | Telegram Scraper v1.8 (MTProto User API) | Standard Telegram Bot API | Cloud SaaS / Browser Scrapers |
|---|---|---|---|
| **Scrape Visible Group Members** | ✅ Full roster (`get_participants`) | ❌ Blocked unless bot is admin | ⚠️ Capped by web scroll buffer |
| **Scrape Hidden Group Members** | ✅ History + `@mentions` + join events | ❌ Impossible | ❌ Impossible |
| **Scrape Channel Audience** | ✅ Post comments + linked discussion | ❌ Blocked (`CHAT_ADMIN_REQUIRED`) | ⚠️ Partial or unsupported |
| **Multi-Account Niche Discovery** | ✅ Built-in (`Option 08` AI Lead Finder) | ❌ No global user search | ❌ Single-session only |
| **Real-Time Join &amp; Keyword Monitors** | ✅ Built-in (`Option 10` Live Monitors) | ⚠️ Requires bot added to target group | ❌ Not supported |
| **Auto `FloodWait` Account Rotation** | ✅ Persistent cooldowns + auto-switch | ❌ Single bot token | ❌ Manual intervention |
| **Sticky Device &amp; Proxy Anti-Detection** | ✅ Per-account mobile fingerprint + proxy | ➖ N/A | ❌ Shared datacenter IPs (high ban risk) |
| **Data Privacy &amp; Session Storage** | ✅ 100% local, Fernet AES-128 encrypted | ✅ Local | ❌ Credentials uploaded to 3rd-party cloud |
| **Cost** | **[`$80 USD` one-time](https://telegramscraper.shop/pricing)** (free updates forever) | Free (severely limited) | `$30–$99+/month` recurring credits |

### ⚠️ Before You Buy: Honest Telegram API Limits

We believe in transparent engineering rather than "100% magic" marketing claims. Before purchasing, please note Telegram's server-side rules ([read the full FAQ](https://telegramscraper.shop/faq)):

1. **Broadcast Channels Without a Linked Discussion Group:** Telegram blocks non-admins from reading a channel's subscriber list (`CHAT_ADMIN_REQUIRED`). Our [Channel Scraper](https://telegramscraper.shop/channel-scraper) extracts users who comment on posts and members of the channel's linked discussion group. If a channel has comments disabled and no linked discussion group, no tool can extract its subscribers.
2. **Hidden Group Rosters:** When a group hides its member list, Hidden Mode (`Option 02 -> 02`) recovers active posters, `@mentions`, and users whose `"joined the group"` service message is still in history. Totally silent users whose join notice was deleted cannot be seen by any non-admin tool.
3. **Phone Numbers:** Only returned when a user's own Telegram privacy settings expose their phone number to your logged-in account (typically `< 5%` of users). User IDs, `@usernames`, and `access_hash` are always captured.
4. **Rate Limits &amp; Account Safety:** Automated adding and DM broadcasting carry inherent Telegram rate-limit (`FloodWait` / `PeerFlood`) and account restriction risks. Use aged accounts, residential/mobile proxies, and conservative pacing ([read our anti-ban guide](https://telegramscraper.shop/blog/how-to-avoid-telegram-ban)).

---

## 📂 Sample Output Schema (`members.csv`, `.txt`, `.json`)

All scrapers (`Option 02`, `Option 03`, `Option 08`, and `Option 10`) merge and deduplicate leads by User ID into `members.csv` without overwriting previous runs:

```csv
Name,ID,Username,Phone Number,Access Hash,Group Name,Group ID
Alex Rivera,1000482910,alex_rivera_dev,,8492019384756102938,Crypto Traders Hub,-1001928374650
Sofia Lindqvist,1000593821,sofia_quant,,7381920495867213049,Crypto Traders Hub,-1001928374650
Marco Rossi,1000674932,mrossi_fx,,6270819384756102938,FX Signals (comments),-1001837465921
Elena Voronova,1000785043,,,5169708273645091827,FX Signals (discussion),-1001837465921
```

- **[Download the 20-Row Synthetic Sample CSV (`sample_members.csv`)](https://telegramscraper.shop/assets/sample_members.csv)** to test with your CRM, spreadsheet, or pipeline before buying.
- Need `@username`-only lists or JSON? Use `Option 02 -> 04 (Export & Filter Scraped Members)` to generate `members_usernames.txt`, `members_export.json`, or `members_with_username.csv` ([learn more about CSV/Excel exports](https://telegramscraper.shop/export-to-csv)).

---

## 🛡️ Verified Purchase Proofs &amp; Live Demo Before You Pay

We do not publish inflated buyer counters or unverified testimonials. Instead, you can verify the toolkit in two ways before spending a dollar:

1. **Request a Free Live Demo on Your Target Group:** Message **[@AkibHridoy on Telegram](https://t.me/AkibHridoy)** with a link to the Telegram group or channel you want to test. We will run a live screen-share or send you a 20-row sample scrape from your own target group so you can see the exact output first.
2. **Inspect Redacted Purchase Proofs &amp; Delivery Records:** View real, privacy-redacted buyer invoices, delivery confirmations, and git update history on our **[Verified Purchase Evidence page](https://telegramscraper.shop/purchase-evidence)** and **[Changelog](https://telegramscraper.shop/changelog)**.

<div align="center">

**[View Verified Purchase Proofs → telegramscraper.shop/purchase-evidence](https://telegramscraper.shop/purchase-evidence)**

</div>

---

## <img src="assets/icons/buy.svg" width="24" height="24" alt="" /> How to Buy

Getting the complete v1.8 toolkit takes about two minutes:

1. **Visit the store or message us on Telegram** – open **[telegramscraper.shop/pricing](https://telegramscraper.shop/pricing)** or message **[@AkibHridoy on Telegram](https://t.me/AkibHridoy)** directly.
2. **Optional live test** – send us your target group or channel link if you want us to verify scrapeability first.
3. **One-time payment ($80 USD)** – includes the complete Python source code for all modules, lifetime access, all future updates, and 1-on-1 setup assistance.
4. **Instant delivery** – receive the full repository/ZIP package and run `setup.bat` (Windows) or `bash setup.sh` (macOS/Linux/Termux) to launch in minutes.

<div align="center">

[![Buy Now – $80 USD](https://img.shields.io/badge/Buy%20Now-%2480%20USD-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/pricing)
&nbsp;
[![Message @AkibHridoy on Telegram](https://img.shields.io/badge/Buy%20on%20Telegram-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)

</div>

---

## 📚 Telegram Scraping Guides &amp; Technical Tutorials

New to MTProto scraping or troubleshooting a specific Telegram error? Read our free engineering guides on **[telegramscraper.shop/blog](https://telegramscraper.shop/blog/)**:

- **[How to Scrape Telegram Group Members in 2026 (Complete Guide)](https://telegramscraper.shop/blog/how-to-scrape-telegram-members)** – Visible rosters vs. message-history extraction explained step by step.
- **[How to Scrape Hidden Telegram Group Members](https://telegramscraper.shop/blog/telegram-hidden-members)** – Recovering active members when admins hide the participant list.
- **[Why Telegram Global Search Shows So Few Groups (And How Multi-Account Search Fixes It)](https://telegramscraper.shop/blog/why-telegram-search-shows-few-groups)** – How Telegram ranks global search by account region/history and how Option 08 expands coverage.
- **[How to Fix `CHAT_ADMIN_REQUIRED` When Scraping Telegram Channels &amp; Groups](https://telegramscraper.shop/blog/telegram-chat-admin-required-error-fix)** – Why direct channel subscriber dumps fail and how linked discussion + comment scraping works.
- **[How to Get Your Telegram `API_ID` and `API_HASH`](https://telegramscraper.shop/blog/how-to-get-telegram-api-id-hash)** – Step-by-step walkthrough for `my.telegram.org/apps`.
- **[Running a Telegram Scraper on Android with Termux](https://telegramscraper.shop/blog/telegram-scraper-termux-android)** – Full mobile setup guide for Android devices without root.
- **[How to Avoid Telegram Bans, `FloodWait`, and `PeerFlood` Errors](https://telegramscraper.shop/blog/how-to-avoid-telegram-ban)** – Account warm-up, residential/mobile proxies, and safe pacing intervals.
- **[Best Telegram Scrapers in 2026 – Honest Comparison](https://telegramscraper.shop/blog/best-telegram-scraper-2026)** – Comparing Python MTProto tools, browser extensions, and cloud platforms.
- **[MTProto User API vs. Telegram Bot API for Scraping](https://telegramscraper.shop/blog/telegram-scraper-vs-bot-api)** &amp; **[Telethon vs. Pyrogram](https://telegramscraper.shop/blog/telethon-vs-pyrogram)** – Architectural breakdown for Python developers.

---

## <img src="assets/icons/docs.svg" width="24" height="24" alt="" /> Full Documentation (v1.8)

Expand any section below to inspect the full CLI menu structure, installation steps, and module workflows.

<details>
<summary><b>Prerequisites &amp; One-Command Installation</b></summary>

### Prerequisites

- **Python 3.8+**
- **Git** (required to install the Pyrogram fork)
- **Telegram API Credentials** (`API_ID` and `API_HASH` from [my.telegram.org/apps](https://my.telegram.org/apps))

### Quick Automated Setup (Recommended)

After extracting your archive or cloning your private repository, run the included setup launcher for your OS. It verifies Python, installs `requirements.txt`, compiles/checks `TgCrypto`, creates `.env` from `.env.example` (prompting for `API_ID` and `API_HASH`), runs `check_setup.py`, and starts `main.py`:

- **Windows:**
  ```bat
  setup.bat
  ```
- **macOS / Linux / Termux (Android):**
  ```bash
  bash setup.sh
  ```

You can also run the standalone environment healthcheck at any time:
```bash
python check_setup.py
```
*(Or from inside the app via **Option 09 – Settings → 07 Test My Setup**.)*

### Manual Step-by-Step Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Optional: run `pip install -r requirements-ai.txt` if you want to enable Gemini / Vertex AI in Option 08.)*
2. **Create `.env` in the project root:**
   ```env
   API_ID=12345678
   API_HASH=your_api_hash_here
   ```
3. **Verify &amp; launch:**
   ```bash
   python check_setup.py
   python main.py
   ```

</details>

<details>
<summary><b>Quick Start &amp; Main Menu (v1.8)</b></summary>

When you launch the tool, you'll see the v1.8 main menu:

```
TelegramScraper v1.8
ℹ 0 sessions loaded (check Manage Sessions for status)

┌──────────────────────────────────────────┐
│                Main Menu                 │
├──────────────────────────────────────────┤
│  01  Login Telegram Account
│  02  Members Scraper
│  03  Channel Scraper
│  04  Members Adder
│  05  Message Broadcast
│  06  Proxy Manager
│  07  Manage Sessions & Account Health
│  08  AI Lead Finder
│  09  Settings
│  10  Live Monitors (Join & Keyword Watch)
│
│  99  About
│  00  Exit
└──────────────────────────────────────────┘
› Choose an option:
```

**Workflow A – You already have target group/channel links:**
1. *(Optional)* Add residential/mobile proxies in **Proxy Manager** (`Option 06`) before logging in.
2. **Login** one or more Telegram accounts (`Option 01`) – bind a proxy when prompted.
3. **Preview &amp; Scrape** members from a group (`Option 02`), channel (`Option 03`), or live monitor (`Option 10`), with optional `@username` / active-user filters.
4. **Export** to `.csv`, `.txt`, or `.json` (`Option 02 -> 04`), **Import** external lead lists (`Option 02 -> 05`), **Add** to your group (`Option 04`), or **Broadcast** a Markdown DM (`Option 05`).

**Workflow B – You want to discover groups in a market/niche:**
1. **Login** one or more accounts (`Option 01`). More accounts = broader Telegram search coverage.
2. Open **AI Lead Finder** (`Option 08`) → **Manage Niches** → create a niche (e.g., `copy trading`) with seed keywords.
3. Run **Preview Searches** (`03`) to see the exact search strings and estimated time before making any network calls.
4. Run **Discovery + Scrape** (`01`), select the groups you want to keep, and scrape them directly into `members.csv`.

</details>

<details>
<summary><b>Usage Guide – Options 01 to 10</b></summary>

### Option 01 – Login Telegram Account
Authenticate accounts via **Phone Number (OTP + 2FA)**, **Telegram Desktop TData import**, or **QR Code scan**. All sessions are encrypted locally in `sessions/` using Fernet (AES-128-CBC + HMAC-SHA256) with a PBKDF2-derived key (`480,000` iterations). New logins automatically receive a sticky mobile device fingerprint.

### Option 02 – Members Scraper
```
01 - Scrape Non-Hidden Members (from Group's Members List)
02 - Scrape Hidden Members (from Group's Messages/Mentions)
03 - Dry-Run / Preview Target Group (Check roster visibility & sample 5 members)
04 - Export & Filter Scraped Members (Save as .txt @usernames, .json, or filtered .csv)
05 - Import External ID / @Username List (.txt / .csv into members.csv)
00 - Go Back
```
- Supports on-the-fly filtering (**only users with `@username`** and/or **activity window** filtering).
- Checkpoints progress every 50 members to `scrape_checkpoint.json` for instant Ctrl+C resume.
- Writes post-run stats to `logs/last_run_summary.txt`.

### Option 03 – Channel Scraper
- **Optional Dry-Run Preview:** Checks channel subscriber count, linked discussion group, and discussion roster visibility before starting.
- **Phase 1 (Comment Authors):** Scans channel posts and extracts commenters.
- **Phase 2 (Discussion Members):** Joins the linked discussion supergroup and merges both the visible member roster and message-history scan.
- **Ctrl+C Phase Skip &amp; Checkpointing:** Pressing Ctrl+C skips the current phase or saves progress to `scrape_channel_checkpoint.json`.

### Option 04 – Members Adder
```
01 - Rush Adder (Remove user from 'members.csv' after adding)
02 - Calm Adder (Keep user in 'members.csv' after adding)
03 - Dry-Run / Preview Adder (Check target group permissions & estimate time)
04 - Import External ID / @Username List (.txt / .csv into members.csv)
00 - Go Back
```
- **Dry-Run Adder Preview (`03`):** Verifies target group invite permissions (`can_invite_users`), active accounts, and estimated run time without sending invites.
- **Post-Run Breakdown:** Summarizes added count, skip reasons (`privacy/limits`, `already in group`, `invalid`), accounts used, and `FloodWait` hits in the terminal and `logs/last_run_summary.txt`.

### Option 05 – Message Broadcast
- Converts Markdown (`message_template.md`) to Telegram HTML (`<b>`, `<i>`, `<s>`, `<code>`, `<pre>`, `<a href>`).
- Includes **`[d]ry-run preview`** to check active accounts, recipient counts, and estimated duration before sending DMs.
- Removes messaged users from `members.csv` on success so interrupted broadcasts can resume cleanly.

### Option 06 – Proxy Manager &amp; Option 07 – Manage Sessions &amp; Account Health
- Add, list, test, and stickily bind SOCKS5/SOCKS4/HTTP proxies to accounts (`Option 06`).
- View the **Account Health Dashboard** (`Total` | `Active Ready` | `Cooling Down` | `Inactive`), live `FloodWait` cooldown countdowns, sticky proxy IDs, mobile device profiles, test live connectivity (`get_me()`), remove deactivated sessions, or clear local cooldown timers (`Option 07`).

### Option 08 – AI Lead Finder, Option 09 – Settings &amp; Option 10 – Live Monitors
- **Option 08 Sub-Menu:** `01 Run Discovery + Scrape`, `02 Manage Niches`, `03 Preview Searches`, `04 Keyword Report`, `05 Discovered Groups`.
- **Option 09 Sub-Menu:** `01 Volume Preset (Conservative/Moderate/Aggressive)`, `02 Scrape Mode`, `03 Automation Mode`, `04 Discovery Modes`, `05 Advanced Limits`, `06 AI Status`, `07 Test My Setup`, `08 Adder & Broadcast Pacing (Delays & FloodWait Threshold)`, `09 Reset to Defaults`.
- **Option 10 Sub-Menu:** `01 New-Member Join Monitor (Real-Time Group Joiners -> members.csv)`, `02 Live Keyword Listener (Capture Buying-Intent Senders -> members.csv)`.

</details>

<details>
<summary><b>Project Structure (v1.8)</b></summary>

```
TelegramScraper/
├── main.py                  # Entry point, main menu loop
├── setup.bat                # Automated setup & launcher script (Windows)
├── setup.sh                 # Automated setup & launcher script (macOS/Linux/Termux)
├── check_setup.py           # Environment & credential healthcheck (CLI + menu)
├── run_summary.py           # Post-run summary renderer & logs/last_run_summary.txt writer
├── error_translator.py      # Plain-English Telegram RPC error explanations & tips
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
├── settings_store.py        # User-editable settings (settings.json)
├── requirements.txt         # Pinned dependencies
├── requirements-ai.txt      # Optional Vertex AI dependency (Option 08 only)
├── .env.example             # Template for .env configuration
├── LICENSE                  # License & Terms of Service
│
├── leadfinder/              # AI Lead Finder engine
│   ├── keyword_variants.py  # Concepts -> search spellings (pure, no AI)
│   ├── ai_provider.py       # Vertex AI (Gemini): optional AI integration
│   ├── niche_store.py       # The niche library (niches.json)
│   ├── term_store.py        # Search-term yield + retirement (search_terms.json)
│   ├── group_store.py       # Every group seen, incl. dead ends + skip memory
│   └── discovery.py         # The four-mode discovery orchestrator
│
└── funcs/
    ├── ui.py                # Rich console styling, prompts, plain-English error tips
    ├── helpers.py           # Session loading, filters, CSV/TXT/JSON export & import helpers
    └── options_handlers/
        ├── login.py         # Phone, QR, TData login flows (+ device/proxy at login)
        ├── scrape_members.py# Visible, hidden, dry-run, export & import group workflows
        ├── scrape_channel.py# Channel audience scraping (comments + discussion)
        ├── add_members.py   # Rush, calm & dry-run member adding + external list import
        ├── broadcast_message.py # Markdown DM broadcast + dry-run preview
        ├── proxy_manager.py # Add/test/assign proxies
        ├── manage_sessions.py # Account Health Dashboard, test, cleanup & cooldown reset
        ├── ai_lead_finder.py# Niche -> discovery -> scrape (Option 08)
        ├── settings_menu.py # Settings, Test My Setup & Pacing screens (Option 09)
        ├── live_monitors.py # Real-time Join Monitor & Keyword Listener (Option 10)
        └── about.py         # About screen
```

</details>

---

## <img src="assets/icons/faq.svg" width="24" height="24" alt="" /> Frequently Asked Questions

**What is the price and what is included?**
**$80 USD one-time** for the complete v1.8 toolkit ([see pricing](https://telegramscraper.shop/pricing)): Group Scraper (visible + hidden), Channel Scraper (comments + linked discussion), Members Adder, Mass DM Broadcaster, AI Lead Finder, Proxy Manager, full editable Python source code, and lifetime free updates. No recurring subscription.

**Can I see it working before I pay?**
Yes. Message **[@AkibHridoy on Telegram](https://t.me/AkibHridoy)** with a group or channel link you care about and we will run a live screen-share demo or send a 20-row sample scrape from that target.

**Does it really scrape hidden group members?**
Yes, with an important technical distinction: when a group hides its member list, `Option 02 -> 02` scans the group's message history for message authors, `@mentions`, replies, and `"X joined the group"` service messages. It captures active participants and recent joiners, not 100% of silent accounts whose join message was deleted ([read more](https://telegramscraper.shop/blog/telegram-hidden-members)).

**Can it scrape a broadcast channel's subscribers?**
Telegram blocks non-admins from fetching a channel's raw subscriber list (`CHAT_ADMIN_REQUIRED`). `Option 03` ([Channel Scraper](https://telegramscraper.shop/channel-scraper)) extracts the channel's active audience via **post comments** and its **linked discussion group** (both visible roster and message history). If a channel has no linked discussion group and comments are off, no non-admin tool can scrape it.

**Will my Telegram accounts get banned?**
Scraping (reading) is low-risk when paced, and the toolkit includes randomized jitter, `FloodWait` auto-cooldowns, multi-account rotation, sticky mobile device fingerprints, and sticky proxy support. Bulk adding (`Option 04`) and cold DM broadcasting (`Option 05`) are aggressively policed by Telegram – never use your personal main account for adding/DMs; use aged secondary accounts with residential/mobile proxies ([read our safety guide](https://telegramscraper.shop/blog/how-to-avoid-telegram-ban)).

**What OS and devices does it run on?**
Any system with Python 3.8+: **Windows 10/11**, **macOS**, **Linux (Ubuntu/Debian VPS)**, and **[Android via Termux](https://telegramscraper.shop/blog/telegram-scraper-termux-android)**.

**What is your refund policy?**
If the toolkit cannot run on your machine and our support team cannot resolve it within 48 hours, you receive a full refund. See our complete **[Refund Policy](https://telegramscraper.shop/refund-policy)** and **[FAQ](https://telegramscraper.shop/faq)** for full details.

---

## 🌍 Multi-Language Documentation (TR / RU / PT)

- 🇹🇷 **Türkçe (`Telegram Üye Çekme ve Grup/Kanal Scraper`):** Gizli grup üyelerini geçmiş mesajlardan çıkarma, kanal yorum/tartışma grubu analizi, çoklu hesap rotasyonu (`FloodWait` koruması), gruba üye ekleme ve toplu DM gönderimi. Detaylar için: **[Türkçe Ana Sayfa](https://telegramscraper.shop/tr/)** · **[Fiyatlandırma ($80 Tek Seferlik)](https://telegramscraper.shop/tr/pricing)** · **[Sıkça Sorulan Sorular](https://telegramscraper.shop/tr/faq)**
- 🇷🇺 **Русский (`Телеграм Парсер Участников, Скрытых Групп и Каналов`):** Парсинг открытых и скрытых участников Telegram-групп через историю сообщений, сбор аудитории каналов через комментарии и чаты обсуждений, инвайтер и рассылка в ЛС с ротацией аккаунтов и прокси. Подробнее: **[Главная на русском](https://telegramscraper.shop/ru/)** · **[Цены ($80 единоразово)](https://telegramscraper.shop/ru/pricing)** · **[Частые вопросы (FAQ)](https://telegramscraper.shop/ru/faq)**
- 🇧🇷 **Português (`Extrator de Membros do Telegram e Automação MTProto`):** Extração de membros visíveis e ocultos de grupos, comentários de canais, adição de membros e disparo de mensagens em massa com rotação de contas. Veja mais: **[Página Inicial em Português](https://telegramscraper.shop/pt/)** · **[Preços ($80 Pagamento Único)](https://telegramscraper.shop/pt/pricing)** · **[Perguntas Frequentes](https://telegramscraper.shop/pt/faq)**

---

<div align="center">

### Ready to get started?

[![Buy Complete Toolkit – $80 USD](https://img.shields.io/badge/Buy%20Now-%2480%20USD%20(Complete%20Toolkit)-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://telegramscraper.shop/pricing)
&nbsp;
[![Request Live Demo on Telegram](https://img.shields.io/badge/Live%20Demo%20%26%20Support-%40AkibHridoy-2CA5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/AkibHridoy)

</div>

---

## License &amp; Legal

This software is proprietary and commercially licensed. By using this tool, you agree to the terms outlined in our [Terms of Service](https://telegramscraper.shop/terms), [Privacy Policy](https://telegramscraper.shop/privacy), and [Refund Policy](https://telegramscraper.shop/refund-policy). Automated scraping and messaging are subject to Telegram's Terms of Service and applicable local regulations; use only with authorized communities and consented migrations.

---

## Developer &amp; Contact

- **Official Website:** [telegramscraper.shop](https://telegramscraper.shop/)
- **Sales &amp; Live Demo (Telegram):** [@AkibHridoy](https://t.me/AkibHridoy)
- **Developer:** Abir Hasan – [github.com/AbirHasan2005](https://github.com/AbirHasan2005) · [@AbirHasan2005](https://t.me/AbirHasan2005)
