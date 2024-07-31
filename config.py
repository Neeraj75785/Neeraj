import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("21265409")
API_HASH = getenv("34c826fd1b989c35e338248d07ad3665")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7278624463:AAFh3-7nxD2xw_S9lT9-AD0kwVndc-O-BYQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://DxLEGEND143:DxLEGEND143@dxlegend.oztipqk.mongodb.net/?retryWrites=true&w=majority&appName=DxLEGEND")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 999999))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002223899421")

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("6559330178")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vicky0604hello/DCxMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_DC_BOTS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TEAM_DC_BOTS")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "821d1bf8430346b98aa98e62ceb31416")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5fad47a0e1a340ca9cf88d9aa60b494b")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQFEfAEARWbIKcZF17k0zqHrF-j6aeac_b4j38S1q5Ij5z91qJQdEWhBYiKnMagg4OVmWbfTdgToj5suMRcf6eZD5G3mqjbixiI9JgWOWl9OECkn_EM9EJZNCG0yAtH1xvZNmbGVCGmee-8OUtV3U7ioodkLtckXG_k4aKmb4hpi7L_txR36JEvEWcUBBEBtb3eZyEIoyOX31046McuFjfFBPRlJRMCSWgMEi8hSVI7Ugl6qNxzRfTZ_ja-0CNyuF4WLJb39Ut-itx-tPAd0vioAzO6Cb4PIwQBU9u0Kt_rrg7OIpvij5htXDI9xzaWBNQQK5_fLa39KhuI6UQGt8qwN-gAAAAGG92-CAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/83da25751161cc4b9d408.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/59d3d5fbaca41ec09f33d.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/954b70e8c68314875cb78.jpg"
STATS_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/92349afcdfb9da6f7c693.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/92349afcdfb9da6f7c693.jpg"
STREAM_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4cf64c2a1902b56a52d13.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
