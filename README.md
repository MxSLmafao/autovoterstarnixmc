# AutoMineVoter for StarnixMC 🤖

**An automated BOT/SCRIPT that votes for Minecraft Servers on multiple server listing sites.**

## Current Server Support

### StarnixMC 🎮
The bot now supports automated voting for **StarnixMC** on 8 different voting sites:

1. [Minecraft-MP](https://minecraft-mp.com/server/346812/vote/)
2. [Minecraft-Server.net](https://minecraft-server.net/details/StarnixMC/)
3. [MinecraftServers.org](https://minecraftservers.org/server/677380)
4. [TopG.org](https://topg.org/minecraft-servers/server-674622)
5. [TopMinecraftServers.org](https://topminecraftservers.org/vote/41289)
6. [MC-Servers.com](https://mc-servers.com/vote/5999)
7. [MCList.io](https://mclist.io/server/66958-play-starnixmc-xyz-indian-based-cracked-surv/vote)
8. [MCServerTime.com](https://mcservertime.com/server-starnixmc.2736/vote)

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- Chrome/Chromium browser installed

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/autovoterstarnixmc.git
cd autovoterstarnixmc
```

2. **Create virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Chrome (for headless servers)**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y chromium-browser chromium-chromedriver

# Or use Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

---

## Configuration

Edit `config.yaml` to customize settings:

```yaml
# Your Minecraft username
username: "RRF_GAMING"

# Enable proxy rotation (not recommended for most users)
is_proxy_change: False

# Show browser for manual captcha solving
# Set to False for headless/server environments
is_show_captcha: False

server:
  StarnixMC:
    -minecraft_mp_com
    -minecraft_server_net
    -minecraftservers_org
    -topg_org
    -topminecraftservers_org
    -mc_servers_com
    -mclist_io
    -mcservertime_com
```

---

## Usage

### Run the bot
```bash
python3 main.py
```

### Headless Mode (for servers)
The bot automatically runs in headless mode when `is_show_captcha: False` in config.yaml.

### Manual Captcha Mode (for desktop)
Set `is_show_captcha: True` if you want to manually solve captchas (requires GUI).

---

## Features

- ✅ Automated voting on 8 different server listing sites
- ✅ Headless mode support for servers
- ✅ Automatic ChromeDriver management
- ✅ Configurable proxy support
- ✅ Error handling and retry logic
- ✅ Vote confirmation messages

---

## Troubleshooting

### ChromeDriver issues
The bot now automatically downloads and manages ChromeDriver using `webdriver-manager`. No manual setup required!

### Headless mode not working
Make sure you have Chrome/Chromium installed and the following packages:
```bash
sudo apt install -y chromium-browser
```

### Captcha errors
Some sites may still require captcha solving. Set `is_show_captcha: True` and run on a machine with GUI.

---

## Notes

- This voting automation is allowed by the server listing sites
- Vote limits typically reset every 24 hours
- Some sites may have additional anti-bot measures

---

## Credits

Based on AutoMineVoter project. Extended to support StarnixMC server with 8 voting sites.
